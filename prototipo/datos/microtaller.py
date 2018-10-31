class MicroTaller(object):

    def __init__(self, dao):
        self.idMicrotaller = int(dao[0])
        self.nombreMicrotaller = str(dao[1])
        self.motivoMicrotaller = str(dao[2])

    """def __init__(self, idMicrotaller, nombreMicrotaller, motivoMicrotaller):
        self.idMicrotaller = idMicrotaller
        self.nombreMicrotaller = nombreMicrotaller
        self.motivoMicrotaller = motivoMicrotaller"""

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

    def __str__(self):
        return "Id del microtaller: {}, nombre del microtaller: {}, motivo del microtaller: {}".format(self.idMicrotaller, self.nombreMicrotaller, self.motivoMicrotaller)