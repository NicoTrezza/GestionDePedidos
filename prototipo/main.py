#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask import render_template
from flask import request
from flask import send_file, send_from_directory
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
from negocio.tutoriaABM import TutoriaABM

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
        # print usuario
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
        # flash(mensajeError1)
    # print usuario
    # print permisos

    ########
    if request.method == 'POST' and matricular.validate():
        if 'usuario' in session:
            if permisos == 1:
                print matricular.departamento.data
                print request.form['carrera']

                f = request.files['file']
                filename = secure_filename(f.filename)
                f.save('C:/Users/martin/Desktop/proyecto software/GestorDePedidos/prototipo/' + filename)

                # creo el pdf
                crearPdf.matricular(matricular.departamento.data,
                                    request.form['carrera'])

                # creo el mail a enviar
                msg = Message('Aula creada', sender=app.config['MAIL_USERNAME'],
                              recipients=['olmos.martin.1992@gmail.com'])  # recipients es una lista!!

                msg.html = render_template('email_matricular.html',
                                           departamento=matricular.departamento.data,
                                           carrera=request.form['carrera']
                                           )
                # archivo pdf adjunto
                with app.open_resource("matricular.pdf") as pdf:
                    msg.attach("matricular.pdf", "documento/pdf", pdf.read())

                with app.open_resource("Formulario_de_matriculacion.xlsx") as excel:
                    msg.attach("Formulario_de_matriculacion.xlsx", "documento/xlsx", excel.read())

                # envio el mail
                mail.send(msg)

                # elimino el pdf despues de enviado el mail
                os.remove('matricular.pdf')
                os.remove('Formulario_de_matriculacion.xlsx')

                usuario = session['usuario']
            else:
                flash('No tiene permisos')
        if usuario == '':
            flash('Necesita estar logueado para matricular')
    return render_template('Usuario/matricular.html', titulo="Matricular", form=matricular)


@app.route('/return_file/')
def devolverarchivo():
    return send_from_directory('C:/Users/martin/Desktop/proyecto software/GestorDePedidos/prototipo/vistas/Archivos/', 'Formulario_de_matriculacion.xlsx', as_attachment=True)


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
        # flash(mensajeError1)
    if request.method == 'POST' and crear_aula.validate():
        if 'usuario' in session:
            if permisos == 1:

                cant_docentes = 5  # es uno menos que el numero
                aula_abm = AulaABM()
                persona_abm = PersonaABM()

                lista_mails = []

                print crear_aula.departamento.data
                print request.form['carrera']
                print crear_aula.nombreaula.data

                for i in range(1, cant_docentes):
                    print "We're on time %d" % (i)
                    try:

                        print request.form['nombredocente' + str(i)]
                        print request.form['apellidodocente' + str(i)]
                        print request.form['dni' + str(i)]
                        print request.form['emailprofesor' + str(i)]
                        print request.form['rol' + str(i)]
                        lista_mails.append(request.form['emailprofesor' + str(i)])

                    except:
                        print 'un error'

                print crear_aula.descripcion.data

                # guardo en la base de datos
                aula = ''

                idpersona = []

                try:
                    aula_abm.traerXNombre(crear_aula.nombreaula.data)
                except:
                    aula = None

                if aula is None:
                    for i in range(1, cant_docentes):
                        try:
                            print 'intento' + str(i)
                            persona = persona_abm.traerXDni(request.form['dni' + str(i)])
                            idpersona.append(persona.getIdPersona())
                        except:
                            try:
                                persona_abm.insertar(request.form['nombredocente' + str(i)],
                                                     request.form['apellidodocente' + str(i)],
                                                     request.form['dni' + str(i)],
                                                     request.form['emailprofesor' + str(i)],
                                                     request.form['rol' + str(i)],
                                                     None)
                                print request.form['dni' + str(i)]
                                persona = persona_abm.traerXDni(request.form['dni' + str(i)])
                                idpersona.append(persona.getIdPersona())
                            except:
                                print 'no se ingresaron datos / dni repetido'

                print idpersona

                if aula is None:
                    if persona is not None:
                        aula_abm.insertar(crear_aula.nombreaula.data, crear_aula.descripcion.data,
                                          crear_aula.departamento.data)
                        for idp in idpersona:
                            aula_abm.insertarpersona(idp, aula_abm.traerXNombre(crear_aula.nombreaula.data).idAula)
                    # else:
                    #    persona_abm.insertar(crear_aula.nombredocente.data, crear_aula.apellidodocente.data,
                    #                         crear_aula.dni.data, crear_aula.emailprofesor.data, crear_aula.rol.data, None)
                    #    persona = persona_abm.traerXDni(crear_aula.dni.data)
                    #    idpersona = persona.idPersona
                    #    aula_abm.insertar(crear_aula.nombreaula.data, crear_aula.descripcion.data, crear_aula.departamento.data)
                    #    aula_abm.insertarpersona(idpersona, aula_abm.traerXNombre(crear_aula.nombreaula.data).idAula)
                else:
                    flash('el aula ya existe')

                if aula is None:
                    # creo el pdf
                    """
                    request.form['nombredocente'],
                    request.form['apellidodocente'],
                    request.form['dni'].dni,
                    request.form['emailprofesor'],
                    request.form['rol'].rol,
                    """
                    lista_personas = []

                    for id in idpersona:
                        lista_personas.append(persona_abm.traer(id))

                    crearPdf.crear_aula(request.form['departamento'],
                                        request.form['carrera'],
                                        request.form['nombreaula'],
                                        lista_personas,
                                        request.form['descripcion'])


                    # creo el mail a enviar
                    msg = Message('Aula creada', sender=app.config['MAIL_USERNAME'],
                                  recipients=lista_mails)  # recipients es una lista!!

                    msg.html = render_template('email.html',
                                               departamento=request.form['departamento'],
                                               carrera=request.form['carrera'],
                                               nombreaula=request.form['nombreaula'],
                                               personas=lista_personas,
                                               descripcion=request.form['descripcion'])
                    # archivo pdf adjunto
                    with app.open_resource("crear_aula.pdf") as pdf:
                        msg.attach("crear_aula.pdf", "documento/pdf", pdf.read())

                    # envio el mail
                    # mail.send(msg)

                    # elimino el pdf despues de enviado el mail
                    # os.remove('crear_aula.pdf')

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
        # flash(mensajeError1)
    if request.method == 'POST' and reutilizar_aula.validate():
        if 'usuario' in session:
            if permisos == 1:
                print reutilizar_aula.departamento.data
                print request.form['carrera']
                print reutilizar_aula.nombreaula.data
                print reutilizar_aula.direccionulr.data

                print reutilizar_aula.nombredocente.data
                print reutilizar_aula.apellidodocente.data
                print reutilizar_aula.dni.data
                print reutilizar_aula.emailprofesor.data
                print reutilizar_aula.rol.data

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
        # flash(mensajeError1)
    if request.method == 'POST' and eliminar_aula.validate():
        if 'usuario' in session:
            if permisos == 1:
                print eliminar_aula.departamento.data
                print request.form['carrera']
                print eliminar_aula.nombreaula.data
                print eliminar_aula.direccionulr.data
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
    tutorias_abm = TutoriaABM()

    if request.method == 'POST' and tutorias.validate():

        persona_abm = PersonaABM()
        print tutorias.motivo.data
        print tutorias.nombre.data
        print tutorias.apellido.data
        print tutorias.email.data
        print tutorias.telefono.data
        print tutorias.dni.data
        print tutorias.departamento.data
        print request.form['carrera']
        print tutorias.rol.data
        print tutorias.grupal.data

        print tutorias.dia1.data
        print tutorias.dia1_hora1.data
        print tutorias.dia1_hora2.data

        print tutorias.dia2.data
        print tutorias.dia2_hora1.data
        print tutorias.dia2_hora2.data

        print tutorias.dia3.data
        print tutorias.dia3_hora1.data
        print tutorias.dia3_hora2.data

        # guardo en la base de datos
        try:
            persona = persona_abm.traerXDni(microtalleres.dni.data)
            idpersona = persona.idPersona
        except:
            persona = None

        if persona is not None:
            tutorias_abm.insertar(tutorias.motivo.data, idpersona, tutorias.departamento.data)
        else:
            persona_abm.insertar(tutorias.nombre.data, tutorias.apellido.data,
                                 tutorias.dni.data, tutorias.email.data, tutorias.rol.data, None)
            persona = persona_abm.traerXDni(tutorias.dni.data)
            idpersona = persona.idPersona
            tutorias_abm.insertar(tutorias.motivo.data, idpersona, tutorias.departamento.data)

        # creo el pdf
        crearPdf.tutoria(tutorias.motivo.data,
                         tutorias.nombre.data,
                         tutorias.apellido.data,
                         tutorias.email.data,
                         tutorias.telefono.data,
                         tutorias.dni.data,
                         tutorias.departamento.data,
                         request.form['carrera'],
                         tutorias.rol.data,
                         tutorias.grupal.data,
                         tutorias.dia1.data,
                         tutorias.dia1_hora1.data,
                         tutorias.dia1_hora2.data,
                         tutorias.dia2.data,
                         tutorias.dia2_hora1.data,
                         tutorias.dia2_hora2.data,
                         tutorias.dia3.data,
                         tutorias.dia3_hora1.data,
                         tutorias.dia3_hora2.data
                         )

        # creo el mail a enviar
        msg = Message('Tutoria', sender=app.config['MAIL_USERNAME'],
                      recipients=[tutorias.email.data])  # recipients es una lista!!

        msg.html = render_template('email_tutoria.html',
                                   motivo=tutorias.motivo.data,
                                   nombre=tutorias.nombre.data,
                                   apellido=tutorias.apellido.data,
                                   email=tutorias.email.data,
                                   telefono=tutorias.telefono.data,
                                   dni=tutorias.dni.data,
                                   departamento=tutorias.departamento.data,
                                   carrera=request.form['carrera'],
                                   rol=tutorias.rol.data,
                                   cant_personas=tutorias.grupal.data,
                                   dia1=tutorias.dia1.data,
                                   dia1_hora1=tutorias.dia1_hora1.data,
                                   dia1_hora2=tutorias.dia1_hora2.data,
                                   dia2=tutorias.dia2.data,
                                   dia2_hora1=tutorias.dia2_hora1.data,
                                   dia2_hora2=tutorias.dia2_hora2.data,
                                   dia3=tutorias.dia3.data,
                                   dia3_hora1=tutorias.dia3_hora1.data,
                                   dia3_hora2=tutorias.dia3_hora2.data,
                                   )
        # archivo pdf adjunto
        with app.open_resource("tutoria.pdf") as pdf:
            msg.attach("tutoria.pdf", "documento/pdf", pdf.read())

        # envio el mail
        # mail.send(msg)

        # elimino el pdf despues de enviado el mail
        # os.remove('tutoria.pdf')

    return render_template('Capacitacion/tutorias.html', titulo="Tutorias", form=tutorias)


@app.route('/capacitacion/microtalleres', methods=['GET', 'POST'])
def microtalleres():
    microtalleres = forms.Microtalleres(request.form)
    microtaller_abm = MicrotallerABM()
    microtalleres_docentes = microtaller_abm.listarDocentes()
    microtalleres_estudiantes = microtaller_abm.listarEstudiantes()

    if request.method == 'POST' and microtalleres.validate():

        persona_abm = PersonaABM()
        print microtalleres.nombre.data
        print microtalleres.apellido.data
        print microtalleres.email.data
        print microtalleres.telefono.data
        print microtalleres.dni.data
        print microtalleres.departamento.data
        print request.form['carrera']
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
        crearPdf.microtaller(microtalleres.nombre.data,
                             microtalleres.apellido.data,
                             microtalleres.email.data,
                             microtalleres.telefono.data,
                             microtalleres.dni.data,
                             microtalleres.departamento.data,
                             request.form['carrera'],
                             microtalleres.motivo.data,
                             request.form['microtaller'])

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
                                   carrera=request.form['carrera'],
                                   motivo=microtalleres.motivo.data,
                                   microtaller=request.form['microtaller']
                                   )
        # archivo pdf adjunto
        with app.open_resource("microtaller.pdf") as pdf:
            msg.attach("microtaller.pdf", "documento/pdf", pdf.read())

        # envio el mail
        # mail.send(msg)

        # elimino el pdf despues de enviado el mail
        # os.remove('microtaller.pdf')

    return render_template('Capacitacion/microtalleres.html', titulo="Microtalleres", form=microtalleres,
                           microtalleres_docentes=microtalleres_docentes, microtalleres_estudiantes=microtalleres_estudiantes)


carrera_abm = CarreraABM()
carreras = carrera_abm.listarxdepartamento(1)
eleccion = [(c.getNombreCarrera()) for c in carreras]

carrera = {
    '1': eleccion,
    '2': ['No aplica'],
    '3': ['No aplica'],
    '4': ['No aplica'],
    '5': ['No aplica'],
    '6': ['No aplica'],
    '7': ['No aplica'],
    '8': ['No aplica'],
    '9': ['No aplica'],
    '10': ['No aplica'],
}


@app.route('/get_food/<departamento>')
def get_food(departamento):
    if departamento not in carrera:
        return jsonify([])
    else:
        return jsonify(carrera[departamento])


if __name__ == '__main__':
    csrf.init_app(app)
    mail.init_app(app)
    app.run(port=8000)  # ejecuta el server
