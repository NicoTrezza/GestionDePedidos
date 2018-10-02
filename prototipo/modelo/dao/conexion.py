import mysql.connector
from mysql.connector import Error

class Conexion(object):

	def __init__(self):
		pass

	def conectar(self):
		try:
			self.conexion = mysql.connector.connect(host='localhost', database='pedidos', user='root', password='tin102030')
		except Error as e:
			print e

	def desconectar(self):
		self.conexion.close()
