from dao.aulaDao import AulaDao

class AulaABM(object):

    def __init__(self):
        self.dao = AulaDao()
        
    def insertar(self, nombreAula, departamentoAula):
        self.dao.insertar(nombreAula, departamentoAula)
        
    def modificar(self, a):
        self.dao.modificar(a.getIdAula(), a.getNombreAula(), a.getDepartamentoAula())
   
    def eliminar(self, idAula):
        self.dao.eliminar(idAula)
        
    def traer(self, idAula):
        return self.dao.traer(idAula)
    
    def listar(self):
        return self.dao.listar()