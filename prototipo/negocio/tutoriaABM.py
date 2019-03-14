from dao.tutoriaDao import TutoriaDao

class TutoriaABM(object):

    def __init__(self):
        self.dao = TutoriaDao()
        
    def insertar(self, motivo, fecha1desde, fecha1hasta, fecha2desde, fecha2hasta, fecha3desde, fecha3hasta, personaTutoria, departamento, fechaactual):
        self.dao.insertar(motivo, fecha1desde, fecha1hasta, fecha2desde, fecha2hasta, fecha3desde, fecha3hasta, personaTutoria, departamento, fechaactual)
        
    def modificar(self, t):
        self.dao.modificar(t.getIdTutoria(), t.getMotivo(), t.getPersonaTutoria(), t.getDepartamento())
   
    def eliminar(self, idTutoria):
        self.dao.eliminar(idTutoria)
        
    def traer(self, idTutoria):
        return self.dao.traer(idTutoria)
    
    def listar(self):
        return self.dao.listar()