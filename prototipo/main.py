# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask_wtf import CSRFProtect
from negocio.aulaABM import AulaABM

import forms

app = Flask(__name__, template_folder="vistas")
app.secret_key = 'clavesupersecreta100porcientosegurarealnofake'
csrf = CSRFProtect(app)


@app.route('/')  # rutas a las que el usuario puede entrar
def index():
    return render_template('index.html', titulo="Campus Gestion")


@app.route('/login/login', methods=['GET', 'POST'])
def login():
    login = forms.Login(request.form)
    if request.method == 'POST' and login.validate():
        print login.usuario.data
        print login.contrasenia.data
    return render_template('Login/login.html', titulo="Login", form=login)


@app.route('/usuario/matricular', methods=['GET', 'POST'])
def matricular():
    matricular = forms.Matricular(request.form)
    if request.method == 'POST' and matricular.validate():
        print matricular.departamento.data
        print matricular.carrera.data
    return render_template('Usuario/matricular.html', titulo="Matricular", form=matricular)


@app.route('/return_file/')
def devolverarchivo():
    return send_file(
        'C:/Users/martin/Desktop/proyecto software/GestorDePedidos/prototipo/vistas/Archivos/Formulario_de_matriculacion.xlsx',
        attachment_filename='Formulario_de_matriculacion.xlsx')


@app.route('/aula/crear', methods=['GET', 'POST'])
def crear():
    crear_aula = forms.CrearAula(request.form)
    if request.method == 'POST' and crear_aula.validate():
        # abm = AulaABM()
        print crear_aula.departamento.data
        print crear_aula.carrera.data
        print crear_aula.nombreaula.data
        print crear_aula.nombredirector.data
        print crear_aula.emaildirector.data
        print crear_aula.nombredocente.data
        print crear_aula.apellidodocente.data
        print crear_aula.dni.data
        print crear_aula.emailprofesor.data
        print crear_aula.rol.data
        print crear_aula.descripcion.data

        # abm.insertar(crear_aula.dependencia.data, crear_aula.nombreAula.data, crear_aula.nombreprofesor.data,
        #             crear_aula.email.data)
    return render_template('Aula/crear.html', titulo="Crear aula", form=crear_aula)


@app.route('/aula/reutilizar', methods=['GET', 'POST'])
def reutilizar():
    reutilizar_aula = forms.ReutilizarAula(request.form)
    if request.method == 'POST' and reutilizar_aula.validate():
        print reutilizar_aula.departamento.data
        print reutilizar_aula.carrera.data
        print reutilizar_aula.nombreaula.data
        print reutilizar_aula.direccionulr.data
        print reutilizar_aula.nombredirector.data
        print reutilizar_aula.emaildirector.data
        print reutilizar_aula.nombrenuevo.data
        print reutilizar_aula.otro.data
    return render_template('Aula/reutilizar.html', titulo="Reutilizar aula", form=reutilizar_aula)


@app.route('/aula/eliminar', methods=['GET', 'POST'])
def eliminar():
    eliminar_aula = forms.EliminarAula(request.form)
    if request.method == 'POST' and eliminar_aula.validate():
        print eliminar_aula.departamento.data
        print eliminar_aula.carrera.data
        print eliminar_aula.nombreaula.data
        print eliminar_aula.direccionulr.data
        print eliminar_aula.nombredirector.data
        print eliminar_aula.emaildirector.data
        print eliminar_aula.motivo.data
    return render_template('Aula/eliminar.html', titulo="Eliminar aula", form=eliminar_aula)


@app.route('/capacitacion/tutorias', methods=['GET', 'POST'])
def tutorias():
    tutorias = forms.Tutorias(request.form)
    if request.method == 'POST' and tutorias.validate():
        print tutorias.motivo.data
        print tutorias.nombre.data
        print tutorias.apellido.data
        print tutorias.email.data
        print tutorias.telefono.data
        print tutorias.dni.data
        print tutorias.fecha.data
        print tutorias.departamento.data
        print tutorias.carrera.data
        print tutorias.rol.data
    return render_template('Capacitacion/tutorias.html', titulo="Tutorias", form=tutorias)


@app.route('/capacitacion/microtalleres', methods=['GET', 'POST'])
def microtalleres():
    microtalleres = forms.Microtalleres(request.form)
    if request.method == 'POST' and microtalleres.validate():
        print microtalleres.nombre.data
        print microtalleres.apellido.data
        print microtalleres.email.data
        print microtalleres.telefono.data
        print microtalleres.dni.data
        print microtalleres.departamento.data
        print microtalleres.carrera.data
        print microtalleres.motivo.data
    return render_template('Capacitacion/microtalleres.html', titulo="Microtalleres", form=microtalleres)


if __name__ == '__main__':
    app.run(debug=True, port=8000)  # ejecuta el server
