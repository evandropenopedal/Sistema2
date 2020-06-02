# importando arquivos da biclioteca
from tkinter import *
from tkinter import messagebox
import tkinter
import sqlite3
from uteis import *
from sis100 import *
from sis210 import *
from sis220 import *
from sis230 import *


def Men_Cad():

    #rootMenu = Toplevel()

    # passando as medidas e configuracoes da tela
    #root.geometry("490x200+450+200")
    #root.title("Cadastros")
    #root.configure(background='white')

    # RigthP1 - Painel da dieita
    Dentro1 = Frame(root, width=195, height=240, bg="#909090")
    Dentro1.place(x=450, y=170)

    #Dentro1 = Frame(root, width=195, height=400, bg="white")
    #Dentro1.place(x=450, y=170)


    # inserindo o label para titulo do sistema
    #lblTitulo2 = Label(menu1, font=('arial', 25), text="Cadastros", width=10)
    #lblTitulo2.grid(row=5, column=3)
    #lblTitulo2.configure(background='green')

    bt11 = Button(Dentro1, width=10, font=('arial', 24), text="Clientes", command=Cadastro)
    bt11.place(x=0, y=0)
    bt11.configure(background='yellow')

    bt21 = Button(Dentro1, width=10, font=('arial', 24), text="SoftWare", command=Software)
    bt21.place(x=0, y=60)
    bt21.configure(background='green')

    bt31 = Button(Dentro1, width=10, font=('arial', 24), text="Módulos")
    bt31.place(x=0, y=120)
    bt31.configure(background='blue')

    bt41 = Button(Dentro1, width=10, font=('arial', 24), text="Sair")
    bt41.place(x=0, y=180)
    bt41.configure(background='red')



    # finalizacao da tela do sistema
    #rootMenu.mainloop()

def Men_Cad1():

    rootMenu = Toplevel()

    # passando as medidas e configuracoes da tela
    rootMenu.geometry("195x240+450+200")
    rootMenu.title("Cadastros")
    rootMenu.configure(background='white')

    # RigthP1 - Painel da dieita
    Dentro1 = Frame(rootMenu, width=195, height=240, bg="#909090")
    Dentro1.place(x=0, y=0)

    #Dentro1 = Frame(rootMenu, width=195, height=400, bg="white")
    #Dentro1.place(x=450, y=170)


    # inserindo o label para titulo do sistema
    #lblTitulo2 = Label(menu1, font=('arial', 25), text="Cadastros", width=10)
    #lblTitulo2.grid(row=5, column=3)
    #lblTitulo2.configure(background='green')

    bt11 = Button(Dentro1, width=10, font=('arial', 24), text="Clientes", command=Cadastro)
    bt11.place(x=0, y=0)
    bt11.configure(background='yellow')

    bt21 = Button(Dentro1, width=10, font=('arial', 24), text="SoftWare", command=Software)
    bt21.place(x=0, y=60)
    bt21.configure(background='green')

    bt31 = Button(Dentro1, width=10, font=('arial', 24), text="Módulos", command=Modulos)
    bt31.place(x=0, y=120)
    bt31.configure(background='blue')

    bt41 = Button(Dentro1, width=10, font=('arial', 24), text="Sair", command=rootMenu.destroy)
    bt41.place(x=0, y=180)
    bt41.configure(background='red')


#def Software():

#    import sis230


# ---------------- iniciando o objeto da tela
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

bt1 = Button(root, width=20, font=('arial', 25), text="Proposta", command=Proposta)
bt1.place(x=30, y=70)
bt1.configure(background='yellow')

bt2 = Button(root, width=20, font=('arial', 25), text="Cadastro", command=Men_Cad1)
bt2.place(x=30, y=170)
bt2.configure(background='green')

bt3 = Button(root, width=20, font=('arial', 25), text="Relatório")
bt3.place(x=30, y=270)
bt3.configure(background='blue')

bt4 = Button(root, width=20, font=('arial', 25), text="Sair", command=root.destroy)
bt4.place(x=30, y=370)
bt4.configure(background='red')

# criando o frame(tabela) da direita
Right = Frame(root, width=900, height=750)
Right.place(x=430, y=70)
Right.configure(background='#909090')

# finalizacao da tela do sistema
root.mainloop()
