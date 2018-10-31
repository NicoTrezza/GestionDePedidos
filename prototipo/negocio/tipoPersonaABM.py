from dao.tipoPersonaDao import TipoPersonaDao

class TipoPersonaABM(object):

    def __init__(self):
        self.dao = TipoPersonaDao()
        
    def insertar(self, rol):
        self.dao.insertar(rol)
        
    def modificar(self, tu):
        self.dao.modificar(tu.getIdTipoPersona(), tu.getRol())
   
    def eliminar(self, idTipoPersona):
        self.dao.eliminar(idTipoPersona)
        
    def traer(self, idTipoPersona):
        return self.dao.traer(idTipoPersona)
    
    def listar(self):
        return self.dao.listar()