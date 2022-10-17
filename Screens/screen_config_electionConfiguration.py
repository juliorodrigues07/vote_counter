from tkinter import *
import tkinter as tk

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.imagem = PhotoImage(file=r"../Static/Imgs/download-removebg-preview.png")
        self.imagem_side = Label(master, image=self.imagem)
        self.imagem_side.image = self.imagem
        self.imagem_side['bg'] = 'white'
        self.imagem_side.grid(row=0, column=0, sticky=tk.W)

        self.titulo = Label(master, text="Vote")
        self.titulo["font"] = ("Arial", "50", "bold")
        self.titulo["fg"] = '#c2393e'
        self.titulo['bg'] = 'white'
        self.titulo.grid(row=0, column=1)

        #
        self.criar = Label(master)
        self.criar["text"] = "Nome da eleição:"
        self.criar["font"] = ("Verdana", "15")
        self.criar["bg"] = '#FFFFFF'
        self.criar.grid(row=3, column=0, padx=20, sticky=tk.W)

        self.criar = Entry(master)
        self.criar["bg"] = '#FFFFFF'
        self.criar["font"] = ("Verdana", "15")
        self.criar.grid(row=3, column=0)

        #
        self.criar = Label(master)
        self.criar["text"] = "Número de cargos:"
        self.criar["font"] = ("Verdana", "15")
        self.criar["bg"] = '#FFFFFF'
        self.criar.grid(row=4, column=0, padx=20, sticky=tk.W, pady=10)

        self.criar = Entry(master)
        self.criar["bg"] = '#FFFFFF'
        self.criar["font"] = ("Verdana", "15")
        self.criar.grid(row=4, column=0, padx=233)

        #
        #
        self.criar = Label(master, pady=22)
        self.criar["text"] = "Cargo:"
        self.criar["font"] = ("Verdana", "15")
        self.criar["bg"] = '#FFFFFF'
        self.criar.grid(row=1, column=1, pady=33)

        self.criar = Entry(master)
        self.criar["bg"] = '#FFFFFF'
        self.criar["font"] = ("Verdana", "15")
        self.criar.grid(row=1, column=2 ,padx=22)

        self.criar = Label(master)
        self.criar["text"] = "Digitos:"
        self.criar["font"] = ("Verdana", "15")
        self.criar["bg"] = '#FFFFFF'
        self.criar.grid(row=2, column=1)

        self.criar = Entry(master)
        self.criar["bg"] = '#FFFFFF'
        self.criar["font"] = ("Verdana", "15")
        self.criar.grid(row=2, column=2, pady=11)

        self.criar = Button(master)
        self.criar["bg"] = '#FFFFFF'
        self.criar["text"] = 'Confirma'
        self.criar["font"] = ("Verdana", "15")
        self.criar.grid(row=3, column=2)


        self.resultado = Listbox(master, width=40, height=20)
        self.resultado["bg"] = '#c2393e'
        self.resultado.grid(row=4, column=2)


root = Tk()
root.attributes('-fullscreen', True)
root['bg'] = 'white'
Application(root)
root.mainloop()
