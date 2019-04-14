from conexion import Conexion
from mysql.connector import Error

from datos.matricular import Matricular
from datos.persona import Persona
from datos.departamento import Departamento


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
            id = cursor.lastrowid
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e
        return id

    def insertarpersona(self, idMatricular, idPersona):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'insert into matricular_has_persona (Matricular_idMatricular, Persona_idPersona) values (%s, %s)'
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

    def listarMatricular(self):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'select * from matricular_has_persona inner join matricular inner join persona inner join departamento where Matricular_idMatricular = idMatricular and Persona_idPersona = idPersona and Departamento_idDepartamento = idDepartamento'

            cursor.execute(sql)

            lista = cursor.fetchall()

            self.desconectar()
        except Error as e:
            print e

        lis = []

        for objeto in lista:
            m = Matricular(objeto[2:5])
            p = Persona(objeto[5:12])
            d = Departamento(objeto[12:])

            lis.append((m, p, d))

        return lis