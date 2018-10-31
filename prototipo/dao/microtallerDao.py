from conexion import Conexion
from mysql.connector import Error

from datos.microtaller import Microtaller

class MicrotallerDao(Conexion):
        
    def __init__(self):
        super(MicrotallerDao, self).__init__()  		

    def insertar(self, nombreMicrotaller, motivoMicrotaller):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into microtaller (nombreMicrotaller, motivoMicrotaller values (%s, %s, %s)'
            val = (nombreMicrotaller, motivoMicrotaller)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idMicrotaller, nombreMicrotaller, motivoMicrotaller):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update microtaller set nombreMicrotaller = %s, motivoMicrotaller = %s where idMicrotaller = %s'
            val = (nombreMicrotaller, motivoMicrotaller, idMicrotaller)
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
    
    def eliminar(self, idMicrotaller):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'delete from microtaller where idMicrotaller = %s'
            val = (idMicrotaller, )
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
            
    def traer(self, idMicrotaller):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from microtaller where idMicrotaller = %s'
            val = (idMicrotaller, )
            
            cursor.execute(sql, val)
            
            objeto = cursor.fetchone()
            
            self.desconectar()
        except Error as e:
            print e
            
        return Microtaller(objeto)

    def listar(self):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from microtaller'
    
            cursor.execute(sql)
            
            lista = cursor.fetchall()
            
            self.desconectar()
        except Error as e:
            print e
                    
        lis = []
        
        for objeto in lista:
            ob = Microtaller(objeto)
            lis.append(ob)
            
        return lis