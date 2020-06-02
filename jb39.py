from tkinter import *

class FrameNome(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label_nome = Label(self, text = "Nome:")
        text_nome = Entry(self)
        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)


root = Tk()
root.geometry("300x200")


def abrir_formulario():
    top = Toplevel()
    top.title("Novo Formulario")
    top.geometry("200x100")
    lb1 = Label(top, text="Label na Nova Janela")
    lb1.pack()
    btDentro = Button(top, text="Sair", command=top.destroy)
    btDentro.pack()

btn = Button(root, text="Novo...", command=abrir_formulario)
btn.pack()

root.mainloop()