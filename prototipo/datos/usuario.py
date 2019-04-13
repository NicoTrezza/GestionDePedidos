class Usuario(object):

    def __init__(self, dao):
        self.idUsuario = int(dao[0])
        self.fechaactual = u'{}'.format(dao[1])
        self.persona = int(dao[2])

    def getIdUsuario(self):
        return self.idUsuario

    def setIdUsuario(self, idUsuario):
        self.idUsuario = idUsuario

    def getFechaactual(self):
        return self.fechaactual

    def setFechaactual(self, fechaactual):
        self.fechaactual = fechaactual

    def getPersona(self):
        return self.persona

    def setPersona(self, persona):
        self.persona = persona

    def __str__(self):
        return "Id: {}, fecha: {}, persona: {}".format(self.idUsuario, self.fechaactual, self.persona)
