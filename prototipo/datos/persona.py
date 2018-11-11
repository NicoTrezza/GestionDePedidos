#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Persona(object):

	def __init__(self, dao):
		self.idPersona = int(dao[0])
		self.nombre = u'{}'.format(dao[1])
		self.apellido = u'{}'.format(dao[2])
		self.dni = int(dao[3])
		try:
			self.mailPersona = u'{}'.format(dao[4])
		except:
			self.mailPersona = None
		self.tipoPersona = int(dao[5])
		try:
			self.login = int(dao[6])
		except:
			self.login = None

	def getIdPersona(self):
		return self.idPersona

	def setIdPersona(self, idPersona):
		self.idPersona = idPersona

	def getNombre(self):
		return self.nombre

	def setNombre(self, nombre):
		self.nombre = nombre

	def getApellido(self):
		return self.apellido

	def setApellido(self, apellido):
		self.apellido = apellido

	def getDni(self):
		return self.dni

	def setDni(self, dni):
		self.dni = dni

	def getMail(self):
		return self.mailPersona

	def setMail(self, mailPersona):
		self.mailPersona = mailPersona

	def getTipoPersona(self):
		return self.tipoPersona

	def setTipoPersona(self, tipoPersona):
		self.tipoPersona = tipoPersona

	def getLogin(self):
		return self.login

	def setLogin(self, login):
		self.login = login
		
	def __str__(self):
		return u'Id de persona: {}, nombre: {}, apellido: {}, dni: {}, tipo de Persona: {}, login: {}'.format(self.idPersona, self.nombre, self.apellido, self.dni, self.tipoPersona, self.login)

