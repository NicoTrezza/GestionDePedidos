from conexion import Conexion
from mysql.connector import Error

from datos.tutoria import Tutoria

class TutoriaDao(Conexion):
        
    def __init__(self):
        super(TutoriaDao, self).__init__()  		

    def insertar(self, motivo, fecha, personaTutoria):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into tutoria (motivo, fecha, personaTutoria) values (%s, %s, %s)'
            val = (motivo, fecha, personaTutoria)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idTutoria, motivo, fecha, personaTutoria):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update tutoria set motivo = %s, fecha = %s, personaTutoria = %s where idTutoria = %s'
            val = (motivo, fecha, personaTutoria, idTutoria)
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
    
    def eliminar(self, idTutoria):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'delete from tutoria where idTutoria = %s'
            val = (idTutoria, )
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
            
    def traer(self, idTutoria):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from tutoria where idTutoria = %s'
            val = (idTutoria, )
            
            cursor.execute(sql, val)
            
            objeto = cursor.fetchone()
            
            self.desconectar()
        except Error as e:
            print e
            
        return Tutoria(objeto)

    def listar(self):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from tutoria'
    
            cursor.execute(sql)
            
            lista = cursor.fetchall()
            
            self.desconectar()
        except Error as e:
            print e
                    
        lis = []
        
        for objeto in lista:
            ob = Tutoria(objeto)
            lis.append(ob)
            
        return lis