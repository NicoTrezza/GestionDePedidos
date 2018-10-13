class Aula(object):

    def __init__(self, dao):
        self.idAula = int(dao[0])
        self.nombreAula = str(dao[1])
        self.departamentoAula = int(dao[2])

    """def __init__(self, idAula, nombreAula, departamentoAula):
        self.idAula = idAula
        self.nombreAula = nombreAula
        self.departamentoAula = departamentoAula"""

    def getIdAula(self):
        return self.idAula

    def setIdAula(self, idAula):
        self.idAula = idAula

    def getNombreAula(self):
        return self.nombreAula

    def setNombreAula(self, nombreAula):
        self.nombreAula = nombreAula

    def getDepartamentoAula(self):
        return self.departamentoAula

    def setDepartamentoAula(self, departamentoAula):
        self.departamentoAula = departamentoAula

    def __str__(self):
        return "Id del aula: {}, nombre del Aula: {}, departamento del Aula: {}".format(self.idAula, self.nombreAula, self.departamentoAula)
