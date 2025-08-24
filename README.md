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
