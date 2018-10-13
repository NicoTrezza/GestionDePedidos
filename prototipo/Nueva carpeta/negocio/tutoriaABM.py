from dao.tutoriaDao import TutoriaDao

class TutoriaABM(object):

    def __init__(self):
        self.dao = TutoriaDao()
        
    def insertar(self, nombreTutoria, motivo, fechaInicio, usuarioTutoria):
        self.dao.insertar(nombreTutoria, motivo, fechaInicio, usuarioTutoria)
        
    def modificar(self, t):
        self.dao.modificar(t.getIdTutoria(), t.getNombreTutoria(), t.getMotivo(), t.getFechaInicio(), t.getUsuarioTutoria())
   
    def eliminar(self, idTutoria):
        self.dao.eliminar(idTutoria)
        
    def traer(self, idTutoria):
        return self.dao.traer(idTutoria)
    
    def listar(self):
        return self.dao.listar()