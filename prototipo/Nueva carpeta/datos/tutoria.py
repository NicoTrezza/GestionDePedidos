class Tutoria(object):

    def __init__(self, dao):
        self.idTutoria = int(dao[0])
        self.nombreTutoria = str(dao[1])
        self.motivo = str(dao[2])
        self.fechaInicio = int(dao[3])
        self.usuarioTutoria = int(dao[4])

    """def __init__(self, idTutoria, nombreTutoria, motivo, fechaInicio, usuarioTutoria):
        self.idTutoria = idTutoria
        self.nombreTutoria = nombreTutoria
        self.motivo = motivo
        self.fechaInicio = fechaInicio
        self.usuarioTutoria = usuarioTutoria"""

    def getIdTutoria (self):
        return self.idTutoria

    def setIdTutoria (self, idTutoria):
        self.idTutoria = idTutoria

    def getNombreTutoria(self):
        return self.nombreTutoria

    def setNombreTutoria(self, nombreTutoria):
        self.nombreTutoria = nombreTutoria

    def getMotivo(self):
        return self.motivo

    def setMotivo(self, motivo):
        self.motivo = motivo

    def getFechaInicio(self):
        return self.fechaInicio

    def setFechaInicio(self, fechaInicio):
        self.fechaInicio = fechaInicio

    def getUsuarioTutoria(self):
        return self.usuarioTutoria

    def setUsuarioTutoria(self, usuarioTutoria):
        self.usuarioTutoria = usuarioTutoria

    def __str__(self):
        return "Id de la Tutoria: {}, nombre de la Tutoria: {}, motivo de la Tutoria: {}, fecha de inicio de la Tutoria: {}, usuario de la Tutoria: {}".format(self.idTutoria, self.nombreTutoria, self.motivo, self.fechaInicio, self.usuarioTutoria)