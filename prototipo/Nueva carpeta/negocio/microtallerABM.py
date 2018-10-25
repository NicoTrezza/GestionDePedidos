from dao.microtallerDao import MicrotallerDao

class MicrotallerABM(object):

    def __init__(self):
        self.dao = MicrotallerDao()
        
    def insertar(self, nombreMicrotaller, motivoMicrotaller):
        self.dao.insertar(nombreMicrotaller, motivoMicrotaller)
        
    def modificar(self, m):
        self.dao.modificar(m.getIdMicrotaller(),  m.getNombreMicrotaller(), m.getMotivoMicrotaller())
   
    def eliminar(self, idMicrotaller):
        self.dao.eliminar(idMicrotaller)
        
    def traer(self, idMicrotaller):
        return self.dao.traer(idMicrotaller)
    
    def listar(self):
        return self.dao.listar()