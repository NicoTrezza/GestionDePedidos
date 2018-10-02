# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder="vistas")

@app.route('/')# rutas a las que el usuario puede entrar
def index():
    return render_template('index.html', titulo="Campus Gestion")
	
@app.route('/usuario/matricular')
def matricular():
    return render_template('Usuario/matricular.html', titulo="Matricular")
	
@app.route('/aula/crear', methods = ['GET', 'POST'])
def crear():
    if request.method == 'POST':
        print request.form['dependencia']
        print request.form['nombreaula']
	print request.form['nombreprofesor']
        print request.form['email']
	print request.form['nombre']
	print request.form['apellido']
        print request.form['dni']
    return render_template('Aula/crear.html', titulo="Crear aula")
	
@app.route('/aula/reutilizar')
def reutilizar():
    return render_template('Aula/reutilizar.html', titulo="Reutilizar aula")
	
@app.route('/aula/eliminar')
def eliminar():
    return render_template('Aula/eliminar.html', titulo="Eliminar aula")
	
@app.route('/capacitacion/tutorias')
def tutorias():
    return render_template('Capacitacion/tutorias.html', titulo="Tutorias")
	
@app.route('/capacitacion/microtalleres')
def microtalleres():
    return render_template('Capacitacion/microtalleres.html', titulo="Microtalleres")


if __name__=='__main__':
    app.run(debug = True, port = 8000) #ejecuta el server
