from tkinter import *
from uteis import *
import tkinter as tk
from tkinter import ttk


conexionBbdd()


miConexion = sqlite3.connect('CADASTRO')

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM SOFTWARE")

results = [line[2] for line in miCursor]

miConexion.commit()

#-------------------------------

root = Tk()
root.title("Movie Chooser")

def create_widgets(arg=None):
    global checkBoxA, checkBoxB, checkBoxC, results_txt

    Label(root, text="Select all that apply:").grid(row=1, column=0, sticky=W)
    checkBoxA = BooleanVar()

    Checkbutton(root, text="A", variable=checkBoxA, command=update_text).grid(row=2, column=0, sticky=W)

    results_txt = Text(root, width=40, height=5, wrap=WORD)
    results_txt.grid(row=5, column=0, columnspan=3)



def update_text(arg=None):
    likes = ""



    if checkBoxA.get():
        likes += "Contudo do campo\n"

    results_txt.delete(0.0, END)
    results_txt.insert(0.0, likes)




    return(checkBoxA.get())

create_widgets()


#app = Application(root)
root.mainloop()
