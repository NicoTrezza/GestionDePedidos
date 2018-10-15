from wtforms import Form
from wtforms import StringField, IntegerField, SelectField, TextAreaField, DateTimeField
from wtforms.fields.html5 import EmailField, DateField
from wtforms import validators
from datetime import datetime

class CrearAula(Form):
    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    roles = ['rol 1', 'rol 2', 'rol 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    dependencia = StringField('dependencia',
                              [validators.length(min=5, max=25,
                                                 message='Departamento debe tener entre 5 y 25 caracteres.'),
                               validators.required()]
                              )
    nombreAula = StringField('nombreAula',
                             [validators.required()]
                             )
    nombreprofesor = StringField('nombreprofesor',
                                 [validators.required()]
                                 )
    email = EmailField('email',
                       [validators.required(),
                        validators.email()]
                       )
    nombre = StringField('nombre',
                         [validators.required()]
                         )
    apellido = StringField('apellido',
                           [validators.required()]
                           )
    dni = StringField('dni',
                      [validators.required()]
                      )
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    rol = SelectField('rol', choices=[('1', roles[0]), ('2', roles[1]), ('3', roles[2])])
    descripcion = TextAreaField('descripcion',
                                [validators.required()]
                                )


class ReutilizarAula(Form):
    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    carreras = ['carrera 1', 'carrera 2', 'carrera 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    carrera = SelectField('carrera', choices=[('1', carreras[0]), ('2', carreras[1]), ('3', carreras[2])])
    nombre = StringField('nombre',
                         [validators.required()]
                         )

    director = StringField('director',
                           [validators.length(min=5, max=25,
                                              message='director debe tener entre 5 y 25 caracteres.'),
                            validators.required()]
                           )


class EliminarAula(Form):
    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    carreras = ['carrera 1', 'carrera 2', 'carrera 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    carrera = SelectField('carrera', choices=[('1', carreras[0]), ('2', carreras[1]), ('3', carreras[2])])
    nombre = StringField('nombre',
                         [validators.required()]
                         )

    director = StringField('director',
                           [validators.length(min=5, max=25,
                                              message='director debe tener entre 5 y 25 caracteres.'),
                            validators.required()]
                           )
    motivo = TextAreaField('motivo',
                           [validators.required()]
                           )

class Tutorias(Form):
    motivo = TextAreaField('motivo',
                           [validators.required()]
                           )
    fecha = DateTimeField('fecha', format="%d/%m/%Y %H:%M:%S", default=datetime.today,
        validators=[validators.DataRequired(message='formato incorrecto')]
    )
    nombre = StringField('nombre',
                         [validators.required()]
                         )
    apellido = StringField('apellido',
                           [validators.required()]
                           )
    dni = StringField('dni',
                      [validators.required()]
                      )
    email = EmailField('email',
                       [validators.required(),
                        validators.email()]
                       )

class Microtalleres(Form):
    microtalleres = StringField('microtalleres',
                           [validators.required()]
                           )
    nombre = StringField('nombre',
                         [validators.required()]
                         )
    apellido = StringField('apellido',
                           [validators.required()]
                           )
    dni = StringField('dni',
                      [validators.required()]
                      )
    email = EmailField('email',
                       [validators.required(),
                        validators.email()]
                       )

class Matricular(Form):
    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    carreras = ['carrera 1', 'carrera 2', 'carrera 3']
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(d.id), d.nombre) for d in departamentos]
    # rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('departamento',
                               choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    # cuando haya una lista de una base de datos usar este metodo
    # eleccion = [(str(r.id), r.nombre) for r in roles]
    # rol = SelectField('rol', choices=eleccion)
    carrera = SelectField('carrera', choices=[('1', carreras[0]), ('2', carreras[1]), ('3', carreras[2])])