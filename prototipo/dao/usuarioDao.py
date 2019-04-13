from conexion import Conexion
from mysql.connector import Error

from datos.usuario import Usuario


class UsuarioDao(Conexion):

    def __init__(self):
        super(UsuarioDao, self).__init__()

    def insertar(self, fechaactual, persona):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'insert into usuario (fechaactual, Persona_idPersona) values (%s, %s)'
            val = (fechaactual, persona)

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idUsuario, fechaactual, persona):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'update usuario set fechaactual = %s, Persona_idPersona = %s where idUsuario = %s'
            val = (fechaactual, persona, idUsuario)

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e

    def eliminar(self, idUsuario):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'delete from usuario where idUsuario = %s'
            val = (idUsuario,)

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e

    def traer(self, idUsuario):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'select * from usuario where idUsuario = %s'
            val = (idUsuario,)

            cursor.execute(sql, val)

            objeto = cursor.fetchone()

            self.desconectar()
        except Error as e:
            print e

        return Usuario(objeto)

    def listar(self):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'select * from usuario'

            cursor.execute(sql)

            lista = cursor.fetchall()

            self.desconectar()
        except Error as e:
            print e

        lis = []

        for objeto in lista:
            ob = Usuario(objeto)
            lis.append(ob)

        return lis
