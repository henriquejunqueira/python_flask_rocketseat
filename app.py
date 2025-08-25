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
def add_product():
    data = request.json # Pega os dados na forma de json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))# Cria o produto
        db.session.add(product) # Cria a sessão de adição do produto
        db.session.commit() # Envia os dados para o banco
        return jsonify({"message": "Product added successfully"})
    return jsonify({'message': "Invalid product data"}), 400 # Retorna a resposta de erro como json e código de erro 400

if __name__ == "__main__": # Verifica se o arquivo está sendo executado diretamente ou importado por outro arquivo
    app.run(debug=True) # Executa a aplicação utilizando o modo debug