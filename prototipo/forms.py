#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms import Form
from wtforms import StringField, SelectField, TextAreaField, DateTimeField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from datetime import datetime
from negocio.departamentoABM import DepartamentoABM



class Login(Form):
    usuario = StringField('Usuario',
                          [validators.required()]
                          )
    contrasenia = PasswordField('Contrasenia',
                              [validators.required()]
                              )


class CrearAula(Form):
    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    carreras = ['carrera 1', 'carrera 2', 'carrera 3']
    roles = ['rol 1', 'rol 2', 'rol 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('Departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    carrera = SelectField('Carrera',
                          choices=[('1', carreras[0]), ('2', carreras[1]), ('3', carreras[2])])

    nombreaula = StringField('Nombre del aula',
                             [validators.required()]
                             )
    nombredirector = StringField('Nombre del director',
                                 [validators.required()]
                                 )
    emaildirector = EmailField('E-mail del director',
                               [validators.required(),
                                validators.email()]
                               )
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
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    rol = SelectField('rol', choices=[('1', roles[0]), ('2', roles[1]), ('3', roles[2])])
    descripcion = TextAreaField('Descripcion',
                                [validators.required()]
                                )


class ReutilizarAula(Form):
    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    carreras = ['carrera 1', 'carrera 2', 'carrera 3']
    roles = ['rol 1', 'rol 2', 'rol 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('Departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    carrera = SelectField('Carrera', choices=[('1', carreras[0]), ('2', carreras[1]), ('3', carreras[2])])
    nombreaula = StringField('Nombre del aula',
                             [validators.required()]
                             )
    direccionulr = StringField('Direccion del aula (ulr)',
                                [validators.required()]
                                )
    nombredirector = StringField('Nombre del director',
                                 [validators.required()]
                                 )
    emaildirector = EmailField('E-mail del director',
                               [validators.required(),
                                validators.email()]
                               )
    nombrenuevo = StringField('Nombre nuevo')
    otro = TextAreaField('Otro')


class EliminarAula(Form):
    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    carreras = ['carrera 1', 'carrera 2', 'carrera 3']
    roles = ['rol 1', 'rol 2', 'rol 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('Departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    carrera = SelectField('Carrera', choices=[('1', carreras[0]), ('2', carreras[1]), ('3', carreras[2])])
    nombreaula = StringField('Nombre del aula',
                             [validators.required()]
                             )
    direccionulr = StringField('Direccion del aula (ulr)',
                                [validators.required()]
                                )
    nombredirector = StringField('Nombre del director',
                                 [validators.required()]
                                 )
    emaildirector = EmailField('E-mail del director',
                               [validators.required(),
                                validators.email()]
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
    dni = StringField('DNI',
                      [validators.required()]
                      )
    fecha = DateTimeField('Fecha', format="%d/%m/%Y %H:%M:%S", default=datetime.today,
                          validators=[validators.DataRequired(message='formato incorrecto')]
                          )
    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    carreras = ['carrera 1', 'carrera 2', 'carrera 3']
    roles = ['rol 1', 'rol 2', 'rol 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('Departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    carrera = SelectField('Carrera', choices=[('1', carreras[0]), ('2', carreras[1]), ('3', carreras[2])])
    rol = SelectField('Rol', choices=[('1', roles[0]), ('2', roles[1]), ('3', roles[2])])


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
    dni = StringField('DNI',
                      [validators.required()]
                      )


    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    carreras = ['carrera 1', 'carrera 2', 'carrera 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('Departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    carrera = SelectField('Carrera', choices=[('1', carreras[0]), ('2', carreras[1]), ('3', carreras[2])])
    motivo = TextAreaField('Motivo',
                           [validators.required()]
                           )


class Matricular(Form):
    departamento_abm = DepartamentoABM()
    departamentos = departamento_abm.listar()
    eleccion = [(str(d.getIdDepartamento()), d.getNombreDepartamento()) for d in departamentos]

    foodkind = SelectField('Departamento', choices=eleccion)

    food = SelectField('Carrera', choices=[])

    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    carreras = ['carrera 1', 'carrera 2', 'carrera 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('Departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    carrera = SelectField('Carrera', choices=[('1', carreras[0]), ('2', carreras[1]), ('3', carreras[2])])
