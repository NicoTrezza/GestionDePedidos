from negocio.aulaABM import AulaABM
from negocio.usuarioABM import UsuarioABM

def main():
	abm = AulaABM()
	
	abm.insertar(1,"nombreAula1","profesor1","email@asd.com")
	
	for a in abm.traerPorProfesor('didio'):
		print a
	
if __name__ == '__main__':
	main()
