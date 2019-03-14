from conexion import Conexion
from mysql.connector import Error

from datos.tutoria import Tutoria

class TutoriaDao(Conexion):
        
    def __init__(self):
        super(TutoriaDao, self).__init__()  		

    def insertar(self, motivo, fecha1desde, fecha1hasta, fecha2desde, fecha2hasta, fecha3desde, fecha3hasta, personaTutoria, departamento, fechaactual):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into tutoria (motivo, fecha1desde, fecha1hasta, fecha2desde, fecha2hasta, fecha3desde, fecha3hasta, personaTutoria, Departamento_idDepartamento, fechaactual) values (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)'
            val = (motivo, fecha1desde, fecha1hasta, fecha2desde, fecha2hasta, fecha3desde, fecha3hasta, personaTutoria, departamento, fechaactual)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idTutoria, motivo, personaTutoria, departamento):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update tutoria set motivo = %s, personaTutoria = %s, Departamento_idDepartamento = %s where idTutoria = %s'
            val = (motivo, personaTutoria, departamento, idTutoria)
            
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