from dao.departamentoDao import DepartamentoDao

class DepartamentoABM(object):

    def __init__(self):
        self.dao = DepartamentoDao()
        
    def insertar(self, nombreDepartamento):
        self.dao.insertar(nombreDepartamento)
        
    def modificar(self, d):
        self.dao.modificar(d.getIdDepartamento(), d.getNombreDepartamento())
   
    def eliminar(self, idDepartamento):
        self.dao.eliminar(idDepartamento)
        
    def traer(self, idDepartamento):
        return self.dao.traer(idDepartamento)
    
    def listar(self):
        return self.dao.listar()