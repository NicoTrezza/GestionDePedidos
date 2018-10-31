#!/usr/bin/env python
# -*- coding: utf-8 -*-
from negocio.departamentoABM import DepartamentoABM
from negocio.carreraABM import CarreraABM

def main():
	departamento_abm = DepartamentoABM()
	carrera_abm = CarreraABM()

	#departamento_abm.eliminar(1)
	#departamento_abm.eliminar(2)

	#carrera_abm.eliminar(1)
	#carrera_abm.eliminar(2)

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

	#dejo comentado este traer que funciona, creo
	#for a in abm.traerPorProfesor('didio'):
	#	print a


if __name__ == '__main__':
	main()
