#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms import Form
from wtforms import StringField, SelectField, TextAreaField, DateTimeField, PasswordField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms import validators
from datetime import datetime
from negocio.departamentoABM import DepartamentoABM
from negocio.tipoPersonaABM import TipoPersonaABM


class Login(Form):
    usuario = StringField('Usuario',
                          [validators.required()]
                          )
    contrasenia = PasswordField(u'Contraseña',
                              [validators.required()]
                              )


class Solicitudcuenta(Form):

    nombredocente = StringField('Nombre',
                                [validators.required()]
                                )
    apellidodocente = StringField('Apellido',
                                  [validators.required()]
                                  )
    dni = StringField('DNI',
                      [validators.required()]
                      )
    emailprofesor = EmailField('E-mail',
                               [validators.required(),
                                validators.email()]
                               )
    tipo_persona_abm = TipoPersonaABM()
    listaroles = tipo_persona_abm.listar()
    lista_eleccion_roles = [(str(d.getIdTipoPersona()), d.getRol()) for d in listaroles]
    rol = SelectField('rol', choices=lista_eleccion_roles)

    usuario = StringField('Usuario',
                      [validators.required()]
                      )
    contrasenia = StringField(u'Contraseña',
                      [validators.required()]
                      )


class Altausuarios(Form):

    nombredocente = StringField('Nombre',
                                [validators.required()]
                                )
    apellidodocente = StringField('Apellido',
                                  [validators.required()]
                                  )
    dni = StringField('DNI',
                      [validators.required()]
                      )
    emailprofesor = EmailField('E-mail',
                               [validators.required(),
                                validators.email()]
                               )
    tipo_persona_abm = TipoPersonaABM()
    listaroles = tipo_persona_abm.listar()
    lista_eleccion_roles = [(str(d.getIdTipoPersona()), d.getRol()) for d in listaroles]
    rol = SelectField('rol', choices=lista_eleccion_roles)

    usuario = StringField('Usuario',
                      [validators.required()]
                      )
    contrasenia = StringField('Contrasenia',
                      [validators.required()]
                      )

    permisos = SelectField('Permisos', choices=[('1', 'Administrador'), ('2', 'Permisos de estadisticas'), ('3', 'Usuario comun')])


class CrearAula(Form):

    departamento_abm = DepartamentoABM()
    departamentos = departamento_abm.listar()
    eleccion = [(str(d.getIdDepartamento()), d.getNombreDepartamento()) for d in departamentos]

    departamento = SelectField('Departamento', choices=eleccion, default=2)

    nombreaula = StringField('Nombre del aula',
                             [validators.required()]
                             )
    """
    nombredocente = StringField('Nombre del docente',
                                [validators.required()]
                                )
    apellidodocente = StringField('Apellido del docente',
                                  [validators.required()]
                                  )
    dni = StringField('DNI',
                      [validators.required()]
                      )
    emailprofesor = EmailField('E-mail del profesor',
                               [validators.required(),
                                validators.email()]
                               )
    tipo_persona_abm = TipoPersonaABM()
    listaroles = tipo_persona_abm.listar()
    lista_eleccion_roles = [(str(d.getIdTipoPersona()), d.getRol()) for d in listaroles]
    rol = SelectField('rol', choices=lista_eleccion_roles)
    """
    descripcion = TextAreaField('Descripcion',
                                [validators.required()]
                                )


class ReutilizarAula(Form):

    departamento_abm = DepartamentoABM()
    departamentos = departamento_abm.listar()
    eleccion = [(str(d.getIdDepartamento()), d.getNombreDepartamento()) for d in departamentos]

    departamento = SelectField('Departamento', choices=eleccion, default=2)

    nombreaula = StringField('Nombre del aula',
                             [validators.required()]
                             )
    direccionulr = StringField('Direccion del aula (ulr)',
                                [validators.required()]
                                )
    nombrenuevo = StringField('Nombre nuevo')
    otro = TextAreaField('Otro')


class EliminarAula(Form):

    departamento_abm = DepartamentoABM()
    departamentos = departamento_abm.listar()
    eleccion = [(str(d.getIdDepartamento()), d.getNombreDepartamento()) for d in departamentos]

    departamento = SelectField('Departamento', choices=eleccion, default=2)

    nombreaula = StringField('Nombre del aula',
                             [validators.required()]
                             )
    direccionulr = StringField('Direccion del aula (ulr)',
                                [validators.required()]
                                )
    motivo = TextAreaField('Motivo',
                           [validators.required()]
                           )


class Tutorias(Form):
    motivo = TextAreaField('Motivo',
                           [validators.required()]
                           )
    nombre = StringField('Nombre',
                         [validators.required()]
                         )
    apellido = StringField('Apellido',
                           [validators.required()]
                           )
    email = EmailField('E-mail',
                       [validators.required(),
                        validators.email()]
                       )
    telefono = StringField('Telefono',
                           [validators.required()]
                           )
    dni = IntegerField('DNI',
                      [validators.required()]
                      )

    dia1 = StringField(u'Día',
                       [validators.required()]
                       )

    dia1_hora1 = StringField('Desde',
                             [validators.required()]
                                )
    dia1_hora2 = StringField('Hasta',
                               [validators.required()]
                               )
    dia2 = StringField(u'Día',
                      [validators.required()]
                      )
    dia2_hora1 = StringField('Desde',
                      [validators.required()]
                      )
    dia2_hora2 = StringField('Hasta',
                               [validators.required()]
                               )
    dia3 = StringField(u'Día',
                      [validators.required()]
                      )
    dia3_hora1 = StringField('Desde',
                      [validators.required()]
                      )
    dia3_hora2 = StringField('Hasta',
                          [validators.required()]
                          )

# fecha = DateTimeField('Fecha', format="%d/%m/%Y %H:%M:%S", default=datetime.today,
# validators=[validators.DataRequired(message='formato incorrecto')])


    departamento_abm = DepartamentoABM()
    departamentos = departamento_abm.listar()
    eleccion = [(str(d.getIdDepartamento()), d.getNombreDepartamento()) for d in departamentos]

    departamento = SelectField('Departamento', choices=eleccion, default=2)

    tipo_persona_abm = TipoPersonaABM()
    listaroles = tipo_persona_abm.listar()
    lista_eleccion_roles = [(str(d.getIdTipoPersona()), d.getRol()) for d in listaroles]
    rol = SelectField('rol', choices=lista_eleccion_roles)

    grupal = IntegerField('Cantidad de personas')


class Microtalleres(Form):
    nombre = StringField('Nombre',
                         [validators.required()]
                         )
    apellido = StringField('Apellido',
                           [validators.required()]
                           )
    email = EmailField('E-mail',
                       [validators.required(),
                        validators.email()]
                       )
    telefono = StringField('Telefono',
                           [validators.required()]
                           )
    dni = IntegerField('DNI',
                      [validators.required()]
                      )

    departamento_abm = DepartamentoABM()
    departamentos = departamento_abm.listar()
    eleccion = [(str(d.getIdDepartamento()), d.getNombreDepartamento()) for d in departamentos]

    departamento = SelectField('Departamento', choices=eleccion, default=2)

    motivo = TextAreaField('Motivo',
                           [validators.required()]
                           )


class Matricular(Form):
    departamento_abm = DepartamentoABM()
    departamentos = departamento_abm.listar()
    eleccion = [(str(d.getIdDepartamento()), d.getNombreDepartamento()) for d in departamentos]

    departamento = SelectField('Departamento', choices=eleccion, default=2)
    #carrera = SelectField(coerce=int)


class Usuario(Form):

    nombre = StringField('Nombre',
                                [validators.required()]
                                )
    apellido = StringField('Apellido',
                                  [validators.required()]
                                  )
    dni = StringField('DNI',
                      [validators.required()]
                      )
    email = EmailField('E-mail',
                               [validators.required(),
                                validators.email()]
                               )
