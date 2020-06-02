from tkinter import *

class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bg'] = 'green'


root = Tk()
frm1 = MinhaFrame(root).pack()
root.mainloop()