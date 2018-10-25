from dao.tutoriaDao import TutoriaDao

class TutoriaABM(object):

    def __init__(self):
        self.dao = TutoriaDao()
        
    def insertar(self, motivo, fecha, personaTutoria):
        self.dao.insertar(motivo, fecha, personaTutoria)
        
    def modificar(self, t):
        self.dao.modificar(t.getIdTutoria(), t.getMotivo(), t.getFecha(), t.getPersonaTutoria())
   
    def eliminar(self, idTutoria):
        self.dao.eliminar(idTutoria)
        
    def traer(self, idTutoria):
        return self.dao.traer(idTutoria)
    
    def listar(self):
        return self.dao.listar()