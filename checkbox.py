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



class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Select all that apply:").grid(row=1, column=0, sticky=W)

        self.checkBoxA = BooleanVar()
        Checkbutton(self,
                    text="A",
                    variable=self.checkBoxA,
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)

        self.checkBoxB = BooleanVar()
        Checkbutton(self,
                    text="B",
                    variable=self.checkBoxB,
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        self.checkBoxC = BooleanVar()
        Checkbutton(self,
                    text="C",
                    variable=self.checkBoxC,
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)

        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        likes = ""

        if self.checkBoxA.get():
            likes += "A\n"

        if self.checkBoxB.get():
            likes += "B\n"

        if self.checkBoxC.get():
            likes += "C"

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)


root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()

#------------------------------------------------

# creating root
root = Tk()

# label text
Label(root, text='Select Programming language of your choice').place(x=20, y=0)

# check buttons
java = Checkbutton(root, text='Java',
                   takefocus=0).place(x=40, y=30)

cpp = Checkbutton(root, text='C++',
                  takefocus=0).place(x=40, y=50)

python = Checkbutton(root, text='Python',
                     takefocus=0).place(x=40, y=70)

c = Checkbutton(root, text='C',
                takefocus=0).place(x=40, y=90)

root.mainloop()
#-----------------------------------------------------


# root
root = Tk()

# This will depict the features of Simple Checkbutton
Label(root, text='Simple Checkbutton').place(x=10, y=10)
chkbtn1 = Checkbutton(root, text='Checkbutton1',
                      takefocus=0).place(x=10, y=40)
chkbtn2 = Checkbutton(root, text='Checkbutton2',
                      takefocus=0).place(x=10, y=60)

# This will depict the features of ttk.Checkbutton
Label(root, text='ttk.Checkbutton').place(x=140, y=10)
chkbtn1 = ttk.Checkbutton(root, text='Checkbutton1',
                          takefocus=0).place(x=140, y=40)
chkbtn2 = ttk.Checkbutton(root, text='Checkbutton2',
                          takefocus=0).place(x=140, y=60)

root.mainloop()

#--------------------------------
import wx

class CheckBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Checkbox Example', size=(150, 200))
        panel = wx.Panel(self, -1)
        wx.CheckBox(panel, -1, "A", (35, 40), (150, 20))
        wx.CheckBox(panel, -1, "B", (35, 60), (150, 20))
        wx.CheckBox(panel, -1, "C", (35, 80), (150, 20))

app = wx.PySimpleApp()
CheckBoxFrame().Show()
app.MainLoop()