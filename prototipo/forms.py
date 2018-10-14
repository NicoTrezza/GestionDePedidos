from wtforms import Form
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.fields.html5 import EmailField


class CrearAula(Form):
    departamentos = ['departamento 1', 'departamento 2', 'departamento 3']
    roles = ['rol 1', 'rol 2', 'rol 3']
    #cuando haya una lista de una base de datos usar este metodo
    #eleccion = [(str(d.id), d.nombre) for d in departamentos]
    #rol = SelectField('departamento', choices=eleccion)
    departamento = SelectField('departamento', choices=[('1', departamentos[0]), ('2', departamentos[1]), ('3', departamentos[2])])
    dependencia = StringField('dependencia')
    nombreAula = StringField('nombreAula')
    nombreprofesor = StringField('nombreprofesor')
    email = EmailField('email')
    nombre = StringField('nombre')
    apellido = StringField('apellido')
    dni = StringField('dni')
    #cuando haya una lista de una base de datos usar este metodo
    #eleccion = [(str(r.id), r.nombre) for r in roles]
    #rol = SelectField('rol', choices=eleccion)
    rol = SelectField('rol', choices=[('1', roles[0]), ('2', roles[1]), ('3', roles[2])])
    descripcion = TextAreaField('descripcion')
