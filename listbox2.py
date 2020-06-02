from tkinter import *
#import tkMessageBox

def botao_pressionado():

    indice = listbox.curselection()[0]
    texto = listbox.get(indice)
    print(texto)
    #tkMessageBox.showinfo("Voce clicou em", texto)

root = Tk()

listbox = Listbox(root, selectmode=SINGLE)
for item in ["verde", "amarelo", "azul", "branco"]:
    listbox.insert(END, item)

button = Button(root, text="ok", command=botao_pressionado)

listbox.grid(row=0)
button.grid(row=1)

root.mainloop()
