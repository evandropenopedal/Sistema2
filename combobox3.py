results  = [
    "January",
    "February",
    "March",
    "April"]

def Gravar():
    print(opcao.get())


root = Tk()

for nome in results:
	#opcao+str(nome) = IntVar()
	cmd = Checkbutton(root, text=nome, variable=opcao.get()).grid(row=l, column=0, sticky='W')

bt = Button(root, text="Gravar", command=Gravar).grid(row=20, column=10, sticky='W')

root.mainloop()