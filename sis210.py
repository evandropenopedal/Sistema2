# importando arquivos da biclioteca
from tkinter import *
from tkinter import messagebox
import tkinter
import sqlite3
from uteis import *



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
    miConexion = sqlite3.connect('CADASTRO')

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM CLIENTES WHERE IDENT=" + vIdent.get())

    vCliente = miCursor.fetchall()

    vDados = vIdent.get(), vNome.get(), vEnder.get(), vContato.get()

    for cliente in vCliente:
        vNome.set(cliente[2])
        vEnder.set(cliente[3])
        vContato.set(cliente[4])

    ed2.configure(state='normal')
    ed3.configure(state='normal')
    ed4.configure(state='normal')
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




# -------- criar banco de dados -----------

conexionBbdd()

# ---------------- iniciando o objeto da tela

def Cadastro(arg=None):

    # ---------------- iniciando o objeto da tela

    root1 = Toplevel()

    global vId, vIdent, vNome, vEnder, vContato
    global ed1, ed2, ed3, ed4, btd

    vId = StringVar()
    vIdent = StringVar()
    vNome = StringVar()
    vEnder = StringVar()
    vContato = StringVar()

    # vLiga.configure(state='normal')

    # RigthP1 - Painel da dieita


    # passando as medidas e configuracoes da tela
    root1.geometry("590x300+600+300")
    root1.title("Sistema de Cadastro")
    root1.configure(background='white')


    # criando o frame(tabela) do topo
    #Top = Frame(root1, width=600, height=50)
    #Top.pack(side=TOP)


    # RigthP1 - Painel da dieita
    Dentro = Frame(root1, width=600, height=400, bg="white")
    Dentro.place(x=0, y=0)
    # Dentro.configure(background='white')


    # Label dentro do frame secundario
    # lb1 = Label(janela, width=15, height=6, bg="red")

    lb0 = Label(Dentro, text="Cadastro de Clientes", font=('Arial', 14), width=53, bg="yellow")

    lb1 = Label(Dentro, text="CPF: ", font=('Arial', 14), bg="white")
    lb2 = Label(Dentro, text="Nome : ", font=('Arial', 14), width=10, bg="white")
    lb3 = Label(Dentro, text="Endereço: ", font=('Arial', 14), bg="white")
    lb4 = Label(Dentro, text="Contato: ", font=('Arial', 14), bg="white")

    # Entry
    ed1 = Entry(Dentro, textvariable=vIdent, font=('Arial', 14), bd=2, bg="white", width=20)
    ed2 = Entry(Dentro, textvariable=vNome, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=30)
    ed3 = Entry(Dentro, textvariable=vEnder, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=40)
    ed4 = Entry(Dentro, textvariable=vContato, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=10)
    ed1.focus()
    ed1.bind("<Return>", Ler)

    # Button GRAVAR
    btd = Button(root1, width=10, font=('arial', 10), text="Gravar", state=DISABLED, command=Gravar)
    btd.place(x=480, y=255)

    #Button SAIR
    btd1 = Button(root1, width=10, font=('arial', 10), text="Sair", command=root1.destroy)
    btd1.place(x=15, y=255)


    # Grid
    lb0.grid(row=0, column=0, columnspan=2)
    lb1.grid(row=20, column=0, pady=10, padx=10)
    lb2.grid(row=30, column=0, pady=10, padx=10)
    lb3.grid(row=40, column=0, pady=10, padx=10)
    lb4.grid(row=50, column=0, pady=10, padx=10)

    ed1.grid(row=20, column=1, sticky=W)
    ed2.grid(row=30, column=1, sticky=W)
    ed3.grid(row=40, column=1, sticky=W)
    ed4.grid(row=50, column=1, sticky=W)


    # finalizacao da tela do sistema
    root1.mainloop()

#obj = Cadastro('vId', 'vIdent', 'vNome', 'vEnder', 'vContato')