class Usuario(object):

	def __init__(self, dao):
		self.idUsuario = int(dao[0])
		self.nombre = str(dao[1])
		self.apellido = str(dao[2])
		self.dni = int(dao[3])
		self.login = int(dao[4])
		self.tipoUsuario = int(dao[5])
		self.departamentoUsuario = int(dao[6])

	"""def __init__(self, idUsuario, nombre, apellido, dni, login, tipoUsuario, departamentoUsuario):
		self.idUsuario = idUsuario
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.login = login
		self.tipoUsuario = tipoUsuario
		self.departamentoUsuario = departamentoUsuario"""

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

	def getLogin(self):
		return self.login

	def setLogin(self, login):
		self.login = login

	def getTipoUsuario(self):
		return self.tipoUsuario

	def setTipoUsuario(self, tipoUsuario):
		self.tipoUsuario = tipoUsuario

	def getDepartamentoUsuario(self):
		return self.departamentoUsuario

	def setDepartamentoUsuario(self, departamentoUsuario):
		self.departamentoUsuario = departamentoUsuario
		
	def __str__(self):
		return "Id del usuario: {}, nombre: {}, apellido: {}, dni: {}, login: {}, tipo de usuario: {}, departamento: {}".format(self.idUsuario, self.nombre, self.apellido, self.dni, self.login, self.tipoUsuario, self.departamentoUsuario)

