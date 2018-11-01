from dao.loginDao import LoginDao

class LoginABM(object):

    def __init__(self):
        self.dao = LoginDao()
        
    def insertar(self, mail, contrasenia, permisos):
        self.dao.insertar(mail, contrasenia, permisos)
        
    def modificar(self, l):
        self.dao.modificar(l.getIdLogin(), l.getMail(), l.getContrasenia(), l.getPermisos())
   
    def eliminar(self, idLogin):
        self.dao.eliminar(idLogin)
        
    def traer(self, idLogin):
        return self.dao.traer(idLogin)
    
    def listar(self):
        return self.dao.listar()