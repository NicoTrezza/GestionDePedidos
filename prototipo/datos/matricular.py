class Matricular(object):

    def __init__(self, dao):
        self.idMatricular = int(dao[0])
        self.departamento = int(dao[1])
        self.fechaactual = u'{}'.format(dao[2])


    def getIdMatricular(self):
        return self.idMatricular

    def setIdMatricular(self, idMatricular):
        self.idMatricular = idMatricular

    def getDepartamento(self):
        return self.departamento

    def setFechaactual(self, fechaactual):
        self.fechaactual = fechaactual

    def getFechaactual(self):
        return self.fechaactual

    def __str__(self):
        return u'Id de matriculacion: {}, departamento: {}, fecha: {}'.format(self.idMatricular, self.departamento, self.fechaactual)