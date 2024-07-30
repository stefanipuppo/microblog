from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Stef"
    dados = {"profissao": "Desenvolvedora backend", "linguagem": "Python, Java"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')