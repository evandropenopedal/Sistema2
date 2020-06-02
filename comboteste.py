import tkinter as tk
from tkinter import ttk
from uteis import *


conexionBbdd()

#cursor = db.cursor()
#cursor.execute("SELECT * FROM SOFTWARE")

miConexion = sqlite3.connect('CADASTRO')

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM MODULOS WHERE NOME = " + comboExample.get())


results = [line[2] for line in miCursor]

#print(results)
miConexion.commit()
#---------------------------------



def Selecao(soft):


    #vNome = comboExample.get()

    print(comboExample.get())

    return(comboExample.get())





def combo():
    app = tk.Tk()
    app.geometry('200x100')

    global vNome

    #vNome = StringVar()

    labelTop = tk.Label(app, text = "Choose your favourite month")
    labelTop.grid(column=0, row=0)

    comboExample = ttk.Combobox(app, values=results)
    comboExample.bind("<<ComboboxSelected>>", Selecao)

    comboExample.grid(column=0, row=1)
    #comboExample.current(1)
    #print(comboExample.current(), comboExample.get())

    app.mainloop()