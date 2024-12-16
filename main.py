from tkinter import *
from random import *

root = Tk ()
root.geometry("400x400")
root.title('D20')

class Application:
    def generateNumber(self):
            number = randrange(1,20)
            self.label.config(text=f"{number}")

    def __init__(self, master=None):
        self.master = master
        self.label = Label(master, text="Gire o dado", font=("Arial", 20))
        self.label.pack(pady=30)
        self.button = Button(master, text="Girar", command=self.generateNumber, font=("Arial", 20))
        self.button.pack(pady=20)

Application(root)
root.mainloop()