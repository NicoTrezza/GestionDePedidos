from dao.aulaDao import AulaDao

class AulaABM(object):

    def __init__(self):
        self.dao = AulaDao()
        
    def insertar(self, dependencia, nombreDelAula, nombreDelProfesor, emailDelProfesor):
        self.dao.insertar(dependencia, nombreDelAula, nombreDelProfesor, emailDelProfesor)
        
    def modificar(self, a):
        self.dao.modificar(a.getIdAula(), a.getDependencia(), a.getNombreDelAula(), a.getNombreDelProfesor(), a.getEmailDelProfesor())
   
    def eliminar(self, idAula):
        self.dao.eliminar(idAula)
        
    def traer(self, idAula):
        return self.dao.traer(idAula)
        
    def traerPorProfesor(self, nombreDelProfesor):
        return self.dao.traerPorProfesor(nombreDelProfesor)
    
    def listar(self):
        return self.dao.listar()