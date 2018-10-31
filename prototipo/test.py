from negocio.departamentoABM import DepartamentoABM
from negocio.carreraABM import CarreraABM

def main():
	departamento_abm = DepartamentoABM()
	carrera_abm = CarreraABM()

	departamento_abm.insertar('departamento1')
	carrera_abm.insertar('carrera1', 1)


	#dejo comentado este traer que funciona, creo
	#for a in abm.traerPorProfesor('didio'):
	#	print a


if __name__ == '__main__':
	main()
