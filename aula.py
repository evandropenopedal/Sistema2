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