#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conexion import Conexion
from mysql.connector import Error

from datos.persona import Persona

class PersonaDao(Conexion):
        
    def __init__(self):
        super(PersonaDao, self).__init__()	

    def insertar(self, nombre, apellido, dni, emailPersona, tipoPersona, login):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            
            sql = 'insert into persona (nombre, apellido, dni, emailPersona, tipoPersona, login) values (%s, %s, %s, %s, %s, %s)'
            val = (nombre, apellido, dni, emailPersona, tipoPersona, login)
        
            cursor.execute(sql, val)
            id = cursor.lastrowid
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
        return id

    def modificar(self, idPersona, nombre, apellido, dni, emailPersona, tipoPersona, login):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'update persona set nombre = %s, apellido = %s, dni = %s, emailPersona = %s, tipoPersona = %s, login = %s where idPersona = %s'
            val = (nombre, apellido, dni, emailPersona, tipoPersona, login, idPersona)
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e

    def modificarLogin(self, idPersona, login):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'update persona set login = %s where idPersona = %s'
            val = (login, idPersona)

            cursor.execute(sql, val)
            self.conexion.commit()

            self.desconectar()
        except Error as e:
            print e

    def eliminar(self, idPersona):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
        
            sql = 'delete from persona where idPersona = %s'
            val = (idPersona, )
            
            cursor.execute(sql, val)
            self.conexion.commit()
        
            self.desconectar()
        except Error as e:
            print e
            
    def traer(self, idPersona):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from persona where idPersona = %s'
            val = (idPersona, )
            
            cursor.execute(sql, val)
            
            objeto = cursor.fetchone()
            
            self.desconectar()
        except Error as e:
            print e
            
        return Persona(objeto)

    def traerXDni(self, dni):
        try:
            self.conectar()
            cursor = self.conexion.cursor()

            sql = 'select * from persona where dni = %s'
            val = (dni,)

            cursor.execute(sql, val)

            objeto = cursor.fetchone()

            self.desconectar()
        except Error as e:
            print e

        return Persona(objeto)

    def listar(self):
        try:
            self.conectar()
            cursor = self.conexion.cursor()
    
            sql = 'select * from persona'
    
            cursor.execute(sql)
            
            lista = cursor.fetchall()
            
            self.desconectar()
        except Error as e:
            print e
                    
        lis = []
        
        for objeto in lista:
            ob = Persona(objeto)
            lis.append(ob)
            
        return lis