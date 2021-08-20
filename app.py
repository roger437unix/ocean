import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

# Configurações
DATABASE = "blog.db"
SECRET_KEY = "pudim"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_first_request
def antes_requisicao():
    g.bd = conectar_db()

@app.teardown_request
def depois_request(exc):
    g.bd.close()

@app.route('/')
def exibir_entradas():
    return render_template('exibir_entradas.html')

@app.route('/hello')
def pagina_inicial():
    return "Hello world"
