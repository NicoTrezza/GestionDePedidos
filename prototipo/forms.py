from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms.fields.html5 import EmailField


class CrearAula(Form):
    dependencia = StringField('dependencia')
    nombreAula = StringField('nombreAula')
    nombreprofesor = StringField('nombreprofesor')
    email = EmailField('email')
    nombre = StringField('nombre')
    apellido = StringField('apellido')
    dni = StringField('dni')
