# HIITA
This is a software developed in the subject CES28 from ITA to assist Personal Trainers to provide training sheets for their clients

## Requirements
Python: 3.7
Libs principais: flask, flask-mysqldb
Database: MySQL Community Server (obrigatório) and MySQL Workbench (opcional)
Frontend: Npm, Vuejs

## Instalação:

## Banco de dados

Para instalação ver documentação do próprio [MySQL](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/) para sua OS. O MySQL server funcionará como Daemon e não precisará mais ser inicializado, somente sendo necessário a configuração da base de dados.

### Flask API Backend
Inicialmente vamos realizar a instalação seguindo o passo a passo com as bibliotecas necessárias de Python. A versão utilizada para o python foi a 3.7.11.

```
pip install requirements.txt
```

### Vue Front-end
Foi utilizada a tecnologia Vue para implementar o front-end da aplicação. Para isso devemos segue abaixo um passo a passo para instalação:

Para instalar NPM ver [documentação](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm), a versão utilizada é a 8.1.4.

Uma vez instalada podemos instalar através do Node Package Manager(npm) a versão do vue desejada pelo terminal:

```
sudo npm install -g @vue/cli@4.5.11
```

## Setup Inicial

Todos os comandos aqui consideram o usuário na pasta raiz do projeto.

## Banco de dados
A geração do banco de dados inicial pode ser feita utilizando os arquivos disponibilizados na pasta database/dumpfiles:

- HIITA.sql: Base de dados inicial do projeto e caso queira criar a base de dados **hiita**
- hiita_mysql_dumpfile: Base de dados da apresentação final, onde assume que uma database importará o dump deste arquivo.

Para importar os bancos de dados utilize substituindo username por **root** caso seja sua instalação inicial do MySQL, ou por um usuário com acesso a modificações no MySQL. Além disso se desejar usar uma base já criada utilize hiita_mysql_dumpfile.sql e o nome da base existente, caso queira criar uma base hiita com as tabelas e dados, a segunda flag se torna opcional. E file naturalmeente são os arquivos que podem ser escolhidos anteriormente:

```
mysql -u [username] -p [database_name] < database/dumpfiles/[file.sql]
```

### Flask API Backend
No primeiro uso configurar no arquivo backend/API.py, os campos referentes a criação do banco de dados a seguir para uma utilização local, onde host é onde está o processo do MySQL server, User se refere ao usuário do MySQL, Password a senha para esse usuário, e DB (database) o banco de dados onde foi feito o setup inicial da base de dados do projeto:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hiita'
```

### Configurações adicionais
Aqui é necessário salientar que a API backend estará funcionando em http://127.0.0.1:5000/HIITA, e o frontend em http://localhost:8080/. Caso alguma modificação nessas portas seja feito, precisa ser propagado no projeto sob risco de não funcionar.

## Execução

### Flask API Backend
Para executar o backend do projeto, basta estar no diretório em um terminal:
```
flask --app backend/API.py run
```

A Flask API estará hosteada em http://127.0.0.1:5000/HIITA

### Vue Front-end
Para executar o frontend do projeto, em um novo terminal:
```
cd frontend
npm run serve
```

O Projeto agora pode ser acessado de qualquer Browser pela porta http://localhost:8080/.

