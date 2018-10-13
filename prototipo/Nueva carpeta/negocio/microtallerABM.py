from dao.microtallerDao import MicrotallerDao

class MicrotallerABM(object):

    def __init__(self):
        self.dao = MicrotallerDao()
        
    def insertar(self, nombreMicrotaller, descripcion, usuarioMicrotaller):
        self.dao.insertar(nombreMicrotaller, descripcion, usuarioMicrotaller)
        
    def modificar(self, m):
        self.dao.modificar(m.getIdMicrotaller(),  m.getNombreMicrotaller(), m.getDescripcion(), m.getUsuarioMicrotaller())
   
    def eliminar(self, idMicrotaller):
        self.dao.eliminar(idMicrotaller)
        
    def traer(self, idMicrotaller):
        return self.dao.traer(idMicrotaller)
    
    def listar(self):
        return self.dao.listar()