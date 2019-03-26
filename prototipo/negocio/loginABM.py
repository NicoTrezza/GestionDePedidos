from dao.loginDao import LoginDao

class LoginABM(object):

    def __init__(self):
        self.dao = LoginDao()
        
    def insertar(self, mail, contrasenia, permisos, estado):
        self.dao.insertar(mail, contrasenia, permisos, estado)
        
    def modificar(self, l):
        self.dao.modificar(l.getIdLogin(), l.getMail(), l.getContrasenia(), l.getPermisos())
   
    def eliminar(self, idLogin):
        self.dao.eliminar(idLogin)
        
    def traer(self, idLogin):
        return self.dao.traer(idLogin)

    def traerXMail(self, mail):
        return self.dao.traerXMail(mail)
    
    def listar(self):
        return self.dao.listar()

    def listarSolicitados(self):
        return self.dao.listarSolicitados()