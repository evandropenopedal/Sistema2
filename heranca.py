
python #43 OO 
#---------------------------------------------
class mae:
	nome = "Maria"
	altura = 1.79
	end = "Rua da Paz, 12"
	olhos = "Azul"
	peso = "69kg"

class filha(mae):
	nome = "Patricia"

pessoa = filha()

class filho(filha):
	nome = "Pedro"
	altura = 1.69

filhos = filho()

print('{} irmã do {} moram na {}'.format(pessoa.nome,filhos.nome,pessoa.end))
