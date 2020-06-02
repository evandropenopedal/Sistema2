# importando arquivos da biclioteca
import sqlite3
import sys
import tkinter
from tkinter import messagebox


def conexionBbdd():
    import os.path
    if os.path.exists("CADASTRO"):
        return



    miConexionBbdd = sqlite3.connect('CADASTRO')
    miCursor = miConexionBbdd.cursor()

    miCursor.execute('''
        	  CREATE TABLE CLIENTES ( 
        	    ID INTEGER PRIMARY KEY AUTOINCREMENT,
        	    IDENT VARCHAR(20),
        	    NOME VARCHAR(30),
        	    ENDER VARCHAR(40),
        	    CONTATO VARCHAR(10))''')


    miCursor.execute('''
        	  CREATE TABLE SOFTWARE ( 
        	    ID INTEGER PRIMARY KEY AUTOINCREMENT,
        	    IDENT VARCHAR(20),
        	    NOME VARCHAR(30),
        	    EMPRESA VARCHAR(40),
        	    CONTATO VARCHAR(40))''')


    miCursor.execute('''
        	  CREATE TABLE MODULOS ( 
        	    ID INTEGER PRIMARY KEY AUTOINCREMENT,
        	    SOFT VARCHAR(20),
       	        NOME VARCHAR(30))''')

def conexionBbdd1():
    import os.path
    if os.path.exists("PROPOSTA"):
        return

    miConexionBbdd1 = sqlite3.connect('PROPOSTA')
    miCursor = miConexionBbdd1.cursor()

    miCursor.execute('''
            	  CREATE TABLE PEDIDO ( 
            	    ID INTEGER PRIMARY KEY AUTOINCREMENT,
            	    IDENT VARCHAR(10),
            	    IDECLI VARCHAR(30),
            	    IDESOF VARCHAR(40),
            	    DATA VARCHAR(10),
            	    OBSERV VARCHAR(40))''')

    miCursor.execute('''
                	  CREATE TABLE PEDMOD ( 
                	    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                	    IDPED VARCHAR(10),
                	    NMMODULO VARCHAR(30))''')


def Sair(arg=None):
    valor = tkinter.messagebox.askquestion('Sair', 'Deseja Sair da Aplicação ?')

    if valor == "yes":
        # root.destroy()
        sys.exit(0)



#radiobutton (text, 'Masculino', variable=barOpcion, value=1,
#Chekbutons - Sao opções com quadrados que permite mais de uma opção