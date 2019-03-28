from conexion import Conexion
from mysql.connector import Error

from datos.login import Login
from datos.persona import Persona


class LoginDao(Conexion):
        
    def __init__(self):
        super(LoginDao, self).__init__()  		

    def insertar(self, mail, contrasenia, permisos, estado):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into login (mail, contrasenia, permisos, estado) values (%s, %s, %s, %s)'
            val = (mail, contrasenia, permisos, estado)
        
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificar(self, idLogin, mail, contrasenia, permisos):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update login set mail = %s, contrasenia = %s, permisos = %s where idLogin = %s'
            val = (mail, contrasenia, permisos, idLogin)
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def confirmarcuenta(self, idLogin):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'update login set estado = 1 where idLogin = %s'
            val = (idLogin, )

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e
    
    def eliminar(self, idLogin):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'delete from login where idLogin = %s'
            val = (idLogin, )
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
            
    def traer(self, idLogin):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from login where idLogin = %s'
            val = (idLogin, )
            
            cursor.execute(sql, val)
            
            objeto = cursor.fetchone()
            
            self.desconectar()
        except Error as e:
            print e
            
        return Login(objeto)

    def traerXMail(self, mail):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'select * from login where mail = %s'
            val = (mail,)

            cursor.execute(sql, val)

            objeto = cursor.fetchone()

            self.desconectar()
        except Error as e:
            print e

        return Login(objeto)

    def listar(self):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from login'
    
            cursor.execute(sql)
            
            lista = cursor.fetchall()
            
            self.desconectar()
        except Error as e:
            print e
                    
        lis = []
        
        for objeto in lista:
            ob = Login(objeto)
            lis.append(ob)
            
        return lis

    def listarSolicitados(self):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'SELECT * FROM login inner join persona where persona.login = login.idLogin and login.estado = 0'

            #sql = 'select * from login where estado = 0'

            cursor.execute(sql)

            lista = cursor.fetchall()

            self.desconectar()
        except Error as e:
            print e

        lis = []

        for objeto in lista:
            l = Login(objeto[:5])
            p = Persona(objeto[5:])

            lis.append((l, p))

        return lis