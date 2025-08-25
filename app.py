from flask import Flask # Importa a biblioteca Flask
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

if __name__ == "__main__": # Verifica se o arquivo está sendo executado diretamente ou importado por outro arquivo
    app.run(debug=True) # Executa a aplicação utilizando o modo debug