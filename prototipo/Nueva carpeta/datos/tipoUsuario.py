class TipoUsuario(object):

    def __init__(self, dao):
        self.idTipoUsuario = int(dao[0])
        self.nombreTipo = str(dao[1])

    """def __init__(self, idTipoUsuario, nombreTipo:
        self.idTipoUsuario = idTipoUsuario
        self.nombreTipo = nombreTipo"""

    def getIdTipoUsuario(self):
        return self.idTipoUsuario

    def setIdTipoUsuario(self, idTipoUsuario):
        self.idTipoUsuario = idTipoUsuario

    def getNombreTipo(self):
        return self.nombreTipo

    def setNombreTIpo(self, nombreTipo):
        self.nombreTipo = nombreTipo

    def __str__(self):
        return "Id del Tipo de Usuario: {}, nombre del Tipo de Usuario: {}".format(self.idTipoUsuario, self.nombreTipo)