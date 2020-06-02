from tkinter import *
from uteis import *

conexionBbdd()


miConexion = sqlite3.connect('CADASTRO')

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM SOFTWARE")

results = [line[2] for line in miCursor]

miConexion.commit()

print(results)

#---------------------------------


def Selecao(soft):


    #vNome = comboExample.get()

    print(comboExample.get())

    return(comboExample.get())






root = Tk()

lista = Listbox(root)
lista.pack()

#lista.insert(END, "Primeiro item da lista")
#lista.insert(END, "Segundo item da lista")

Nomes = ["Joao", "Ana", "Carlos"]

for nome in Nomes:
	lista.insert(END, nome)

def executar():
	print(lista.get(ACTIVE))

cmd = Button(root, text="Clique", command=executar).pack()

root.mainloop()