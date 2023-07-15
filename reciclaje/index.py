from tkinter import *
from tkinter import ttk

class pru:
    def __init__(self, ventana):
        marco=ventana
        marco.title('El correo de YURY')

        marco=LabelFrame(marco, text='RRHH: ')
        marco.grid(row=0, column=0, columnspan=3, pady=20, padx=20)
        #Nombre
        Label(marco, text='Nombre').grid(row=0, column=0)
        Entry(marco).grid(row=0, column=1)

        #Clave
        Label(marco, text='Clave').grid(row=1, column=0)
        Entry(marco, show='*').grid(row=1, column=1)

        #Boton
        ttk.Button(marco, text='Ingresar').grid(row=2, columnspan=2 ) #sticky=W+E abarca de este a oeste


if __name__=='__main__':
    ventana=Tk()
    aplicacion=pru(ventana)
    ventana.mainloop()