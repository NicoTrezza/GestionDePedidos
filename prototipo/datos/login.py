class Login(object):

    def __init__(self, dao):
        self.idLogin = int(dao[0])
        self.mail = str(dao[1])
        self.contrasenia = str(dao[2])
        self.permisos = int(dao[3])  # 1= administrador, 2= usuario
        self.estado = int(dao[4])    # 0= solicitado, 1= activo

    def getIdLogin(self):
        return self.idLogin

    def setIdLogin(self, idLogin):
        self.idLogin = idLogin

    def getMail(self):
        return self.mail

    def setMail(self, mail):
        self.mail = mail

    def getContrasenia(self):
        return self.contrasenia

    def setContrasenia(self, contrasenia):
        self.contrasenia = contrasenia

    def getPermisos(self):
        return self.permisos

    def setPermisos(self, permisos):
        self.permisos = permisos

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def __str__(self):
        return "Id del login: {}, mail del login: {}, contrasenia del login: {}, permisos del login: {}".format(self.idLogin, self.mail, self.contrasenia, self.permisos)