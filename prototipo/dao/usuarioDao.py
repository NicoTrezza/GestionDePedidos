from conexion import Conexion
from mysql.connector import Error

from datos.usuario import Usuario

class UsuarioDao(Conexion):
        
    def __init__(self):
        pass		

    def insertar(self, nombre, apellido, dni, email):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into usuario (nombre, apellido, dni, email) values (%s, %s, %s, %s)'
            val = (nombre, apellido, dni, email)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idUsuario, nombre, apellido, dni, email):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update usuario set nombre = %s, apellido = %s, dni = %s, email = %s where idUsuario = %s'
            val = (nombre, apellido, dni, email, idUsuario)
            
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
            val = (idUsuario, )
            
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
            val = (idUsuario, )
            
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