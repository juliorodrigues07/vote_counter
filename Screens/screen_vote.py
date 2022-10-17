from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 200
        self.segundoContainer.pack(side=LEFT)

        self.imagem = PhotoImage(file=r"../Static/Imgs/download-removebg-preview.png")
        self.imagem_side = Label(self.primeiroContainer, image=self.imagem)
        self.imagem_side.image = self.imagem
        self.imagem_side.place(x=0, y=75)
        self.imagem_side.pack(side=LEFT)

        self.titulo = Label(self.primeiroContainer, text="Vote")
        self.titulo["font"] = ("Arial", "50", "bold")
        self.titulo["fg"] = '#c2393e'
        self.titulo['padx'] = 400
        self.titulo.pack(side=RIGHT)

        self.criar = Button(self.segundoContainer)
        self.criar["text"] = "Votar"
        self.criar["font"] = ("Verdana", "20")
        self.criar["bg"] = '#c2393e'
        self.criar["relief"] = 'flat'
        self.criar["width"] = 40
        self.criar["height"] = 2
        self.criar["command"] = self.segundoContainer.quit
        self.criar.pack(padx=485)


root = Tk()
root.attributes('-fullscreen', True)
Application(root)
root.mainloop()
