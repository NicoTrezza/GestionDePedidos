from dao.carreraDao import CarreraDao

class CarreraABM(object):

    def __init__(self):
        self.dao = CarreraDao()
        
    def insertar(self, nombreCarrera, departamento):
        self.dao.insertar(nombreCarrera, departamento)
        
    def modificar(self, c):
        self.dao.modificar(c.getIdCarrera(), c.getNombreCarrera(), c.getDepartamento())
   
    def eliminar(self, idCarrera):
        self.dao.eliminar(idCarrera)
        
    def traer(self, idCarrera):
        return self.dao.traer(idCarrera)
    
    def listar(self):
        return self.dao.listar()