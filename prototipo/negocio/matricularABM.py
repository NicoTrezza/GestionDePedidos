from dao.matricularDao import MatricularDao


class MatricularABM(object):

    def __init__(self):
        self.dao = MatricularDao()

    def insertar(self, departamento, fechaactual):
        self.dao.insertar(departamento, fechaactual)

    def insertarpersona(self, idMatricular, idPersona):
        self.dao.insertarpersona(idMatricular, idPersona)

    def modificar(self, m):
        self.dao.modificar(m.getIdMatricular(), m.getDepartamento(), m.getFechaactual())

    def eliminar(self, idMatricular):
        self.dao.eliminar(idMatricular)

    def traer(self, idMatricular):
        return self.dao.traer(idMatricular)

    def listar(self):
        return self.dao.listar()
