from flask import Flask # Importa a biblioteca Flask

app = Flask(__name__) # Cria uma instancia do aplicativo

# Cria as rotas para comunicar com a API
@app.route('/') # Define uma rota raiz (página inicial) e a função que será executada quando o usuário requisitar
def hello_world(): # Define a função que a rota raiz irá executar
    return 'Hello World'

if __name__ == "__main__": # Verifica se o arquivo está sendo executado diretamente ou importado por outro arquivo
    app.run(debug=True) # Executa a aplicação utilizando o modo debug