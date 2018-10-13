from conexion import Conexion
from mysql.connector import Error

from datos.tipoUsuario import TipoUsuario

class TipoUsuarioDao(Conexion):
        
    def __init__(self):
        super(TipoUsuarioDao, self).__init__()	

    def insertar(self, nombreTipo):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into tipoUsuario (nombreTipo) values (%s)'
            val = (nombreTipo)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idTipoUsuario, nombreTipo):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update tipoUsuario set nombreTipo = %s where idTipoUsuario = %s'
            val = (nombreTipo, idTipoUsuario)
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
    
    def eliminar(self, idTipoUsuario):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'delete from tipoUsuario where idTipoUsuario = %s'
            val = (idTipoUsuario, )
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
            
    def traer(self, idTipoUsuario):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from tipoUsuario where idTipoUsuario = %s'
            val = (idTipoUsuario, )
            
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
    
            sql = 'select * from tipoUsuario'
    
            cursor.execute(sql)
            
            lista = cursor.fetchall()
            
            self.desconectar()
        except Error as e:
            print e
                    
        lis = []
        
        for objeto in lista:
            ob = TipoUsuario(objeto)
            lis.append(ob)
            
        return lis