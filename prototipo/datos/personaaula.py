class Personaaula(object):

    def __init__(self, dao):
        self.idPersonaaula = int(dao[0])
        try:
            self.persona = int(dao[1])
        except:
            self.persona = None
        try:
            self.aula = int(dao[2])
        except:
            self.aula = None
        try:
            self.descripcion = u'{}'.format(dao[3])
        except:
            self.descripcion = None
        try:
            self.ulr = u'{}'.format(dao[4])
        except:
            self.ulr = None
        try:
            self.nombreAnterior = u'{}'.format(dao[5])
        except:
            self.nombreAnterior = None
        try:
            self.otrosReutilizar = u'{}'.format(dao[6])
        except:
            self.otrosReutilizar = None
        try:
            self.motivoEliminacion = u'{}'.format(dao[7])
        except:
            self.motivoEliminacion = None
        self.tipo = int(dao[8])
        self.fechaactual = u'{}'.format(dao[9])

    def getIdPersonaaula(self):
        return self.idPersonaaula

    def setIdPersonaaula(self, idPersonaaula):
        self.idPersonaaula = idPersonaaula

    def getPersona(self):
        return self.persona

    def setPersona(self, persona):
        self.persona = persona

    def getAula(self):
        return self.aula

    def setAula(self, aula):
        self.aula = aula

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getUlr(self):
        return self.ulr

    def setUlr(self, ulr):
        self.ulr = ulr

    def getNombreAnterior(self):
        return self.nombreAnterior

    def setNombreAnterior(self, nombreAnterior):
        self.nombreAnterior = nombreAnterior

    def getOtrosReutilizar(self):
        return self.otrosReutilizar

    def setOtrosReutilizar(self, otrosReutilizar):
        self.otrosReutilizar = otrosReutilizar

    def getMotivoEliminacion(self):
        return self.motivoEliminacion

    def setMotivoEliminacion(self, motivoEliminacion):
        self.motivoEliminacion = motivoEliminacion

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getFechaactual(self):
        return self.fechaactual

    def setFechaactual(self, fechaactual):
        self.fechaactual = fechaactual

    def __str__(self):
        return u'Id: {}, persona: {}, aula: {} , descripcion: {} , ulr: {} , nombre anterior: {} , otros reutilizar: {} , motivo eliminacion: {} , tipo: {}, fecha: {}'.format(self.idPersonaaula, self.persona, self.aula, self.descripcion, self.ulr, self.nombreAnterior, self.otrosReutilizar, self.motivoEliminacion, self.tipo, self.fechaactual)