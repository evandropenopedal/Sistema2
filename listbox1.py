from tkinter import *
from uteis import *
import tkinter as tk
from tkinter import ttk

conexionBbdd()
conexionBbdd1()

miConexion = sqlite3.connect('CADASTRO')

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM MODULOS")

results = [line[2] for line in miCursor]

miConexion.commit()


#----------------------------------------


def Gravar(arg=None):

    miConexion = sqlite3.connect('PROPOSTA')

    miCursor = miConexion.cursor()


	#for nome in results:

    #vDados = list.get(), vNome.get()

	#print(list.get())


	#miCursor.execute("INSERT INTO MODULOS VALUES(NULL,?,?)", (vDados))


    #for mod in vModulo:
    #    #vId.set(mod[2])
    #    ed2.set(mod[1])


    miConexion.commit()

#---------------------------------
def Click(event=None):
	#for nome in results:

	selecao = [line[2] for line in lista.get()]

	#print(lista.get())
	print(selecao)

#-------------------------------
root = Tk()

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)


vSelec = list()
lista = Listbox(root, yscrollcommand= scroll.set,  selectmode=EXTENDED, width=30, height=5)
lista.pack()

for nome in results:
	lista.insert(END, nome)

def executar():


	miConexion = sqlite3.connect('PROPOSTA')

	miCursor = miConexion.cursor()

	itens = lista.curselection()

	for item in itens:
		vSelec.append(lista.get(item))
		#print(lista.get(item))



	for grava in vSelec:

		vDados = "444", grava
		query_eva = """INSERT INTO PEDMOD (ID, IDPED, NMMODULO) VALUES (NULL, ?, ?)"""
		miCursor.execute(query_eva, vDados)

		#vDados = "123", grava
		#miCursor.execute("INSERT INTO PEDMOD VALUES(NULL,?,?)", (vDados))
		#miCursor.execute("INSERT INTO PEDMOD VALUES(NULL,%s,?)", (vDados))


		print(vDados)


	miConexion.commit()
	miConexion.close()
	#miConexion.rollback()


btd = Button(root, text="Gravar", command=executar).pack()


scroll.config(command=lista.yview)
root.mainloop()



#print(results)

