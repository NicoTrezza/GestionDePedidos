# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask_wtf import CsrfProtect
from negocio.aulaABM import AulaABM

import forms

app = Flask(__name__, template_folder="vistas")
app.secret_key = 'clavesupersecreta100porcientosegurarealnofake'
csrf = CsrfProtect(app)

@app.route('/')  # rutas a las que el usuario puede entrar
def index():
    return render_template('index.html', titulo="Campus Gestion")


@app.route('/usuario/matricular')
def matricular():
    return render_template('Usuario/matricular.html', titulo="Matricular")

@app.route('/return_file/')
def devolverarchivo():
    return send_file('C:/Users/martin/Desktop/proyecto software/GestorDePedidos/prototipo/vistas/Archivos/Formulario_de_matriculacion.xlsx', attachment_filename='Formulario_de_matriculacion.xlsx')


@app.route('/aula/crear', methods=['GET', 'POST'])
def crear():
    crear_aula = forms.CrearAula(request.form)
    if request.method == 'POST':
        abm = AulaABM()
        print crear_aula.dependencia.data
        print crear_aula.nombreAula.data
        print crear_aula.nombreprofesor.data
        print crear_aula.email.data
        print crear_aula.nombre.data
        print crear_aula.apellido.data
        print crear_aula.dni.data

        abm.insertar(crear_aula.dependencia.data, crear_aula.nombreAula.data, crear_aula.nombreprofesor.data,
                     crear_aula.email.data)
    return render_template('Aula/crear.html', titulo="Crear aula", form=crear_aula)


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


if __name__ == '__main__':
    app.run(debug=True, port=8000)  # ejecuta el server
