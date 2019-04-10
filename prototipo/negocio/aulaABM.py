from dao.aulaDao import AulaDao
import time


class AulaABM(object):

    def __init__(self):
        self.dao = AulaDao()
        
    def insertar(self, nombreAula, descripcion, iddepartamento):
        return self.dao.insertar(nombreAula, descripcion, iddepartamento)

    def insertaraula_personaaula(self, idaula, idtipo):
        self.dao.insertaraula_personaaula(idaula, idtipo)

    def insertarpersona(self, idpersona, idaula, idtipo):
        self.dao.insertarpersona(idpersona, idaula, idtipo)

    def insertarpersona_crear(self, idpersona, idaula, descipcion):
        self.dao.insertarpersona_crear(idpersona, idaula, descipcion, 1, time.strftime("%Y-%m-%d %H:%M:%S"))

    def insertarpersona_modificar(self, idpersona, idaula, url, nombre_anterior, otros):
        self.dao.insertarpersona_modificar(idpersona, idaula, url, nombre_anterior, otros, 2, time.strftime("%Y-%m-%d %H:%M:%S"))

    def insertarpersona_eliminar(self, idaula, url, motivo):
        self.dao.insertarpersona_eliminar(idaula, url, motivo, 3, time.strftime("%Y-%m-%d %H:%M:%S"))

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

    def listarAulasCrear(self):
        return self.dao.listarAulasCrear()

    def listarAulasModificar(self):
        return self.dao.listarAulasModificar()

    def listarAulasEliminar(self):
        return self.dao.listarAulasEliminar()
