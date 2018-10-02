from conexion import Conexion
from mysql.connector import Error

from datos.aula import Aula

class AulaDao(Conexion):
        
    def __init__(self):
        pass		

    def insertar(self, dependencia, nombreDelAula, nombreDelProfesor, emailDelProfesor):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into aula (dependencia, nombreDelAula, nombreDelProfesor, emailDelProfesor) values (%s, %s, %s, %s)'
            val = (dependencia, nombreDelAula, nombreDelProfesor, emailDelProfesor)
    
            cursor.execute(sql, val)
            self.conexion.commit()
    
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idAula, dependencia, nombreDelAula, nombreDelProfesor, emailDelProfesor):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update aula set dependencia = %s, nombreDelAula = %s, nombreDelProfesor = %s, emailDelProfesor = %s where idAula = %s'
            val = (dependencia, nombreDelAula, nombreDelProfesor, emailDelProfesor, idAula)
            
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
    
    def traerPorProfesor(self, nombreDelProfesor):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from aula where nombreDelProfesor = %s'
            val = (nombreDelProfesor, )
            
            cursor.execute(sql, val)
            
            lista = cursor.fetchall()
            
            self.desconectar()
        except Error as e:
            print e
                    
        lis = []
        
        for objeto in lista:
            ob = Aula(objeto)
            lis.append(ob)
            
        return lis

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