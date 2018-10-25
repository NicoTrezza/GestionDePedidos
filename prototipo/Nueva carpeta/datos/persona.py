class Usuario(object):

	def __init__(self, dao):
		self.idUsuario = int(dao[0])
		self.nombre = str(dao[1])
		self.apellido = str(dao[2])
		self.dni = int(dao[3])
		self.tipoPersona = int(dao[4])
		self.carrera = int(dao[5])
		self.login = int(dao[6])

	"""def __init__(self, idUsuario, nombre, apellido, dni, tipoPersona, carrera, login):
		self.idUsuario = idUsuario
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.tipoPersona = tipoPersona
		self.carrera = carrera
		self.login = login"""

	def getIdUsuario(self):
		return self.idUsuario

	def setIdUsuario(self, idUsuario):
		self.idUsuario = idUsuario

	def getNombre(self):
		return self.nombre

	def setNombre(self, nombre):
		self.nombre = nombre

	def getApellido(self):
		return self.apellido

	def setApellido(self, apellido):
		self.apellido = apellido

	def getDni(self):
		return self.dni

	def setDni(self, dni):
		self.dni = dni

	def getTipoPersona(self):
		return self.tipoPersona

	def setTipoPersona(self, tipoPersona):
		self.tipoPersona = tipoPersona

	def getCarrera(self):
		return self.carrera

	def setCarrera(self, carrera):
		self.carrera = carrera

	def getLogin(self):
		return self.login

	def setLogin(self, login):
		self.login = login
		
	def __str__(self):
		return "Id del usuario: {}, nombre: {}, apellido: {}, dni: {}, tipo de Persona: {}, carrera: {}, login: {}".format(self.idUsuario, self.nombre, self.apellido, self.dni, self.tipoPersona, self.carrera, self.login)

