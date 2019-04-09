from dao.microtallerDao import MicrotallerDao

class MicrotallerABM(object):

    def __init__(self):
        self.dao = MicrotallerDao()
        
    def insertar(self, nombreMicrotaller, motivoMicrotaller, tipo):
        self.dao.insertar(nombreMicrotaller, motivoMicrotaller, tipo)

    def insertarpersona(self, idMicrotaller, idPersona):
        self.dao.insertarpersona(idMicrotaller, idPersona)
        
    def modificar(self, m):
        self.dao.modificar(m.getIdMicrotaller(),  m.getNombreMicrotaller(), m.getMotivoMicrotaller())
   
    def eliminar(self, idMicrotaller):
        self.dao.eliminar(idMicrotaller)
        
    def traer(self, idMicrotaller):
        return self.dao.traer(idMicrotaller)
    
    def listar(self):
        return self.dao.listar()

    def listarDocentes(self):
        return self.dao.listarDocentes()

    def listarEstudiantes(self):
        return self.dao.listarEstudiantes()

    def listarMicrotalleres(self):
        return self.dao.listarMicrotalleres()