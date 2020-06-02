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

    miCursor.execute("SELECT * FROM CLIENTES WHERE IDENT=" + vIdent.get())

    vCliente = miCursor.fetchall()

    vDados = vIdent.get(), vNome.get(), vEnder.get(), vContato.get()

    for cliente in vCliente:
        vNome.set(cliente[2])
        vEnder.set(cliente[3])
        vContato.set(cliente[4])

    if not vCliente:

        miCursor.execute("INSERT INTO CLIENTES VALUES(NULL,?,?,?,?)", (vDados))
        #tkinter.messagebox.showinfo('BBDD', 'Registro inserido com sucesso')

    else:

        miCursor.execute("UPDATE CLIENTES SET IDENT=?,NOME=?,ENDER=?,CONTATO=? WHERE IDENT= " + vIdent.get(), (vDados))

        # tkinter.messagebox.showinfo('BBDD', 'Registro ALTERADO com sucesso')

    # vDados = vIdent.get(),vNome.get(),vEnder.get(),vContato.get()

    miConexion.commit()

    Limpar()

def Ler(arg=None):
    miConexion = sqlite3.connect('PROPOSTA')

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM PEDIDO WHERE IDENT=" + vIdent.get())

    vPedido = miCursor.fetchall()

    #vDados = vIdent.get(), vIdecli.get(), vIdesoft.get(), vNomMod.get(), vObserv.get()


    for ped in vPedido:
        vIdecli.set(ped[2])
        vIdesof.set(ped[3])
        vNomMod.set(ped[4])
        vObserv.set(ped[5])

    ed2.configure(state='normal')
    ed3.configure(state='normal')
    #ed4.configure(state='normal')
    #ed5.configure(state='normal')
    btd.configure(state='normal')

    miConexion.commit()
    ed2.focus()

def Limpar():
    vId.set('')
    vNome.set('')
    vIdent.set('')
    vEnder.set('')
    vContato.set('')

    ed2.configure(state='disabled')
    ed3.configure(state='disabled')
    ed4.configure(state='disabled')
    btd.configure(state='disabled')

    ed1.focus()

def Sair(arg=None):

    root1.destroy()
    #import sis000

def SelSof(arg=None):

    miConexion = sqlite3.connect('CADASTRO')

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM SOFTWARE")

    ResSoft = [line[2] for line in miCursor]

    return ResSoft

conexionBbdd()

def EscSoft():

    ed2.configure(state='normal')
    #ed4.configure(state='normal')
    #ed5.configure(state='normal')
    btd.configure(state='normal')
    #ed4.focus()


    miConexion = sqlite3.connect('CADASTRO')
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM MODULOS WHERE SOFT='%s'" % ed3.get())
    ResMod = [line[2] for line in miCursor]
    miCursor.close()

    #print(ResMod)

    return(ResMod)


def SelCli(arg=None):

    miConexion = sqlite3.connect('CADASTRO')

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM CLIENTES")

    results = [line[2] for line in miCursor]

    #print(results)
    miConexion.commit()

    return results

#conexionBbdd()

def EscCli(soft):

    ed3.configure(state='normal')
    #ed4.configure(state='normal')
    #ed5.configure(state='normal')
    btd.configure(state='normal')
    #ed4.focus()

    vSoft = ed3.get()

    #print(ed2.current(),vSoft)

    return(ed2.get())


# -------- criar banco de dados -----------

conexionBbdd()
conexionBbdd1()

# ---------------- iniciando o objeto da tela

def Proposta(arg=None):

    # ---------------- iniciando o objeto da tela

    root1 = Toplevel()

    global vId, vIdent, vIdecli, vIdesof, vNomMod, vObserv
    global ed1, ed2, ed3, ed4, ed5, btd


    vId = StringVar()
    vIdent = StringVar()
    vIdecli = StringVar()
    vIdesof = StringVar()
    vNomMod = StringVar()
    vObserv = StringVar()


    # passando as medidas e configuracoes da tela
    root1.geometry("590x400+600+300")
    root1.title("Sistema de Cadastro")
    root1.configure(background='white')


    # criando o frame(tabela) do topo
    #Top = Frame(root1, width=600, height=50)
    #Top.pack(side=TOP)

    # RigthP1 - Painel da dieita
    Dentro = Frame(root1, width=600, height=400, bg="white")
    Dentro.place(x=0, y=0)


    lb0 = Label(Dentro, text="Proposta para o Clientes", font=('Arial', 14), width=53, bg="yellow")

    lb1 = Label(Dentro, text="Numero : ", font=('Arial', 14), bg="white")
    lb2 = Label(Dentro, text="Cliente : ", font=('Arial', 14), bg="white")
    lb3 = Label(Dentro, text="SoftWare : ", font=('Arial', 14), width=10, bg="white")
    lb4 = Label(Dentro, text="Modulos : ", font=('Arial', 14), bg="white")
    #lb5 = Label(Dentro, text="Observação: ", font=('Arial', 14), bg="white")

    # Entry
    ed1 = Entry(Dentro, textvariable=vIdent, font=('Arial', 14), bd=2, bg="white", width=20)
    #ed2 = Entry(Dentro, textvariable=vIdecli, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=30)

    ed2 = ttk.Combobox(Dentro, values=SelCli(), font=('Arial', 14))
    ed2.bind("<<ComboboxSelected>>", EscCli)

    ed3 = ttk.Combobox(Dentro, values=SelSof(), font=('Arial', 14))
    ed3.bind("<<ComboboxSelected>>", EscSoft)

    #ed4 = Entry(Dentro, textvariable=vNomMod, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=30)

    vSelec = list()
    ed4 = Listbox(Dentro, selectmode=EXTENDED, font=('Arial', 14), bd=2, bg="white", width=30, height=6)
    ed4.grid(row=50, column=1, sticky=W)
    ResMod2 = EscSoft()

    #for nome in ResMod:
    #    lista.insert(END, nome)


    print()

    ed1.focus()
    ed1.bind("<Return>", Ler)

    # Button GRAVAR
    btd = Button(root1, width=10, font=('arial', 10), text="Gravar", state=DISABLED, command=Gravar)
    btd.place(x=480, y=355)

    #Button SAIR
    btd1 = Button(root1, width=10, font=('arial', 10), text="Sair", command=root1.destroy)
    btd1.place(x=15, y=355)

    # Grid
    lb0.grid(row=0, column=0, columnspan=2)
    lb1.grid(row=20, column=0, pady=10, padx=10)
    lb2.grid(row=30, column=0, pady=10, padx=10)
    lb3.grid(row=40, column=0, pady=10, padx=10)
    lb4.grid(row=50, column=0, pady=10, padx=10)
    #lb5.grid(row=60, column=0, pady=10, padx=10)

    ed1.grid(row=20, column=1, sticky=W)
    ed2.grid(row=30, column=1, sticky=W)
    ed3.grid(row=40, column=1, sticky=W)
    #ed4.grid(row=50, column=1, sticky=W)
    #ed5.grid(row=60, column=1, sticky=W)


    # finalizacao da tela do sistema
    root1.mainloop()

#obj = Cadastro('vId', 'vIdent', 'vNome', 'vEnder', 'vContato')