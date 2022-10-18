# HIITA
This is a software developed in the subject CES28 from ITA to assist Personal Trainers to provide training sheets for their clients

## Requirements
Python: 3.7
Libs: flask, flask-mysqldb
Database: MySQL Community Server and MySQL Workbench

## Instalação:

### Servidor
Inicialmente vamos realizar a instalação seguindo o passo a passo com as bibliotecas necessárias de Python. A versão utilizada para o python foi a 3.7.11.

```
pip install flask
pip install googletrans==3.1.0a0
pip install requests
pip install flask_sqlalchemy
pip install flask_cors
```
Para rodar:
```
flask --app backend/API.py run
```

### Cliente/Front-end
Foi utilizada a tecnologia Vue para implementar o front-end da aplicação. Para isso devemos segue abaixo um passo a passo para instalação:
```
sudo npm install -g @vue/cli@4.5.11
```

Para rodar:
```
npm run serve
```