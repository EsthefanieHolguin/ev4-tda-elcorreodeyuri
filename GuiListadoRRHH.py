#https://www.youtube.com/watch?v=Ro2m95m8QkI&ab_channel=SinRuedaTecnológica

import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#from Conexion import *
#from IngresoDatosFormTrabajadores import *
from model.trabajadorDao import *


class FormularioTrabajadores:

    global base
    base =None

    global textBoxRutTrabajador
    textBoxRutTrabajador =None

    global textBoxNombreTrabajador
    textBoxNombreTrabajador =None

    global textBoxDireccionTrabajador
    textBoxDireccionTrabajador =None

    global textBoxTelefonoTrabajador
    textBoxTelefonoTrabajador =None

    global comboSexo
    comboSexo =None

    global textBoxCargoTrabajador
    textBoxCargoTrabajador =None

    global textBoxDepartamento
    textBoxDepartamento =None

    global textBoxRutCarga
    textBoxRutCarga =None

    global textBoxNombreCarga
    textBoxNombreCarga =None

    global comboSexoCarga
    comboSexoCarga =None
    
    global comboCargoCarga
    comboCargoCarga =None
    
    global comboAreaCarga
    comboAreaCarga =None
    
    global comboDptoCarga
    comboDptoCarga =None    

    global groupBox
    groupBox =None

    global tree
    tree =None



def FormularioT():

    global base
    global textBoxRutTrabajador
    global textBoxNombreTrabajador
    global textBoxDireccionTrabajador
    global textBoxTelefonoTrabajador
    global comboSexo
    global comboCargo
    global textBoxCargoTrabajador
    global textBoxAreaTrabajador
    global textBoxDepartamento
    global textBoxRutCarga
    global textBoxNombreCarga
    global comboSexoCarga
    global comboCargoCarga
    global groupBox
    global tree


    try:
        base = Tk()
        base.geometry("1200x500")
        base.title("Selección Trabajadores ")

        #Crear un Treeview

        lista_trabajadores = listarTrabajador()
        
        #Titulos Header Tabla
        tabla = ttk.Treeview(column=('Rut','Nombre', 'Sexo', 'Cargo'))
        
        #Se define la posición de la ventana donde se mostrará
        tabla.grid(row=0, column=0, columnspan=4)

        
        #Valores Detalle Tabla
        tabla.heading('#0', text='RUT')
        tabla.heading('#1', text='NOMBRE')
        tabla.heading('#2', text='SEXO')
        tabla.heading('#3', text='CARGO')

        #Iterar lista trabajadores de base de datos
        for t in lista_trabajadores:
             tabla.insert('', 0, text=t[0], values=(t[1],t[2],t[3],t[4]))
        
        tabla.pack()

        base.mainloop()

    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))

FormularioT()
