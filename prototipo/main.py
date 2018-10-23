#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask_wtf import CSRFProtect
from flask import session
from flask import url_for
from flask import redirect
from flask import flash

from flask_mail import Mail
from flask_mail import Message

from config import DevelopmentConfig
from negocio.aulaABM import AulaABM

from werkzeug.utils import secure_filename


import forms

app = Flask(__name__, template_folder="vistas")
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()
mail = Mail()

usuariovalido = 'martin'


@app.route('/')  # rutas a las que el usuario puede entrar
def index():
    usuario = ''
    if 'usuario' in session:
        usuario = session['usuario']
        print usuario
    return render_template('index.html', titulo="Campus Gestion", usuario=usuario)


@app.route('/login/login', methods=['GET', 'POST'])
def login():
    login = forms.Login(request.form)
    if request.method == 'POST' and login.validate():
        #print login.usuario.data
        #print login.contrasenia.data
        mensajeBienvenida = 'Bienvenido {}'.format(login.usuario.data)
        flash(mensajeBienvenida)

        session['usuario'] = login.usuario.data
    return render_template('Login/login.html', titulo="Login", form=login)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'usuario' in session:
        session.pop('usuario')
    return redirect(url_for('index'))


@app.route('/usuario/matricular', methods=['GET', 'POST'])
def matricular():
    matricular = forms.Matricular(request.form)
    usuario = ''
    if request.method == 'POST' and matricular.validate():
        if 'usuario' in session:
            if session['usuario'] == usuariovalido:
                print matricular.departamento.data
                print matricular.carrera.data

                f = request.files['file']
                filename = secure_filename(f.filename)
                f.save('C:/Users/martin/Desktop/proyecto software/GestorDePedidos/prototipo/vistas/Archivos/ ' + filename)

                usuario = session['usuario']
            else:
                flash('No tiene permisos')
        if usuario == '':
            flash('Necesita estar logueado para matricular')

    return render_template('Usuario/matricular.html', titulo="Matricular", form=matricular)


@app.route('/return_file/')
def devolverarchivo():
    return send_file(
        'C:/Users/martin/Desktop/proyecto software/GestorDePedidos/prototipo/vistas/Archivos/Formulario_de_matriculacion.xlsx',
        attachment_filename='Formulario_de_matriculacion.xlsx')


@app.route('/aula/crear', methods=['GET', 'POST'])
def crear():
    crear_aula = forms.CrearAula(request.form)
    usuario = ''
    if request.method == 'POST' and crear_aula.validate():
        if 'usuario' in session:
            if session['usuario'] == usuariovalido:
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

                #recipients es una lista!!
                msg = Message('Aula creada', sender=app.config['MAIL_USERNAME'],
                              recipients=[crear_aula.emailprofesor.data])
                msg.html = render_template('email.html',
                                           departamento=crear_aula.departamento.data,
                                           carrera=crear_aula.carrera.data,
                                           nombreaula=crear_aula.nombreaula.data,
                                           nombredirector=crear_aula.nombredirector.data,
                                           emaildirector=crear_aula.emaildirector.data,
                                           nombredocente=crear_aula.nombredocente.data,
                                           apellidodocente=crear_aula.apellidodocente.data,
                                           dni=crear_aula.dni.data,
                                           emailprofesor=crear_aula.emailprofesor.data,
                                           rol=crear_aula.rol.data,
                                           descripcion=crear_aula.descripcion.data)
                mail.send(msg)

                usuario = session['usuario']
                # abm.insertar(crear_aula.dependencia.data, crear_aula.nombreAula.data, crear_aula.nombreprofesor.data,
                #             crear_aula.email.data)
            else:
                flash('No tiene permisos')
        if usuario == '':
            flash('Necesita estar logueado para crear aula')
    return render_template('Aula/crear.html', titulo="Crear aula", form=crear_aula)


@app.route('/aula/reutilizar', methods=['GET', 'POST'])
def reutilizar():
    reutilizar_aula = forms.ReutilizarAula(request.form)
    usuario = ''
    if request.method == 'POST' and reutilizar_aula.validate():
        if 'usuario' in session:
            if session['usuario'] == usuariovalido:
                print reutilizar_aula.departamento.data
                print reutilizar_aula.carrera.data
                print reutilizar_aula.nombreaula.data
                print reutilizar_aula.direccionulr.data
                print reutilizar_aula.nombredirector.data
                print reutilizar_aula.emaildirector.data
                print reutilizar_aula.nombrenuevo.data
                print reutilizar_aula.otro.data
                usuario = session['usuario']
            else:
                flash('No tiene permisos')
        if usuario == '':
            flash('Necesita estar logueado para reutilizar aula')
    return render_template('Aula/reutilizar.html', titulo="Reutilizar aula", form=reutilizar_aula)


@app.route('/aula/eliminar', methods=['GET', 'POST'])
def eliminar():
    eliminar_aula = forms.EliminarAula(request.form)
    usuario = ''
    if request.method == 'POST' and eliminar_aula.validate():
        if 'usuario' in session:
            if session['usuario'] == usuariovalido:
                print eliminar_aula.departamento.data
                print eliminar_aula.carrera.data
                print eliminar_aula.nombreaula.data
                print eliminar_aula.direccionulr.data
                print eliminar_aula.nombredirector.data
                print eliminar_aula.emaildirector.data
                print eliminar_aula.motivo.data
                usuario = session['usuario']
            else:
                flash('No tiene permisos')
        if usuario == '':
            flash('Necesita estar logueado para eliminar aula')
    return render_template('Aula/eliminar.html', titulo="Eliminar aula", form=eliminar_aula)


@app.route('/capacitacion/tutorias', methods=['GET', 'POST'])
def tutorias():
    tutorias = forms.Tutorias(request.form)
    usuario = ''
    if request.method == 'POST' and tutorias.validate():
        if 'usuario' in session:
            if session['usuario'] == usuariovalido:
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
                usuario = session['usuario']
            else:
                flash('No tiene permisos')
        if usuario == '':
            flash('Necesita estar logueado para pedir tutoria')
    return render_template('Capacitacion/tutorias.html', titulo="Tutorias", form=tutorias)


@app.route('/capacitacion/microtalleres', methods=['GET', 'POST'])
def microtalleres():
    microtalleres = forms.Microtalleres(request.form)
    usuario = ''
    if request.method == 'POST' and microtalleres.validate():
        if 'usuario' in session:
            if session['usuario'] == usuariovalido:
                print microtalleres.nombre.data
                print microtalleres.apellido.data
                print microtalleres.email.data
                print microtalleres.telefono.data
                print microtalleres.dni.data
                print microtalleres.departamento.data
                print microtalleres.carrera.data
                print microtalleres.motivo.data
                usuario = session['usuario']
            else:
                flash('No tiene permisos')
        if usuario == '':
            flash('Necesita estar logueado para pedir microtaller')
    return render_template('Capacitacion/microtalleres.html', titulo="Microtalleres", form=microtalleres)


if __name__ == '__main__':
    csrf.init_app(app)
    mail.init_app(app)
    app.run(port=8000)  # ejecuta el server
