# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="vistas")

@app.route('/')# rutas a las que el usuario puede entrar
def index():
    return render_template('index.html', titulo="Campus Gestion")


if __name__=='__main__':
    app.run(debug = True, port = 8000) #ejecuta el server