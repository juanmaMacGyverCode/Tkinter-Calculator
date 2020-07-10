import os.path
from tkinter import *
from tkinter import messagebox as MessageBox

class Programa:

    ############################

    def __init__(self):
        self.title = "Calculadora Python"
        self.icon = "./imagenes/favicon.ico"
        #self.icon_alt = "./18Tkinter/imagenes/favicon.ico"
        self.size = "300x300"
        self.resizable = True

    def load(self):
        window = Tk()
        self.window = window

        window.title(self.title)
        ruta_icono = os.path.abspath(self.icon)

        #if not os.path.isfile(ruta_icono):
        #    ruta_icono = os.path.abspath(self.icon_alt)

        window.iconbitmap(ruta_icono)
        window.geometry(self.size)

        if self.resizable:
            window.resizable(1, 1)
        else:
            window.resizable(0, 0)

    ###############################################

    def showHeader(self, dato):
        text = Label(self.window, text=dato)
        text.config(
            fg="white",
            bg="#000000",
            width=20,
            padx=0,
            pady=20,
            font=("Consolas", 20)
        )
        text.grid(row=0, columnspan=2)

    def entryFields(self, rowGrid, columnGrid):
        self.dato1 = StringVar()
        self.dato2 = StringVar()

        #Label
        label = Label(self.window, text="Primer dato: ")
        label.grid(row=rowGrid, column=columnGrid, sticky=W, padx=5, pady=5)

        #field text
        field_text = Entry(self.window, textvariable=self.dato1)
        field_text.grid(row=rowGrid, column=columnGrid + 1, columnspan=6, sticky=W, padx=5, pady=5)
        field_text.config(justify="right", state="normal")

        #Label
        label = Label(self.window, text="Segundo dato: ")
        label.grid(row=rowGrid + 1, column=columnGrid, sticky=W, padx=5, pady=5)

        #field text
        field_text = Entry(self.window, textvariable=self.dato2)
        field_text.grid(row=rowGrid + 1, column=columnGrid + 1, columnspan=6, sticky=W, padx=5, pady=5)
        field_text.config(justify="right", state="normal")

    def showResult(self):
        if len(self.result.get()) > 0:
            self.fieldSolve.config(
                bg="green",
                fg="white"
            )

    def isEmpty(self) -> bool:
        return len(self.dato1.get()) == 0 or len(self.dato2.get()) == 0

    def add(self):
        if self.isEmpty():
            MessageBox.showerror("Error", "Some field is empty")
        else:
            self.result.set(int(self.dato1.get()) + int(self.dato2.get()))
            self.showResult()

    def subs(self):

        if self.isEmpty():
            MessageBox.showerror("Error", "Some field is empty")
        else:
            self.result.set(int(self.dato1.get()) - int(self.dato2.get()))
            self.showResult()

    def multiply(self):

        if self.isEmpty():
            MessageBox.showerror("Error", "Some field is empty")
        else:
            self.result.set(int(self.dato1.get()) * int(self.dato2.get()))
            self.showResult()

    def divide(self):

        if self.isEmpty():
            MessageBox.showerror("Error", "Some field is empty")
        else:
            if int(self.dato2.get()) == 0:
                self.result.set("It is not possible to divide by 0")
                self.fieldSolve.config(
                    bg="red",
                    fg="white"
                )
                MessageBox.showerror("Error", "It is not possible to divide by 0")
            else:
                self.result.set(int(self.dato1.get()) / int(self.dato2.get()))
                self.showResult()

    def createOperations(self, rowGrid, columnGrid):

        frame_padre = Frame(self.window, width=300, height=40)
        frame_padre.config(
            bg="lightblue",
        )
        frame_padre.grid(row=rowGrid, columnspan=2)

        button = Button(self.window, text="add", command=self.add)
        button.grid(row=rowGrid, column=0)

        button = Button(self.window, text="subs", command=self.subs)
        button.grid(row=rowGrid, column=1)
        
        frame_padre = Frame(self.window, width=300, height=40)
        frame_padre.config(
            bg="lightblue",
        )
        frame_padre.grid(row=rowGrid+1, columnspan=2)

        button = Button(self.window, text="multiply", command=self.multiply)
        button.grid(row=rowGrid+1, column=0)

        button = Button(self.window, text="divide", command=self.divide)
        button.grid(row=rowGrid+1, column=1)

    def fieldResult(self, rowGrid, columnGrid):
        self.result = StringVar()

        label = Label(self.window, text="Result: ")
        label.grid(row=rowGrid, column=columnGrid, sticky=W, padx=5, pady=5)

        self.fieldSolve = Label(self.window, textvariable=self.result)
        self.fieldSolve.grid(row=rowGrid, column=columnGrid+1, sticky=W, padx=5, pady=5)

    def run(self):
        self.window.mainloop()


programa = Programa()
programa.load()
programa.showHeader("Calculadora Python")
programa.entryFields(1, 0)
programa.createOperations(3, 0)
programa.fieldResult(5, 0)
programa.run()
