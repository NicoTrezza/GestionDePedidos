from conexion import Conexion
from mysql.connector import Error

from datos.carrera import Carrera

class CarreraDao(Conexion):
        
    def __init__(self):
        super(CarreraDao, self).__init__()  		

    def insertar(self, nombreCarrera, departamento):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into carrera (nombreCarrera, departamento) values (%s, %s)'
            val = (nombreCarrera, departamento)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idCarrera, nombreCarrera, departamento):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update carrera set nombreCarrera = %s, departamento = %s where idCarrera = %s'
            val = (nombreCarrera, departamento, idCarrera)
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
    
    def eliminar(self, idCarrera):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'delete from carrera where idCarrera = %s'
            val = (idCarrera, )
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
            
    def traer(self, idCarrera):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from carrera where idCarrera = %s'
            val = (idCarrera, )
            
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
    
            sql = 'select * from carrera'
    
            cursor.execute(sql)
            
            lista = cursor.fetchall()
            
            self.desconectar()
        except Error as e:
            print e
                    
        lis = []
        
        for objeto in lista:
            ob = Carrera(objeto)
            lis.append(ob)
            
        return lis