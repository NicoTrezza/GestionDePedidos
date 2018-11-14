from dao.aulaDao import AulaDao

class AulaABM(object):

    def __init__(self):
        self.dao = AulaDao()
        
    def insertar(self, nombreAula, descripcion, iddepartamento):
        self.dao.insertar(nombreAula, descripcion, iddepartamento)

    def insertarpersona(self, idpersona, idaula):
        self.dao.insertarpersona(idpersona, idaula)

    def modificar(self, a):
        self.dao.modificar(a.getIdAula(), a.getNombreAula(), a.getDescripcion(), a.getDepartamentoAula())

    def modificarpersona(self, idpersona, idaula):
        self.dao.modificarpersona(idpersona, idaula)
   
    def eliminar(self, idAula):
        self.dao.eliminar(idAula)

    def eliminar_personaaula(self, idAula):
        self.dao.eliminar_personaaula(idAula)
        
    def traer(self, idAula):
        return self.dao.traer(idAula)

    def traer_personasXAula(self, idAula):
        return self.dao.traer_personasXAula(idAula)

    def traerXNombre(self, nombreAula):
        return self.dao.traerXNombre(nombreAula)
    
    def listar(self):
        return self.dao.listar()