#!/usr/bin/env python
# -*- coding: utf-8 -*-
from negocio.departamentoABM import DepartamentoABM
from negocio.carreraABM import CarreraABM
from negocio.tutoriaABM import TutoriaABM
from negocio.tipoPersonaABM import TipoPersonaABM
from negocio.personaABM import PersonaABM
from negocio.loginABM import LoginABM
from negocio.microtallerABM import MicrotallerABM



def main():
	departamento_abm = DepartamentoABM()
	carrera_abm = CarreraABM()
	tutoria_abm = TutoriaABM()
	tipo_persona_abm = TipoPersonaABM()
	persona_abm = PersonaABM()
	login_abm = LoginABM()
	microtaller_abm = MicrotallerABM()

	# departamento_abm.eliminar(1)
	# departamento_abm.eliminar(2)

	# carrera_abm.eliminar(1)
	# carrera_abm.eliminar(2)

	departamento_abm.insertar('departamento1')
	departamento_abm.insertar('departamento2')
	departamento_abm.insertar('departamento3')

	carrera_abm.insertar('Departamento de Ciencias Básicas', 1)
	carrera_abm.insertar('Departamento de Ingeniería Civil', 2)
	carrera_abm.insertar('Departamento de Ingeniería Eléctrica', 3)
	carrera_abm.insertar('Departamento de Ingeniería Electrónica', 1)
	carrera_abm.insertar('Departamento de Ingeniería Industrial', 2)
	carrera_abm.insertar('Departamento de Ingeniería Mecánica', 3)
	carrera_abm.insertar('Departamento de Ingeniería Naval', 1)
	carrera_abm.insertar('Departamento de Ingeniería Quimica', 2)
	carrera_abm.insertar('Departamento de Ingeniería en Sistemas de Información', 3)
	carrera_abm.insertar('Departamento de Ingeniería Textil', 1)

	# creo un tipo de persona para probar
	tipo_persona_abm.insertar('Admin')
	tipo_persona_abm.insertar('Docente')
	tipo_persona_abm.insertar('estudiánte')
	tipo_persona_abm.insertar('otro')

	# creo un login para la persona de prueba con permisos de administrador
	login_abm.insertar('mailrandom@lalal.com', '1234', 1)
	login_abm.insertar('otromail@lalal.com', '1234', 2)

	# creo una persona de prueba y le doy el login de administrador
	persona_abm.insertar('martín', 'Lanús', 12345678, 'email@lalal.com', 1, 1)
	# creo otra persona de prueba y le doy el login de usuario
	persona_abm.insertar('martín', 'Lanús', 12345687, 'email@lalal.com', 2, 2)

	# creo tutorias
	tutoria_abm.insertar('lelelelmótívo', '2016-01-01', 2)
	tutoria_abm.insertar('lalalalmótívo', '2016-01-01', 2)

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
