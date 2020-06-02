from tkinter import *
from uteis import *
import tkinter as tk
from tkinter import ttk

#conexionBbdd()

#miConexion = sqlite3.connect('CADASTRO')

#miCursor = miConexion.cursor()

#miCursor.execute("SELECT * FROM SOFTWARE")

#results = [line[2] for line in miCursor]

#miConexion.commit()



results  = [
    "January",
    "February",
    "March",
    "April"]

def Gravar():
    print(opcao.get())
    print()


root = Tk()
opcao = IntVar()
#l = IntVar()
l=0

for nome in results:

    l = l + 1

    cmd = Checkbutton(root, text=nome, variable=opcao,  onvalue = 1, offvalue = 0).grid(row=l, column=0, sticky='W')


#v = "opcao"+str(3)

bt = Button(root, text="Gravar", command=Gravar).grid(row=20, column=10, sticky='W')

root.mainloop()

#if opcao.get() == 1:
#    print(opcao.get())

