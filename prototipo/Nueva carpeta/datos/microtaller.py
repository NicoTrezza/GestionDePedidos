class MicroTaller(object):

    def __init__(self, dao):
        self.idMicrotaller = int(dao[0])
        self.nombreMicrotaller = str(dao[1])
        self.descripcion = str(dao[2])
        self.usuarioMicrotaller = int(dao[3])

    """def __init__(self, idMicrotaller, nombreMicrotaller, descripcion, usuarioMicrotaller):
        self.idMicrotaller = idMicrotaller
        self.nombreMicrotaller = nombreMicrotaller
        self.descripcion = descripcion
        self.usuarioMicrotaller = usuarioMicrotaller"""

    def getIdMicrotaller(self):
        return self.idMicrotaller

    def setIdMicrotaller(self, idMicrotaller):
        self.idMicrotaller = idMicrotaller

    def getNombreMicrotaller(self):
        return self.nombreMicrotaller

    def setNombreMicrotaller(self, nombreMicrotaller):
        self.nombreMicrotaller = nombreMicrotaller

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getUsuarioMicrotaller(self):
        return self.usuarioMicrotaller

    def setUsuarioMicrotaller(self, usuarioMicrotaller):
        self.usuarioMicrotaller = usuarioMicrotaller

    def __str__(self):
        return "Id del microtaller: {}, nombre del microtaller: {}, descripcion del microtaller: {}, usuario del microtaller: {}".format(self.idMicrotaller, self.nombreMicrotaller, self.descripcion, self.usuarioMicrotaller)