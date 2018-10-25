from conexion import Conexion
from mysql.connector import Error

from datos.tipoPersona import tipoPersona

class TipoPersonaDao(Conexion):
        
    def __init__(self):
        super(TipoPersonaDao, self).__init__()	

    def insertar(self, rol):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into tipoPersona (rol) values (%s)'
            val = (rol)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idTipoPersona, rol):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update tipoPersona set rol = %s where idTipoPersona = %s'
            val = (rol, idTipoPersona)
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
    
    def eliminar(self, idTipoPersona):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'delete from tipoPersona where idTipoPersona = %s'
            val = (idTipoPersona, )
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
            
    def traer(self, idTipoPersona):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from tipoPersona where idTipoPersona = %s'
            val = (idTipoPersona, )
            
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
    
            sql = 'select * from tipoPersona'
    
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