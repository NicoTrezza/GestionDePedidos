from dao.loginDao import LoginDao
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class LoginABM(object):

    def __init__(self):
        self.dao = LoginDao()

    def checkPassword(self, l, contrasenia):
        return check_password_hash(l.getContrasenia(), contrasenia)

    def insertar(self, mail, contrasenia, permisos, estado):
        self.dao.insertar(mail, generate_password_hash(contrasenia), permisos, estado)
        
    def modificar(self, l):
        self.dao.modificar(l.getIdLogin(), l.getMail(), generate_password_hash(l.getContrasenia()), l.getPermisos())

    def confirmarcuenta(self, idLogin):
        self.dao.confirmarcuenta(idLogin)
   
    def eliminar(self, idLogin):
        self.dao.eliminar(idLogin)
        
    def traer(self, idLogin):
        return self.dao.traer(idLogin)

    def traerXMail(self, mail):
        return self.dao.traerXMail(mail)

    def traePersonaLoginXMail(self, mail):
        return self.dao.traePersonaLoginXMail(mail)
    
    def listar(self):
        return self.dao.listar()

    def listarSolicitados(self):
        return self.dao.listarSolicitados()

    def listarLoginYPersona(self):
        return self.dao.listarLoginYPersona()