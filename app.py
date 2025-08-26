from flask import Flask, request, jsonify # Importa as bibliotecas Flask, request e jsonify
from flask_sqlalchemy import SQLAlchemy # Importa a biblioteca para trabahar com SQLite 

app = Flask(__name__) # Cria uma instancia do aplicativo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db' # Define o local do banco de dados

db = SQLAlchemy(app) # Inicia a conexão com o banco de dados

# Cria uma classe Produto recebendo como parâmetro um model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Define a coluna id do banco de dados
    name = db.Column(db.String(120), nullable=False) # Define a coluna nome do banco de dados
    price = db.Column(db.Float, nullable=False) # Define a coluna preço do banco de dados
    description = db.Column(db.Text, nullable=True)

# Cria as rotas para comunicar com a API
@app.route('/') # Define uma rota raiz (página inicial) e a função que será executada quando o usuário requisitar
def hello_world(): # Define a função que a rota raiz irá executar
    return 'Hello World'

@app.route('/api/products/add', methods=["POST"]) # Define a rota de adição de produtos e o metodo como POST
def add_product(): # Define a função que a rota de adição irá executar
    data = request.json # Pega os dados na forma de json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))# Cria o produto
        db.session.add(product) # Cria a sessão de adição do produto
        db.session.commit() # Envia os dados para o banco de dados
        return jsonify({"message": "Product added successfully"}) # Retorna a mensagem de sucesso como json
    return jsonify({'message': "Invalid product data"}), 400 # Retorna a resposta de erro como json e código de erro 400

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"]) # Define a rota de remoção de produtos e o metodo como DELETE
def delete_product(product_id): # Define a função que a rota de remoção irá executar
    product = Product.query.get(product_id) # Recupera o produto do banco de dados
    # Verifica se o produto existe
    if product: # Se exite, o dado é removido do banco de dados
        db.session.delete(product) # Cria a sessão de remoção do produto
        db.session.commit() # Remove os dados do banco de dados
        return jsonify({"message": "Product deleted successfully"}) # Retorna a mensagem de sucesso como json
    return jsonify({"message": "Product not found"}) , 404 # Se não existe, retorna o erro 404 not found

@app.route('/api/products/<int:product_id>', methods=["GET"]) # Define a rota de listagem de um produto
def get_product_details(product_id): # Define a função que a rota de listagem de produtos irá executar
    product = Product.query.get(product_id) # Recupera o produto do banco de dados
    # Verifica se o produto existe
    if product: # Se exite, o dado é recuperado do banco de dados
        return jsonify({ # retorna os dados recuperados como json
            "id": product.id,
            "nome": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__": # Verifica se o arquivo está sendo executado diretamente ou importado por outro arquivo
    app.run(debug=True) # Executa a aplicação utilizando o modo debug