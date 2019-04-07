from conexion import Conexion
from mysql.connector import Error

from datos.matricular import Matricular


class MatricularDao(Conexion):

    def __init__(self):
        super(MatricularDao, self).__init__()

    def insertar(self, departamento, fechaactual):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'insert into matricular (Departamento_idDepartamento, fechaactual) values (%s, %s)'
            val = (departamento, fechaactual)

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e

    def insertarpersona(self, idMatricular, idPersona):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'insert into Matricular_has_Persona (Matricular_idMatricular, Persona_idPersona) values (%s, %s)'
            val = (idMatricular, idPersona)

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idMatricular, departamento, fechaactual):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'update matricular set departamento = %s, fechaactual = %s where idMatricular = %s'
            val = (departamento, fechaactual, idMatricular)

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e

    def eliminar(self, idMatricular):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'delete from matricular where idMatricular = %s'
            val = (idMatricular,)

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e

    def traer(self, idMatricular):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'select * from matricular where idMatricular = %s'
            val = (idMatricular,)

            cursor.execute(sql, val)

            objeto = cursor.fetchone()

            self.desconectar()
        except Error as e:
            print e

        return Matricular(objeto)

    def listar(self):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'select * from matricular'

            cursor.execute(sql)

            lista = cursor.fetchall()

            self.desconectar()
        except Error as e:
            print e

        lis = []

        for objeto in lista:
            ob = Matricular(objeto)
            lis.append(ob)

        return lis
