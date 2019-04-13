from dao.usuarioDao import UsuarioDao
import time


class UsuarioABM(object):

    def __init__(self):
        self.dao = UsuarioDao()

    def insertar(self, persona):
        self.dao.insertar(time.strftime("%Y-%m-%d %H:%M:%S"), persona)

    def modificar(self, u):
        self.dao.modificar(u.getFechaactual(), u.getPersona())

    def eliminar(self, idUsuario):
        self.dao.eliminar(idUsuario)

    def traer(self, idUsuario):
        return self.dao.traer(idUsuario)

    def listar(self):
        return self.dao.listar()
