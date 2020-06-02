# importando arquivos da biclioteca
from tkinter import *
from tkinter import messagebox
import tkinter
import sqlite3
from uteis import *


#objeto
class Cliente:

    def __init__(self, id, ident, nome, ender, contato):

        self.id = id
        self.ident = ident
        self.nome = nome
        self.ender = ender
        self.contato = contato

vnome = "Evandro"
vende = "Rua da paz 22"

cliente1 = Cliente(nome=vnome, ender=vende)
cliente1

var = cliente()

    def Cadastro(arg=None):
        # ---------------- iniciando o objeto da tela
        root = Tk()

        vId = StringVar()
        vIdent = StringVar()
        vNome = StringVar()
        vEnder = StringVar()
        vContato = StringVar()

        # vLiga.configure(state='normal')

        # passando as medidas e configuracoes da tela
        root.geometry("590x300+600+300")
        root.title("Sistema de rootastro")
        root.configure(background='white')

        # criando o frame(tabela) do topo
        # Top = Frame(root, width=600, height=50)
        # Top.pack(side=TOP)

        # RigthP1 - Painel da dieita
        Dentro = Frame(root, width=600, height=400, bg="white")
        Dentro.place(x=0, y=0)
        # Dentro.configure(background='white')

        # Label dentro do frame secundario
        # lb1 = Label(janela, width=15, height=6, bg="red")

        lb0 = Label(Dentro, text="Cadastro de Clientes", font=('Arial', 14), width=53, bg="green")

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
        btd = Button(root, width=10, font=('arial', 10), text="Gravar", state=DISABLED, command=Gravar)
        btd.place(x=480, y=255)

        # Button SAIR
        btd1 = Button(root, width=10, font=('arial', 10), text="Sair", command=Sair1)
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
        root.mainloop()


# -------- criar banco de dados -----------

conexionBbdd()

# ---------------- iniciando o objeto da tela

# def Tela():


root = Tk()

# passando as medidas e configuracoes da tela
root.geometry("1350x900+0+0")
root.title("Sistema")
root.configure(background='#707070')

# criando o frame(tabela) do topo
Top = Frame(root, width=1350, height=600)
Top.pack(side=TOP)

# inserindo o label para titulo do sistema
lblTitulo = Label(Top, font=('arial', 25), text="Sistema de Cadastro", width=72)
lblTitulo.grid(row=0, column=0)
lblTitulo.configure(background='green')

bt1 = Button(root, width=20, font=('arial', 25), text="1 - Movimento")
bt1.place(x=30, y=70)
bt1.configure(background='yellow')

bt2 = Button(root, width=20, font=('arial', 25), text="2 - Cadastro", command=Cadastro)
bt2.place(x=30, y=170)
bt2.configure(background='green')

bt3 = Button(root, width=20, font=('arial', 25), text="3 - Relatório")
bt3.place(x=30, y=270)
bt3.configure(background='blue')

bt4 = Button(root, width=20, font=('arial', 25), text="4 - Sair", command=Sair)
bt4.place(x=30, y=370)
bt4.configure(background='red')

# criando o frame(tabela) da direita
Right = Frame(root, width=900, height=750)
Right.place(x=430, y=70)
Right.configure(background='#909090')

# finalizacao da tela do sistema
# root.mainloop()


root.mainloop()