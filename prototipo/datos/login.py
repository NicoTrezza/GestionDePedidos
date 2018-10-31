class Login(object):

    def __init__(self, dao):
        self.idLogin = int(dao[0])
        self.mail = str(dao[1])
        self.contrasenia = str(dao[2])

    """def __init__(self, idLogin, mail, contrasenia):
        self.idLogin = idLogin
        self.mail = mail
        self.contrasenia = contrasenia"""

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

    def __str__(self):
        return "Id del login: {}, mail del login: {}, contrasenia del login: {}".format(self.idLogin, self.mail, self.contrasenia)