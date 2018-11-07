#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask_wtf import CSRFProtect
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask import jsonify

from flask_mail import Mail
from flask_mail import Message

from config import DevelopmentConfig
from negocio.loginABM import LoginABM

from negocio.aulaABM import AulaABM
from negocio.personaABM import PersonaABM
from negocio.microtallerABM import MicrotallerABM
from negocio.carreraABM import CarreraABM


from werkzeug.utils import secure_filename

import forms
import crearPdf

app = Flask(__name__, template_folder="vistas")
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()
mail = Mail()

usuariovalido = 'martin'

@app.before_request
def before_request():
    pass


@app.route('/')  # rutas a las que el usuario puede entrar
def index():
    usuario = ''
    if 'usuario' in session:
        usuario = session['usuario']
        print usuario
    return render_template('index.html', titulo="Campus Gestion", usuario=usuario)


@app.route('/login/login', methods=['GET', 'POST'])
def login():
    login_abm = LoginABM()
    login = forms.Login(request.form)
    if request.method == 'POST' and login.validate():
        mail = login.usuario.data
        contrasenia = login.contrasenia.data

        try:
            usuario = login_abm.traerXMail(mail)
            if usuario.getContrasenia() == contrasenia:
                mensajeBienvenida = 'Bienvenido {}'.format(login.usuario.data)
                flash(mensajeBienvenida)
                session['usuario'] = login.usuario.data
                return redirect(url_for('index'))
            else:
                mensajeError = u'usuario o contraseña no validas'#este es para la contraseña no valida
                flash(mensajeError)
        except:
            mensajeError1 = u'usuario o contraseña no validas'#este es para el usuario no valido
            flash(mensajeError1)

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
    #########
    login_abm = LoginABM()
    permisos = 0
    try:
        us = login_abm.traerXMail(session['usuario'])
        permisos = us.getPermisos()
    except:
        mensajeError1 = u'usuario no valido'  # este es para el usuario no valido
        flash(mensajeError1)
    print usuario
    print permisos

    ########
    if request.method == 'POST' and matricular.validate():
        if 'usuario' in session:
            if permisos == 1:
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
    ##
    login_abm = LoginABM()
    permisos = 0
    try:
        us = login_abm.traerXMail(session['usuario'])
        permisos = us.getPermisos()
    except:
        mensajeError1 = u'usuario no valido'  # este es para el usuario no valido
        flash(mensajeError1)
    if request.method == 'POST' and crear_aula.validate():
        if 'usuario' in session:
            if permisos == 1:
                aula_abm = AulaABM()
                persona_abm = PersonaABM()
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

                # guardo en la base de datos
                aula = ''
                try:
                    persona = persona_abm.traerXDni(crear_aula.dni.data)
                    idpersona = persona.idPersona
                except:
                    persona = None

                try:
                    aula_abm.traerXNombre(crear_aula.nombreaula.data)
                except:
                    aula = None

                if aula is None:
                    if persona is not None:
                        aula_abm.insertar(crear_aula.nombreaula.data, 'ulr', crear_aula.descripcion.data, crear_aula.carrera.data)
                        aula_abm.insertarpersona(idpersona, aula_abm.traerXNombre(crear_aula.nombreaula.data).idAula)
                    else:
                        persona_abm.insertar(crear_aula.nombredocente.data, crear_aula.apellidodocente.data,
                                             crear_aula.dni.data, crear_aula.emailprofesor.data, 4, None)
                        persona = persona_abm.traerXDni(crear_aula.dni.data)
                        idpersona = persona.idPersona
                        aula_abm.insertar(crear_aula.nombreaula.data, 'ulr', crear_aula.descripcion.data, crear_aula.carrera.data)
                        aula_abm.insertarpersona(idpersona, aula_abm.traerXNombre(crear_aula.nombreaula.data).idAula)
                else:
                    flash('el aula ya existe')

                if aula is None:
                    # creo el pdf
                    crearPdf.crear_aula(crear_aula.departamento.data, crear_aula.carrera.data, crear_aula.nombreaula.data,
                                        crear_aula.nombredirector.data, crear_aula.emaildirector.data,
                                        crear_aula.nombredocente.data, crear_aula.apellidodocente.data, crear_aula.dni.data,
                                        crear_aula.emailprofesor.data, crear_aula.rol.data, crear_aula.descripcion.data)

                    # creo el mail a enviar
                    msg = Message('Aula creada', sender=app.config['MAIL_USERNAME'],
                                  recipients=[crear_aula.emailprofesor.data])  # recipients es una lista!!

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
                    # archivo pdf adjunto
                    with app.open_resource("crear_aula.pdf") as pdf:
                        msg.attach("crear_aula.pdf", "documento/pdf", pdf.read())

                    # envio el mail
                    # mail.send(msg)

                    # elimino el pdf despues de enviado el mail
                    os.remove('crear_aula.pdf')
                usuario = session['usuario']

            else:
                flash('No tiene permisos')
        if usuario == '':
            flash('Necesita estar logueado para crear aula')

    return render_template('Aula/crear.html', titulo="Crear aula", form=crear_aula)


@app.route('/aula/reutilizar', methods=['GET', 'POST'])
def reutilizar():
    reutilizar_aula = forms.ReutilizarAula(request.form)
    usuario = ''
    ##
    login_abm = LoginABM()
    permisos = 0
    try:
        us = login_abm.traerXMail(session['usuario'])
        permisos = us.getPermisos()
    except:
        mensajeError1 = u'usuario no valido'  # este es para el usuario no valido
        flash(mensajeError1)
    if request.method == 'POST' and reutilizar_aula.validate():
        if 'usuario' in session:
            if permisos == 1:
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
    ##
    login_abm = LoginABM()
    permisos = 0
    try:
        us = login_abm.traerXMail(session['usuario'])
        permisos = us.getPermisos()
    except:
        mensajeError1 = u'usuario no valido'  # este es para el usuario no valido
        flash(mensajeError1)
    if request.method == 'POST' and eliminar_aula.validate():
        if 'usuario' in session:
            if permisos == 1:
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
    ##
    login_abm = LoginABM()
    permisos = 0
    try:
        us = login_abm.traerXMail(session['usuario'])
        permisos = us.getPermisos()
    except:
        mensajeError1 = u'usuario no valido'  # este es para el usuario no valido
        flash(mensajeError1)
    if request.method == 'POST' and tutorias.validate():
        if 'usuario' in session:
            if permisos == 1:
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
    ##
    login_abm = LoginABM()
    microtaller_abm = MicrotallerABM()
    microtalleres_docentes = microtaller_abm.listarDocentes()
    microtalleres_estudiantes = microtaller_abm.listarEstudiantes()
    permisos = 0
    try:
        us = login_abm.traerXMail(session['usuario'])
        permisos = us.getPermisos()
    except:
        mensajeError1 = u'usuario no valido'  # este es para el usuario no valido
        flash(mensajeError1)
    if request.method == 'POST' and microtalleres.validate():
        if 'usuario' in session:
            if permisos == 1:
                persona_abm = PersonaABM()
                print microtalleres.nombre.data
                print microtalleres.apellido.data
                print microtalleres.email.data
                print microtalleres.telefono.data
                print microtalleres.dni.data
                print microtalleres.departamento.data
                print microtalleres.carrera.data
                print microtalleres.motivo.data
                print request.form['microtaller']

                # guardo en la base de datos
                try:
                    persona = persona_abm.traerXDni(microtalleres.dni.data)
                    idpersona = persona.idPersona
                except:
                    persona = None

                if persona is not None:
                    microtaller_abm.insertarpersona(request.form['microtaller'], idpersona)
                else:
                    persona_abm.insertar(microtalleres.nombre.data, microtalleres.apellido.data,
                                         microtalleres.dni.data, microtalleres.email.data, 4, None)
                    persona = persona_abm.traerXDni(microtalleres.dni.data)
                    idpersona = persona.idPersona
                    microtaller_abm.insertarpersona(request.form['microtaller'], idpersona)

                    # creo el pdf
                    crearPdf.microtaller(microtalleres.nombre.data, microtalleres.apellido.data,
                                         microtalleres.email.data, microtalleres.telefono.data,
                                         microtalleres.dni.data,
                                         microtalleres.departamento.data, microtalleres.carrera.data,
                                         microtalleres.motivo.data, request.form['microtaller'])

                    # creo el mail a enviar
                    msg = Message('Microtaller', sender=app.config['MAIL_USERNAME'],
                                  recipients=[microtalleres.email.data])  # recipients es una lista!!

                    msg.html = render_template('email_microtaller.html',
                                               nombre=microtalleres.nombre.data,
                                               apellido=microtalleres.apellido.data,
                                               email=microtalleres.email.data,
                                               telefono=microtalleres.telefono.data,
                                               dni=microtalleres.dni.data,
                                               departamento=microtalleres.departamento.data,
                                               carrera=microtalleres.carrera.data,
                                               motivo=microtalleres.motivo.data,
                                               microtaller=request.form['microtaller']
                                               )
                    # archivo pdf adjunto
                    with app.open_resource("microtaller.pdf") as pdf:
                        msg.attach("microtaller.pdf", "documento/pdf", pdf.read())

                    # envio el mail
                    mail.send(msg)

                    # elimino el pdf despues de enviado el mail
                    os.remove('microtaller.pdf')

                usuario = session['usuario']
            else:
                flash('No tiene permisos')
        if usuario == '':
            flash('Necesita estar logueado para pedir microtaller')
    return render_template('Capacitacion/microtalleres.html', titulo="Microtalleres", form=microtalleres,
                           microtalleres_docentes=microtalleres_docentes, microtalleres_estudiantes=microtalleres_estudiantes)

carrera_abm = CarreraABM()
carreras = carrera_abm.listarxdepartamento(1)
eleccion = [(str(c.getIdCarreraa()), c.getNombreCarrera()) for c in carreras]

food = {
    '1': eleccion,
    # '1': ['apple', 'banana', 'cherry'],
    '2': ['onion', 'cucumber'],
    '3': ['sausage', 'beef'],
}


@app.route('/get_food/<foodkind>')
def get_food(foodkind):
    if foodkind not in food:
        return jsonify([])
    else:
        return jsonify(food[foodkind])


if __name__ == '__main__':
    csrf.init_app(app)
    mail.init_app(app)
    app.run(port=8000)  # ejecuta el server
