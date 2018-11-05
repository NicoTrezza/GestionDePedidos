#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tutoria(object):

    def __init__(self, dao):
        self.idTutoria = int(dao[0])
        self.motivo = u'{}'.format(dao[2])
        self.fecha = str(dao[3])
        self.personaTutoria = int(dao[4])

    """def __init__(self, idTutoria, motivo, fecha, personaTutoria):
        self.idTutoria = idTutoria
        self.motivo = motivo
        self.fecha = fecha
        self.personaTutoria = personaTutoria"""

    def getIdTutoria (self):
        return self.idTutoria

    def setIdTutoria (self, idTutoria):
        self.idTutoria = idTutoria

    def getMotivo(self):
        return self.motivo

    def setMotivo(self, motivo):
        self.motivo = motivo

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def getPersonaTutoria(self):
        return self.personaTutoria

    def setPersonaTutoria(self, personaTutoria):
        self.personaTutoria = personaTutoria

    def __str__(self):
        return "Id de la Tutoria: {}, motivo de la Tutoria: {}, fecha de inicio de la Tutoria: {}, usuario de la Tutoria: {}".format(self.idTutoria, self.motivo, self.fecha, self.personaTutoria)