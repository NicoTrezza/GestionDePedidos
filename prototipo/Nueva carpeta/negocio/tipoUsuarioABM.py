from dao.tipoUsuarioDao import TipoUsuarioDao

class TipoUsuarioABM(object):

    def __init__(self):
        self.dao = TipoUsuarioDao()
        
    def insertar(self, nombreTipo):
        self.dao.insertar(nombreTipo)
        
    def modificar(self, tu):
        self.dao.modificar(tu.getIdTipoUsuario(), tu.getNombreTipo())
   
    def eliminar(self, idTipoUsuario):
        self.dao.eliminar(idTipoUsuario)
        
    def traer(self, idTipoUsuario):
        return self.dao.traer(idTipoUsuario)
    
    def listar(self):
        return self.dao.listar()