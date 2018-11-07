class Carrera(object):

    def __init__(self, dao):
        self.idCarrera = int(dao[0])
        self.nombreCarrera = u'{}'.format(dao[1])
        self.departamento = int(dao[2])

    def getIdCarreraa(self):
        return self.idCarrera

    def setIdCarrera(self, idCarrera):
        self.idCarrera = idCarrera

    def getNombreCarrera(self):
        return self.nombreCarrera

    def setNombreCarrera(self, nombreCarrera):
        self.nombreCarrera = nombreCarrera

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def __str__(self):
        return "Id de la Carrera: {}, nombre: {}, departamento: {}".format(self.idCarrera, self.nombreCarrera, self.departamento)