from dao.aulaDao import AulaDao

class AulaABM(object):

    def __init__(self):
        self.dao = AulaDao()
        
    def insertar(self, nombreAula, urlAula, descripcion, carrera):
        self.dao.insertar(nombreAula, urlAula, descripcion, carrera)

    def insertarpersona(self, idpersona, idaula):
        self.dao.insertarpersona(idpersona, idaula)

    def modificar(self, a):
        self.dao.modificar(a.getIdAula(), a.getNombreAula(), a.getUrlAula(), a.getDescripcion(), a.getCarreraAula())
   
    def eliminar(self, idAula):
        self.dao.eliminar(idAula)
        
    def traer(self, idAula):
        return self.dao.traer(idAula)

    def traerXNombre(self, nombreAula):
        return self.dao.traerXNombre(nombreAula)
    
    def listar(self):
        return self.dao.listar()