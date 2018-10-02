from dao.usuarioDao import UsuarioDao

class UsuarioABM(object):

    def __init__(self):
        self.dao = UsuarioDao()
        
    def insertar(self, nombre, apellido, dni, email):
        self.dao.insertar(nombre, apellido, dni, email)
        
    def modificar(self, u):
        self.dao.modificar(u.getIdUsuario(), u.getNombre(), u.getApellido(), u.getDni(), u.getEmail())
   
    def eliminar(self, idUsuario):
        self.dao.eliminar(idUsuario)
        
    def traer(self, idUsuario):
        return self.dao.traer(idUsuario)
        
    def listar(self):
        return self.dao.listar()