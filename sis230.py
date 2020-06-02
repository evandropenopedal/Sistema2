# importando arquivos da biclioteca
from tkinter import *
from tkinter import messagebox
import tkinter
import sqlite3
from uteis import *
import tkinter as tk
from tkinter import ttk


def Gravar(arg=None):

    miConexion = sqlite3.connect('CADASTRO')

    miCursor = miConexion.cursor()


    miCursor.execute("SELECT * FROM MODULOS WHERE NOME='%s'" % vNome.get())


    vModulo = miCursor.fetchall()

    vDados = ed2.get(), vNome.get()

    for mod in vModulo:
        #vId.set(mod[2])
        ed2.set(mod[1])

    if not vModulo:

        miCursor.execute("INSERT INTO MODULOS VALUES(NULL,?,?)", (vDados))

    else:

        #miCursor.execute("UPDATE MODULOS SET ID=?,SOFT=?,NOME=? WHERE IDENT= " + vId.get(), (vDados))
        miCursor.execute("UPDATE MODULOS SET SOFT=?,NOME=? WHERE NOME='%s'" % vNome.get(), (vDados))

    miConexion.commit()

    Limpar()

def Ler(arg=None):
    miConexion = sqlite3.connect('CADASTRO')

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM MODULOS WHERE NOME=" + vNome.get())

    vModulo = miCursor.fetchall()

    for mod in vModulo:
        vSoft.set(mod[2])
        vNome.set(mod[3])

    #ed2.configure(state='normal')
    ed3.configure(state='normal')
    btd.configure(state='normal')

    miConexion.commit()
    ed3.focus()

def Limpar():
    vId.set('')
    vSoft.set('')
    vNome.set('')

    ed2.set('')
    #ed2.configure(state='disabled')
    ed3.configure(state='disabled')
    btd.configure(state='disabled')

    #ed1.focus()

def Sair(arg=None):

    root1.destroy()
    #import sis000

def Selecao(arg=None):

    miConexion = sqlite3.connect('CADASTRO')

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM SOFTWARE")

    results = [line[2] for line in miCursor]


    #print(results)
    miConexion.commit()

    return results

conexionBbdd()

def Escolha(soft):

    ed3.configure(state='normal')
    btd.configure(state='normal')
    ed3.focus()

    vSoft = ed2.get()

    #print(ed2.current(),vSoft)

    return(ed2.get())


# ----------------

def Modulos(arg=None):

    root1 = Toplevel()

    global vId, vIdent, vSoft, vNome
    global ed1, ed2, ed3, btd

    vId = StringVar()
    vSoft = StringVar()
    vNome = StringVar()

    #root1.geometry("590x300+600+300")
    root1.geometry("590x200+600+300")
    root1.title("Cadastro de Modulos")
    root1.configure(background='white')

    #Dentro = Frame(root1, width=600, height=400, bg="white")
    Dentro = Frame(root1, width=600, height=400, bg="white")
    Dentro.place(x=0, y=0)

    lb0 = Label(Dentro, text="Cadastro de Modulos", font=('Arial', 14), width=53, bg="blue")

    #lb1 = Label(Dentro, text="Identificação : ", font=('Arial', 14), bg="white")
    lb2 = Label(Dentro, text="SoftWare : ", font=('Arial', 14), bg="white")
    lb3 = Label(Dentro, text="Módulo : ", font=('Arial', 14), bg="white")

    #print(Selecao())
    # Entry
    #ed1 = Entry(Dentro, textvariable=vIdent, font=('Arial', 14), bd=2, bg="white", width=20)
    #ed2 = Entry(Dentro, textvariable=vSoft, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=20)
    ed2 = ttk.Combobox(Dentro, values=Selecao(), font=('Arial', 14))
    ed2.bind("<<ComboboxSelected>>", Escolha)
    #ed2.current(1)
    ed3 = Entry(Dentro, textvariable=vNome, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=30)
    #ed3.focus()
    #ed1.bind("<Return>", Ler)

    # Button GRAVAR
    btd = Button(root1, width=10, font=('arial', 10), text="Gravar", state=DISABLED, command=Gravar)
    btd.place(x=480, y=145)

    # Button SAIR
    btd1 = Button(root1, width=10, font=('arial', 10), text="Sair", command=root1.destroy)
    btd1.place(x=15, y=145)

    # Grid
    lb0.grid(row=0, column=0, columnspan=2)
    #lb1.grid(row=20, column=0, pady=10, padx=10)
    lb2.grid(row=30, column=0, pady=10, padx=10)
    lb3.grid(row=40, column=0, pady=10, padx=10)

    #ed1.grid(row=20, column=1, sticky=W)
    ed2.grid(row=30, column=1, sticky=W)
    ed3.grid(row=40, column=1, sticky=W)

    root1.mainloop()