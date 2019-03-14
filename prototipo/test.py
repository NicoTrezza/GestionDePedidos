#!/usr/bin/env python
# -*- coding: utf-8 -*-
from negocio.departamentoABM import DepartamentoABM
from negocio.carreraABM import CarreraABM
from negocio.tipoPersonaABM import TipoPersonaABM
from negocio.personaABM import PersonaABM
from negocio.loginABM import LoginABM
from negocio.microtallerABM import MicrotallerABM
from negocio.tutoriaABM import TutoriaABM



def main():
	departamento_abm = DepartamentoABM()
	carrera_abm = CarreraABM()
	tipo_persona_abm = TipoPersonaABM()
	persona_abm = PersonaABM()
	login_abm = LoginABM()
	microtaller_abm = MicrotallerABM()
	tutoria_abm = TutoriaABM()

	# departamento_abm.eliminar(1)
	# departamento_abm.eliminar(2)

	# carrera_abm.eliminar(1)
	# carrera_abm.eliminar(2)

	departamento_abm.insertar('Departamento de Ciencias Básicas')
	departamento_abm.insertar('Departamento de Ingeniería Civil')
	departamento_abm.insertar('Departamento de Ingeniería Eléctrica')
	departamento_abm.insertar('Departamento de Ingeniería Electrónica')
	departamento_abm.insertar('Departamento de Ingeniería Industrial')
	departamento_abm.insertar('Departamento de Ingeniería Mecánica')
	departamento_abm.insertar('Departamento de Ingeniería Naval')
	departamento_abm.insertar('Departamento de Ingeniería Quimica')
	departamento_abm.insertar('Departamento de Ingeniería en Sistemas de Información')
	departamento_abm.insertar('Departamento de Ingeniería Textil')

	carrera_abm.insertar('Física', 1)
	carrera_abm.insertar('Quimica', 1)
	carrera_abm.insertar('Ingles', 1)
	carrera_abm.insertar('Algebra', 1)
	carrera_abm.insertar('Geogebra', 1)
	carrera_abm.insertar('Análisis matemático', 1)
	carrera_abm.insertar('Probabilidad Estadísticas', 1)

	# creo un tipo de persona especial para Usuario
	tipo_persona_abm.insertar('Docente a cargo')
	tipo_persona_abm.insertar('Docente')
	tipo_persona_abm.insertar('Docente Auxiliar')
	tipo_persona_abm.insertar('Estudiante')

	# creo un tipo de persona para el resto
	"""
	tipo_persona_abm.insertar('Docente a cargo')
	tipo_persona_abm.insertar('Docente')
	tipo_persona_abm.insertar('Docente Auxiliar')
	"""

	# creo un login para la persona de prueba con permisos de administrador
	login_abm.insertar('martin', '1234', 1, 1)
	login_abm.insertar('nico', '1234', 2, 1)
	login_abm.insertar('gris', '1234', 3, 1)
	login_abm.insertar('jose', '1234', 3, 1)
	login_abm.insertar('Dario', '1234', 1, 1)

	# creo una persona de prueba y le doy el login de administrador
	persona_abm.insertar('Martín', 'Lanús', 12345678, 'martin', 1, 1)
	# creo otra persona de prueba y le doy el login de usuario con permisos
	persona_abm.insertar('Nico', 'Boca', 12345687, 'nico', 2, 2)
	# creo otra persona de prueba y le doy el login de usuario comun
	persona_abm.insertar('Gris', 'River', 12345689, 'gris', 3, 3)
	# creo otra persona de prueba y le doy el login de usuario comun
	persona_abm.insertar('Jose', 'River', 12345610, 'jose', 3, 4)
	# creo otra persona de prueba y le doy el otro login de administrador
	persona_abm.insertar('Dario', 'Rodríguez', 12345611, 'Dario', 1, 5)
	#Permiso, id (no lo borren -.- este comentario)

	# creo microtalleres
	microtaller_abm.insertar('Diseño y Gestión del Aula Virtual en Moodle', None, 1)
	microtaller_abm.insertar('Diseño y Gestión del Aula en Moodle: Unidad 1', None, 2)
	microtaller_abm.insertar('Diseño y Gestión del Aula en Moodle: Unidad 2', None, 2)
	microtaller_abm.insertar('Diseño y Gestión del Aula en Moodle: Unidad 3', None, 2)

	# dejo comentado este traer que funciona, creo
	# for a in abm.traerPorProfesor('didio'):
	#	print a

	# tutorias para probar
	# tutoria_abm.insertar('asdf', '2019-03-13 00:00:00', '2019-03-13 00:00:00', '2019-03-13 00:00:00', '2019-03-13 00:00:00', '2019-03-13 00:00:00', '2019-03-13 00:00:00', '1', '1', '2019-03-13 00:00:00')

if __name__ == '__main__':
	main()
