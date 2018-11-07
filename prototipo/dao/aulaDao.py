from conexion import Conexion
from mysql.connector import Error

from datos.aula import Aula

class AulaDao(Conexion):
        
    def __init__(self):
        super(AulaDao, self).__init__()  	

    def insertar(self, nombreAula, descripcion, iddepartamento):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into aula (nombreAula, descripcion, Departamento_idDepartamento) values (%s, %s, %s)'
            val = (nombreAula, descripcion, iddepartamento)
    
            cursor.execute(sql, val)
            self.conexion.commit()
    
            self.desconectar()
        except Error as e:
            print e

    def insertarpersona(self, idpersona, idaula):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'insert into personaaula (Persona_idPersona, Aula_idAula) values (%s, %s)'
            val = (idpersona, idaula)

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idAula, nombreAula, descripcion, carreraAula):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update aula set nombreAula = %s, descripcion = %s, carreraAula = %s where idAula = %s'
            val = (nombreAula, descripcion, carreraAula, idAula)
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
    
    def eliminar(self, idAula):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'delete from aula where idAula = %s'
            val = (idAula, )
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
            
    def traer(self, idAula):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from aula where idAula = %s'
            val = (idAula, )
            
            cursor.execute(sql, val)
            
            objeto = cursor.fetchone()
            
            self.desconectar()
        except Error as e:
            print e
            
        return Aula(objeto)

    def traerXNombre(self, nombreAula):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'select * from aula where nombreAula = %s'
            val = (nombreAula,)

            cursor.execute(sql, val)

            objeto = cursor.fetchone()

            self.desconectar()
        except Error as e:
            print e

        return Aula(objeto)

    def listar(self):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from aula'
    
            cursor.execute(sql)
            
            lista = cursor.fetchall()
            
            self.desconectar()
        except Error as e:
            print e
                    
        lis = []
        
        for objeto in lista:
            ob = Aula(objeto)
            lis.append(ob)
            
        return lis