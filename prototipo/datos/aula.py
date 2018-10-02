class Aula(object):

    def __init__(self, dao):
        self.idAula = int(dao[0])
        self.dependencia = str(dao[1])
        self.nombreDelAula = str(dao[2])
        self.nombreDelProfesor = str(dao[3])
        self.emailDelProfesor = str(dao[4])

    """def __init__(self, idAula, dependencia, nombreDelAula, nombreDelProfesor, emailDelProfesor):
        self.idAula = idAula
        self.dependencia = dependencia
        self.nombreDelAula = nombreDelAula
        self.nombreDelProfesor = nombreDelProfesor
        self.emailDelProfesor = emailDelProfesor"""

    def getIdAula(self):
        return self.idAula

    def setIdAula(self, idAula):
        self.idAula = idAula

    def getDependencia(self):
        return self.dependencia

    def setDependencia(self, dependencia):
        self.dependencia = dependencia

    def getNombreDelAula(self):
        return self.nombreDelAula

    def setNombreDelAula(self, nombreDelAula):
        self.nombreDelAula = nombreDelAula

    def getNombreDelProfesor(self):
        return self.nombreDelProfesor

    def setNombreDelProfesor(self, nombreDelProfesor):
        self.nombreDelProfesor = nombreDelProfesor

    def getEmailDelProfesor(self):
        return self.emailDelProfesor

    def setEmailDelProfesor(self, emailDelProfesor):
        self.emailDelProfesor = emailDelProfesor

    def __str__(self):
        return "Id del aula: {}, dependencia: {}, nombre del aula: {}, nombre del profesor: {}, email del profesor: {}".format(self.idAula, self.dependencia, self.nombreDelAula, self.nombreDelProfesor, self.emailDelProfesor)
