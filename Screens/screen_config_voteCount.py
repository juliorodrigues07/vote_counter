from tkinter import *
import tkinter as tk

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.imagem = PhotoImage(file=r"../Static/Imgs/download-removebg-preview.png")
        self.imagem_side = Label(master, image=self.imagem)
        self.imagem_side.image = self.imagem
        self.imagem_side['bg'] = 'white'
        self.imagem_side.grid(row=0, column=0)

        self.titulo = Label(master, text="Vote")
        self.titulo["font"] = ("Arial", "50", "bold")
        self.titulo["fg"] = '#c2393e'
        self.titulo['bg'] = 'white'
        self.titulo.grid(row=0, column=1)

        self.criar = Label(master)
        self.criar["text"] = "Nome da eleição:"
        self.criar["font"] = ("Verdana", "15")
        self.criar["bg"] = '#FFFFFF'
        self.criar.grid(row=2, column=1, padx=20, sticky=tk.W, pady=10)

        self.criar = Entry(master)
        self.criar["bg"] = '#FFFFFF'
        self.criar["font"] = ("Verdana", "15")
        self.criar.grid(row=2, column=1, padx=222)

        self.resultado = Listbox(master)
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=3, column=1, pady=100)


root = Tk()
root.attributes('-fullscreen', True)
root['bg'] = 'white'
Application(root)
root.mainloop()
