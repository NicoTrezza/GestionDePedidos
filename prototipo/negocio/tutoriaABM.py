from dao.tutoriaDao import TutoriaDao

class TutoriaABM(object):

    def __init__(self):
        self.dao = TutoriaDao()
        
    def insertar(self, motivo, personaTutoria, departamento):
        self.dao.insertar(motivo, personaTutoria, departamento)
        
    def modificar(self, t):
        self.dao.modificar(t.getIdTutoria(), t.getMotivo(), t.getPersonaTutoria(), t.getDepartamento())
   
    def eliminar(self, idTutoria):
        self.dao.eliminar(idTutoria)
        
    def traer(self, idTutoria):
        return self.dao.traer(idTutoria)
    
    def listar(self):
        return self.dao.listar()