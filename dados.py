

#----------------------------
class Mae():
	def __init__(self, nome):
		self.nome = nome
		self.idade = 20
		self.cor = 'parda'
		self.sobren = 'Oliveira'

#----------------------------
#objeto
class cadastro():
    #construtor
	def __init__(self, nome, id_c, saldo, tipo_c):
		self.nome = nome
		self.id_c = id_c
		self.saldo = saldo
    	self.tipo_c = tipo_c
    #metodo
	def saque(self, sacar):
		#Atributos
	    self.sacar = sacar
	    self.saldo = self.saldo - self.sacar

#---------------------------
#objeto
class dado:
	#metodo
	def __init__(self, nome, altura, idade, peso):
		#Atributos
		self.nome = nome
		self.altura = altura
		self.idade = idade
		self. peso = peso