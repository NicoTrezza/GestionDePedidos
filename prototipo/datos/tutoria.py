#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tutoria(object):

    def __init__(self, dao):
        self.idTutoria = int(dao[0])
        self.motivo = u'{}'.format(dao[1])
        self.fecha1desde = u'{}'.format(dao[2])
        self.fecha1hasta = u'{}'.format(dao[3])
        self.fecha2desde = u'{}'.format(dao[4])
        self.fecha2hasta = u'{}'.format(dao[5])
        self.fecha3desde = u'{}'.format(dao[6])
        self.fecha3hasta = u'{}'.format(dao[7])
        self.personaTutoria = int(dao[8])
        self.departamento = int(dao[9])
        self.fechaactual = u'{}'.format(dao[10])

    def getIdTutoria (self):
        return self.idTutoria

    def setIdTutoria (self, idTutoria):
        self.idTutoria = idTutoria

    def getMotivo(self):
        return self.motivo

    def setMotivo(self, motivo):
        self.motivo = motivo

    def getFecha1desde(self):
        return self.fecha1hasta

    def setFecha1hasta(self, fecha1hasta):
        self.fecha1hasta = fecha1hasta

    def getFecha2desde(self):
        return self.fecha2hasta

    def setFecha2hasta(self, fecha2hasta):
        self.fecha2hasta = fecha2hasta

    def getFecha3desde(self):
        return self.fecha3hasta

    def setFecha3hasta(self, fecha3hasta):
        self.fecha3hasta = fecha3hasta

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getPersonaTutoria(self):
        return self.personaTutoria

    def setPersonaTutoria(self, personaTutoria):
        self.personaTutoria = personaTutoria

    def getFechaactual(self):
        return self.fechaactual

    def setFechaactual(self, fechaactual):
        self.fechaactual = fechaactual

    def __str__(self):
        return u'Id de la Tutoria: {}, motivo de la Tutoria: {}, usuario de la Tutoria: {}, usuario de la Tutoria: {}'.format(self.idTutoria, self.motivo, self.personaTutoria, self.departamento)