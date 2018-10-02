class Usuario(object):

	def __init__(self, dao):
		self.idUsuario = int(dao[0])
		self.nombre = str(dao[1])
		self.apellido = str(dao[2])
		self.dni = int(dao[3])
		self.email = str(dao[4])

	"""def __init__(self, idUsuario, nombre, apellido, dni, email):
		self.idUsuario = idUsuario
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.email = email"""

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

	def getEmail(self):
		return self.email

	def setEmail(self, email):
		self.email = email
		
	def __str__(self):
		return "Id del usuario: {}, nombre: {}, apellido: {}, dni: {}, email: {}".format(self.idUsuario, self.nombre, self.apellido, self.dni, self.email)

