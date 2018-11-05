#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MicroTaller(object):

    def __init__(self, dao):
        self.idMicrotaller = int(dao[0])
        self.nombreMicrotaller = u'{}'.format(dao[1])
        try:
            self.motivoMicrotaller = u'{}'.format(dao[2])
        except:
            self.login = None
        self.tipo = int(dao[3])  # 1 para docentes, 2 para estudiantes

    def getIdMicrotaller(self):
        return self.idMicrotaller

    def setIdMicrotaller(self, idMicrotaller):
        self.idMicrotaller = idMicrotaller

    def getNombreMicrotaller(self):
        return self.nombreMicrotaller

    def setNombreMicrotaller(self, nombreMicrotaller):
        self.nombreMicrotaller = nombreMicrotaller

    def getMotivoMicrotaller(self):
        return self.motivoMicrotaller

    def setMotivoMicrotaller(self, motivoMicrotaller):
        self.motivoMicrotaller = motivoMicrotaller

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return "Id del microtaller: {}, nombre del microtaller: {}, motivo del microtaller: {}".format(self.idMicrotaller, self.nombreMicrotaller, self.motivoMicrotaller)