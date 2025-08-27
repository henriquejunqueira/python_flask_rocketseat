from flask import Flask, request, jsonify # Importa as bibliotecas Flask, request e jsonify
from flask_sqlalchemy import SQLAlchemy # Importa a biblioteca para trabalhar com SQLite
from flask_cors import CORS # Importa a biblioteca CORS que permite que sistemas externos acessem essa API (como o swagger por exemplo)
from flask_login import UserMixin # Importa a biblioteca de login UserMixin

app = Flask(__name__) # Cria uma instancia do aplicativo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db' # Define o local do banco de dados

db = SQLAlchemy(app) # Inicia a conexão com o banco de dados
CORS(app) # Utiliza o CORS

# Cria uma classe Usuário recebendo como parâmetro um model e o UserMixin para utilizar o login
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Define a coluna id da tabela product no banco de dados como chave primária
    username = db.Column(db.String(80), nullable=False, unique=True) # Define a coluna username da tabela user no banco de dados proibindo ser nulo e sendo único
    password = db.Column(db.String(80), nullable=True) # Define a coluna password da tabela user no banco de dados proibindo ser nulo

# Cria uma classe Produto recebendo como parâmetro um model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Define a coluna id da tabela product no banco de dados como chave primária
    name = db.Column(db.String(120), nullable=False) # Define a coluna name da tabela product no banco de dados
    price = db.Column(db.Float, nullable=False) # Define a coluna price da tabela product no banco de dados
    description = db.Column(db.Text, nullable=True) # Define a coluna description da tabela product no banco de dados

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
def get_product_details(product_id): # Define a função que a rota de listagem de um produto irá executar
    product = Product.query.get(product_id) # Recupera o produto do banco de dados
    # Verifica se o produto existe
    if product: # Se exite, o dado é recuperado do banco de dados
        return jsonify({ # retorna os dados recuperados como json
            "id": product.id,
            "nome": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "Product not found"}), 404 # Se não existe, retorna o erro 404 not found

@app.route('/api/products/update/<int:product_id>', methods=["PUT"]) # Define a rota de atualização de um produto
def update_product(product_id): # Define a função que a rota de atualização de um produto irá executar
    product = Product.query.get(product_id) # Recebe o produto que tenha o id procurado pelo usuário
    # Verifica se não tem um produto
    if not product: # Se não exite o produto, uma mensagem de erro é retornada com o código 404
        return jsonify({"message": "Product not found"}), 404 # Se não existe, retorna o erro 404 not found

    data = request.json
    if 'name' in data: # Verifica se a chave name existe nos dados que foram requisitados
        product.name = data['name'] # Se a verificação for verdadeira o product.name recebe os dados da chave name

    if 'price' in data: # Verifica se a chave price existe nos dados que foram requisitados
        product.price = data['price'] # Se a verificação for verdadeira o product.price recebe os dados da chave price

    if 'description' in data: # Verifica se a chave description existe nos dados que foram requisitados
        product.description = data['description'] # Se a verificação for verdadeira o product.description recebe os dados da chave description

    db.session.commit() # Atualiza os dados do banco de dados
    return jsonify({'message': 'Product updated successfully'}) # Retorna a mensagem de sucesso como json

@app.route('/api/products', methods=['GET']) # Define a rota de listagem de todos os produtos
def get_products(): # Define a função que a rota de listagen de todos os produtos irá executar
    products = Product.query.all() # Recebe todos os produtos
    product_list = [] # Cria uma lista de produtos vazia
    for product in products: # Cria um loop para listar os itens da lista de produtos
        product_data = { # recebe os dados recuperados como json
            "id": product.id,
            "name": product.name,
            "price": product.price
        }
        product_list.append(product_data) # Insere os dados que product_data tiver na lista
    return jsonify(product_list) # Retorna os valores inseridos na lista

if __name__ == "__main__": # Verifica se o arquivo está sendo executado diretamente ou importado por outro arquivo
    app.run(debug=True) # Executa a aplicação utilizando o modo debug