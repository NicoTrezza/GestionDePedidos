class TipoUsuario(object):

    def __init__(self, dao):
        self.idTipoPersona = int(dao[0])
        self.rol = str(dao[1])

    """def __init__(self, idTipoPersona, rol):
        self.idTipoPersona = idTipoPersona
        self.rol = rol"""

    def getIdTipoPersona(self):
        return self.idTipoPersona

    def setIdTipoPersona(self, idTipoPersona):
        self.idTipoPersona = idTipoPersona

    def getRol(self):
        return self.rol

    def setRol(self, rol):
        self.rol = rol

    def __str__(self):
        return "Id del Tipo de persona: {},rol de persona: {}".format(self.idTipoPersona, self.rol)