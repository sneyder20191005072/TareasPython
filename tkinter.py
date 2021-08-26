from tkinter import *

Ventana = tkinter.Tk()
Ventana.geometry("400x300")
Ventana.title("Riego Por Goteo")
Ventana.config(bg="green")

etiqueta = Label(
    Ventana,
    text='\nBienvenido\nPara consultar el riego de hoy presione el boton\n\n',
    bg='green',
    font='Times 16')
etiqueta.pack()


def Riego():
    Litros = '\n\n Hoy se regaron 2 litros/por minuto'
    Etiqueta_1 = Label(Ventana, text=Litros, bg='green',
                       font='Times 20').pack()


boton = Button(Ventana, text="Riego Diario", command=Riego)
boton.pack()

Ventana.mainloop()
