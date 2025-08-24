# Python com Flask - Curso Introdutório

### Esse é um repositório para acompanhar o curso introdutório da RocketSeat

#### Aulas:

- Aula 01: Introdução ao Python e Flask;
- Aula 02: Integração de Banco de Dados, Roteamento e Modelos;
- Aula 03: Autenticação do Usuário;
- Aula 04: Construção da API de E-Commerce;
- Aula 05: Tópicos Avançados e Implantação;

#### Arquivos utilizados no projeto:

- requeriments.txt: Define as bibliotecas utilizadas no projeto
- .gitignore: Define os arquivos e pastas que não vou subir para o github
- app.py: Esse é o arquivo da aplicação

#### Comandos utilizados:

- Instalando bibliotecas definidas no arquivo requeriments.txt:
  `pip3 install -r requeriments.txt`
- No caso de precisar instalar uma biblioteca sem utilizar o requeriments.txt é só utilizar:
  `pip3 install <nome_da_biblioteca==versão>`
- No meu caso criei uma vm python pra rodar o comando pip3:
  `/<caminho_completo_do_projeto>/.venv/bin/python -m pip3 install -r requeriments.txt`
- Obs: a pasta .venv adicionei ao arquivo .gitignore que criei no projeto, pois não tem necessidade de subir essa pasta para o github.
- Pra isso é só criar um .gitignore no projeto e adicionar nele:

```gitignore
.venv/
venv/
```

- Antes de rodar o projeto ativei o ambiente virtual venv:

`source .venv/bin/activate`

- Em seguida instalei o flask dentro do ambiente:

`pip install flask`

- Por último rodei o projeto:

`python3 app.py`

- Obs: No caso do windows posso ativar o ambiente do venv com o comando:

`.venv\Scripts\activate`

- Para desativar o ambiente basta rodar: deactivate;

- Obs: O ambiente está ativado ou desativado quando aparece (.venv), se aparecer apenas .venv é apenas uma customização do prompt;

- Após ativar o ambiente posso acessar a aplicação pelo navegador utilizando http://127.0.0.1:5000 ou via postman, httpie, insomnia colando o mesmo link com o número da porta e deve aparecer:

```bash * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 180-716-632
```
