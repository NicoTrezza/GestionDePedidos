class Departamento(object):

    def __init__(self, dao):
        self.idDepartamento = int(dao[0])
        self.nombreDepartamento = str(dao[1])

    def getIdDepartamento(self):
        return self.idDepartamento

    def setIdDepartamento(self, idDepartamento):
        self.idDepartamento = idDepartamento

    def getNombreDepartamento(self):
        return self.nombreDepartamento

    def setNombreDepartamento(self, nombreDepartamento):
        self.nombreDepartamento = nombreDepartamento

    def __str__(self):
        return "Id del Departamento: {}, nombre: {}".format(self.idDepartamento, self.nombreDepartamento)