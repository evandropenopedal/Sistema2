# importando arquivos da biclioteca
from tkinter import *
from tkinter import messagebox
import tkinter
import sqlite3
from uteis import *


def Gravar(arg=None):
    miConexion = sqlite3.connect('CADASTRO')

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM SOFTWARE WHERE IDENT=" + vIdent.get())

    vSoftware = miCursor.fetchall()

    vDados = vIdent.get(), vNome.get(), vEmpresa.get(), vContato.get()

    for soft in vSoftware:
        vNome.set(soft[2])
        vEmpresa.set(soft[3])
        vContato.set(soft[4])

    if not vSoftware:

        miCursor.execute("INSERT INTO SOFTWARE VALUES(NULL,?,?,?,?)", (vDados))
        tkinter.messagebox.showinfo('BBDD', 'Registro inserido com sucesso')

    else:

        miCursor.execute("UPDATE SOFTWARE SET IDENT=?,NOME=?,EMPRESA=?,CONTATO=? WHERE IDENT= " + vIdent.get(), (vDados))

        # tkinter.messagebox.showinfo('BBDD', 'Registro ALTERADO com sucesso')

    miConexion.commit()

    Limpar()

def Ler(arg=None):
    miConexion = sqlite3.connect('CADASTRO')

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM SOFTWARE WHERE IDENT=" + vIdent.get())

    vSoftware = miCursor.fetchall()

    #vDados = vIdent.get(), vNome.get(), vEmpresa.get(), vContato.get()

    for soft in vSoftware:
        vNome.set(soft[2])
        vEmpresa.set(soft[3])
        vContato.set(soft[4])

    #FrameNome.configure(state='normal')

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
    vEmpresa.set('')
    vContato.set('')

    #ed2.configure(state='disabled')
    #ed3.configure(state='disabled')
    #ed4.configure(state='disabled')
    #btd.configure(state='disabled')

    #ed1.focus()

def Sair(arg=None):

    root1.destroy()
    #import sis000


conexionBbdd()

# ----------------


class FrameNome(Frame):
    def __init__(self, parent):
        super().__init__()
        self['width'] = 600
        self['height'] = 400
        #self['bd'] = 2
        self['bg'] = "white"
        #self['relief'] = SOLID



        global ed1, ed2, ed3, ed4, btd

        lb0 = Label(self, text="Cadastro de SofWare", font=('Arial', 14), width=53, bg="green")

        lb1 = Label(self, text="CNPJ / CPF: ", font=('Arial', 14), bg="white")
        lb2 = Label(self, text="Nome : ", font=('Arial', 14), width=10, bg="white")
        lb3 = Label(self, text="Empresa: ", font=('Arial', 14), bg="white")
        lb4 = Label(self, text="Contato: ", font=('Arial', 14), bg="white")

        # Entry
        ed1 = Entry(self, textvariable=vIdent, font=('Arial', 14), bd=2, bg="white", width=20)
        ed2 = Entry(self, textvariable=vNome, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=30)
        ed3 = Entry(self, textvariable=vEmpresa, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=40)
        ed4 = Entry(self, textvariable=vContato, state=DISABLED, font=('Arial', 14), bd=2, bg="white", width=10)
        ed1.focus()
        ed1.bind("<Return>", Ler)

        # Button GRAVAR
        btd = Button(root, width=10, font=('arial', 10), text="Gravar", state=DISABLED, command=Gravar)
        btd.place(x=480, y=255)

        # Button SAIR
        btd1 = Button(root, width=10, font=('arial', 10), text="Sair", command=root.destroy)
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

        #label_nome = Label(self, text = "Nome:")
        #text_nome = Entry(self)
        #label_nome.grid(row=0, column=0)
        #text_nome.grid(row=0, column=1)


#root = Toplevel()
root = Tk()
#root.geometry("300x200")

global vId, vIdent, vNome, vEnder, vContato

vId = StringVar()
vIdent = StringVar()
vNome = StringVar()
vEmpresa = StringVar()
vContato = StringVar()

root.geometry("590x300+600+300")
root.title("Sistema de Cadastro")
root.configure(background='white')

Dentro = FrameNome(root)
Dentro.place(x=600, y=400)

root.mainloop()