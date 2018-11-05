#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dao.personaDao import PersonaDao

class PersonaABM(object):

    def __init__(self):
        self.dao = PersonaDao()
        
    def insertar(self, nombre, apellido, dni, emailPersona, tipoPersona, login):
        self.dao.insertar(nombre, apellido, dni, emailPersona, tipoPersona, login)
        
    def modificar(self, u):
        self.dao.modificar(u.getIdPersona(), u.getNombre(), u.getApellido(), u.getDni(), u.getEmailPersona, u.getTipoPersona(), u.getCarrera(), u.getLogin())
   
    def eliminar(self, idPersona):
        self.dao.eliminar(idPersona)
        
    def traer(self, idPersona):
        return self.dao.traer(idPersona)

    def traerXDni(self, dni):
        return self.dao.traerXDni(dni)
        
    def listar(self):
        return self.dao.listar()