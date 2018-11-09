#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tutoria(object):

    def __init__(self, dao):
        self.idTutoria = int(dao[0])
        self.motivo = u'{}'.format(dao[2])
        self.personaTutoria = int(dao[3])
        self.departamento = int(dao[4])

    def getIdTutoria (self):
        return self.idTutoria

    def setIdTutoria (self, idTutoria):
        self.idTutoria = idTutoria

    def getMotivo(self):
        return self.motivo

    def setMotivo(self, motivo):
        self.motivo = motivo

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getPersonaTutoria(self):
        return self.personaTutoria

    def setPersonaTutoria(self, personaTutoria):
        self.personaTutoria = personaTutoria

    def __str__(self):
        return "Id de la Tutoria: {}, motivo de la Tutoria: {}, usuario de la Tutoria: {}, usuario de la Tutoria: {}".format(self.idTutoria, self.motivo, self.personaTutoria, self.departamento)