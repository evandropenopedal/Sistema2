from dados import *
import socket, sys

class op:
    def __init__(self, entrada):
    	self.inicial = entrada

    def __add__(self, other):
        return self.inicial + other.inicial

    def __mul__(self, other):
        return self.inicial * other.inicial

    def __div__(self, other):
        return self.inicial / other.inicial



#----------------------------------
#Python #41 OO
#https://www.youtube.com/watch?v=r2DD0IYzF3s
#atributo - é o conteudo da variavel

pessoa = Mae('Maria')
print(pessoa.nome)

#-------------------------------
#Python #40 OO
cliente = cadastro('Evandro', 99,20000, 'conta poupança')

print('Olá, {} o seu saldo é {}'.format(cliente.nome, cliente.saldo))

cliente.saque(80)

print('Olá, {} o seu saldo é {} apos fazer o saque'.format(cliente.nome, cliente.saldo))


#--------------------------
#Python #39 OO

humano = dado('Joao', 1.7, 54, 67)


print(humano.nome)

#--------------------------
#Python #38 OO
class carro():
	marca = "BMW"
	portas = 4
	tanque = 20

print(carro.marca)

