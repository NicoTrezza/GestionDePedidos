#!/usr/bin/env python
# -*- coding: utf-8 -*-
from negocio.departamentoABM import DepartamentoABM
from negocio.carreraABM import CarreraABM
from negocio.tipoPersonaABM import TipoPersonaABM
from negocio.PersonaABM import PersonaABM
from negocio.loginABM import LoginABM
from negocio.microtallerABM import MicrotallerABM



def main():
	departamento_abm = DepartamentoABM()
	carrera_abm = CarreraABM()
	tipo_persona_abm = TipoPersonaABM()
	persona_abm = PersonaABM()
	login_abm = LoginABM()
	microtaller_abm = MicrotallerABM()

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
	departamento_abm.insertar('este es el de las carreras adentro Griss XD')

	carrera_abm.insertar('carrera1', 11)
	carrera_abm.insertar('carrera2', 11)
	carrera_abm.insertar('carrera3', 11)

	# creo un tipo de persona para probar
	tipo_persona_abm.insertar('Docente')
	tipo_persona_abm.insertar('No docente')
	tipo_persona_abm.insertar('Estudiante')
	tipo_persona_abm.insertar('otro')

	# creo un login para la persona de prueba con permisos de administrador
	login_abm.insertar('mailrandom@lalal.com', '1234', 1)
	login_abm.insertar('otromail@lalal.com', '1234', 2)

	# creo una persona de prueba y le doy el login de administrador
	persona_abm.insertar('martín', 'Lanús', 12345678, 'email@lalal.com', 1, 1)
	# creo otra persona de prueba y le doy el login de usuario
	persona_abm.insertar('martín', 'Lanús', 12345687, 'email@lalal.com', 2, 2)

	# creo microtalleres
	microtaller_abm.insertar('microtáller1', None, 1)
	microtaller_abm.insertar('micrótaller2', 'motívo', 1)
	microtaller_abm.insertar('mícrotaller3', 'motivo', 2)
	microtaller_abm.insertar('microtaller4', None, 2)


	# dejo comentado este traer que funciona, creo
	# for a in abm.traerPorProfesor('didio'):
	#	print a


if __name__ == '__main__':
	main()
