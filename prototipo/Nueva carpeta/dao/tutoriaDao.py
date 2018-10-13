from conexion import Conexion
from mysql.connector import Error

from datos.tutoria import Tutoria

class TutoriaDao(Conexion):
        
    def __init__(self):
        super(TutoriaDao, self).__init__()  		

    def insertar(self, nombreTutoria, motivo, fechaInicio, usuarioTutoria):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into tutoria (nombreTutoria, motivo, fechaInicio, usuarioTutoria) values (%s, %s, %s, %s)'
            val = (nombreTutoria, motivo, fechaInicio, usuarioTutoria)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idTutoria, nombreTutoria, motivo, fechaInicio, usuarioTutoria):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update tutoria set nombreTutoria = %s, motivo = %s, fechaInicio = %s, usuarioTutoria = %s where idTutoria = %s'
            val = (nombreTutoria, motivo, fechaInicio, usuarioTutoria, idTutoria)
            
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
            
        return Usuario(objeto)

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