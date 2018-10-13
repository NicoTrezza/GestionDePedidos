from conexion import Conexion
from mysql.connector import Error

from datos.departamento import Departamento

class DepartamentoDao(Conexion):
        
    def __init__(self):
        super(DepartamentoDao, self).__init__()  		

    def insertar(self, nombreDepartamento):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into departamento (nombreDepartamento) values (%s)'
            val = (nombreDepartamento)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idDepartamento, nombreDepartamento):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update departamento set nombreDepartamento = %s where idDepartamento = %s'
            val = (nombreDepartamento, idDepartamento)
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
    
    def eliminar(self, idDepartamento):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'delete from departamento where idDepartamento = %s'
            val = (idDepartamento, )
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
            
    def traer(self, idDepartamento):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from departamento where idDepartamento = %s'
            val = (idDepartamento, )
            
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
    
            sql = 'select * from departamento'
    
            cursor.execute(sql)
            
            lista = cursor.fetchall()
            
            self.desconectar()
        except Error as e:
            print e
                    
        lis = []
        
        for objeto in lista:
            ob = Departamento(objeto)
            lis.append(ob)
            
        return lis