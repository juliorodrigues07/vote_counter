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
        self.titulo.grid(row=0, column=3)

        self.criar = Label(master)
        self.criar["text"] = "Nome da eleição:"
        self.criar["font"] = ("Verdana", "15")
        self.criar["bg"] = '#FFFFFF'
        self.criar.grid(row=2, column=0, padx=20, sticky=tk.W, pady=20)

        #
        self.resultado = Button(master, width=4)
        self.resultado["text"] = '1'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=3, column=1, padx=22, pady=22)

        self.resultado = Button(master, width=4)
        self.resultado["text"] = '2'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=3, column=2, padx=22, pady=22)

        self.resultado = Button(master, width=4)
        self.resultado["text"] = '3'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=3, column=3, padx=22, pady=22)

        #
        self.resultado = Button(master, width=4)
        self.resultado["text"] = '4'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=4, column=1, padx=22, pady=22)

        self.resultado = Button(master, width=4)
        self.resultado["text"] = '5'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=4, column=2, padx=22, pady=22)

        self.resultado = Button(master, width=4)
        self.resultado["text"] = '6'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=4, column=3, padx=22, pady=22)

        #

        self.resultado = Button(master, width=4)
        self.resultado["text"] = '7'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=5, column=1, padx=22, pady=22)

        self.resultado = Button(master, width=4)
        self.resultado["text"] = '8'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=5, column=2, padx=22, pady=22)

        self.resultado = Button(master, width=4)
        self.resultado["text"] = '9'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=5, column=3, padx=22, pady=22)

        self.resultado = Button(master, width=4)
        self.resultado["text"] = '0'
        self.resultado["bg"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=6, column=2, padx=22, pady=22)

        # Digitos
        self.resultado = Label(master, width=12)
        self.resultado["bg"] = '#EEEEEE'
        self.resultado["text"] = '12334'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=4, column=6, padx=122, pady=40)

        # Confirma
        self.resultado = Button(master, width=12)
        self.resultado["bg"] = '#008000'
        self.resultado["text"] = '#c2393e'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=6, column=6, padx=122, pady=40)

        # Apaga
        self.resultado = Button(master, width=12)
        self.resultado["bg"] = '#FF0000'
        self.resultado["text"] = 'Apaga'
        self.resultado["font"] = ("Verdana", "25")
        self.resultado.grid(row=6, column=0, sticky=tk.W, padx=20)

root = Tk()
root.attributes('-fullscreen', True)
root['bg'] = 'white'
Application(root)
root.mainloop()
