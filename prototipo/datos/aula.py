class Aula(object):

    def __init__(self, dao):
        self.idAula = int(dao[0])
        self.nombreAula = str(dao[1])
        self.urlAula = str(dao[2])
        try:
            self.descripcion = str(dao[3])
        except:
            self.descripcion = None
        self.carreraAula = int(dao[4])

    def getIdAula(self):
        return self.idAula

    def setIdAula(self, idAula):
        self.idAula = idAula

    def getNombreAula(self):
        return self.nombreAula

    def setNombreAula(self, nombreAula):
        self.nombreAula = nombreAula

    def getUrlAula(self):
        return self.urlAula

    def setUrlAula(self, urlAula):
        self.urlAula = urlAula

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getCarreraAula(self):
        return self.carreraAula

    def setCarreraAula(self, carreraAula):
        self.carreraAula = carreraAula

    def __str__(self):
        return "Id del aula: {}, nombre del Aula: {}, url del Aula: {}, descripcion del Aula: {}".format(self.idAula, self.nombreAula, self.urlAula, self.descripcion)
