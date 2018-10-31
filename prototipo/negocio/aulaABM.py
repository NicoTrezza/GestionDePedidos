from dao.aulaDao import AulaDao

class AulaABM(object):

    def __init__(self):
        self.dao = AulaDao()
        
    def insertar(self, nombreAula, urlAula, descripcion, carreraAula):
        self.dao.insertar(nombreAula, urlAula, descripcion, carreraAula)
        
    def modificar(self, a):
        self.dao.modificar(a.getIdAula(), a.getNombreAula(), a.getUrlAula(), a.getDescripcion(), a.getCarreraAula())
   
    def eliminar(self, idAula):
        self.dao.eliminar(idAula)
        
    def traer(self, idAula):
        return self.dao.traer(idAula)
    
    def listar(self):
        return self.dao.listar()