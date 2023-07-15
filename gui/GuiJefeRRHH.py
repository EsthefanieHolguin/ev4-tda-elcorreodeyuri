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
        base.title("Seleeción Trabajadores ")

        groupBox = LabelFrame(base,text="Filtros",font='courier 10',padx=10,pady=10)
        groupBox.grid(row=0,column=0,padx=10,pady=10)

        labelSexoTrabajador=Label(groupBox,text="Sexo:",width=20).grid(row=0,column=0)
        seleccionSexo = tk.StringVar()
        comboSexo = ttk.Combobox(groupBox,values=["Masculino","Femenino"," Prefierono responder"], textvariable=seleccionSexo)
        comboSexo.grid(row=1,column=0)
        
        labelCargoTrabajador=Label(groupBox,text="Cargo:",width=20).grid(row=0,column=1)
        seleccionCargo = tk.StringVar()
        comboCargo = ttk.Combobox(groupBox,values=["Ejecutivo","RRHH","Jefe RRHH"], textvariable=seleccionCargo)
        comboCargo.grid(row=1,column=1)

        labelAreaTrabajador=Label(groupBox,text="Área:",width=20).grid(row=0,column=2)
        seleccionArea = tk.StringVar()
        comboArea = ttk.Combobox(groupBox,values=["RRHH","Producción"], textvariable=seleccionArea)
        comboArea.grid(row=1,column=2)
        
        groupBox.grid(row=0,column=0,padx=1,pady=1)
        Button(groupBox,text="Aplicar",width=10,command=limpiarCampos,padx=1,pady=1).grid(row=2,column=0)
        Button(groupBox,text="Limpiar",width=10,command=limpiarCampos).grid(row=2,column=1)
        Button(groupBox,text="Salir",width=10,command=base.destroy).grid(row=2,column=2)
        
        labelDepartamentoTrabajador=Label(groupBox,text="Departamento:",width=20).grid(row=0,column=3)
        seleccionDepartamento = tk.StringVar()
        comboDepartamento = ttk.Combobox(groupBox,values=["RRHH","Producción"], textvariable=seleccionDepartamento)
        comboDepartamento.grid(row=1,column=3)
       
        groupBox = LabelFrame(base,padx=10,pady=10)


        groupBox = LabelFrame(base,text="Lista de Trabajadores",font='Courier 11', padx=10,pady=10)
        groupBox.grid(row=3,column=0,padx=10,pady=10)

        #Crear un Treeview

        #Crea Tabla y Titulos Header 
        tree = ttk.Treeview(groupBox,columns=("Rut","Nombre","Sexo","Cargo"),show='headings',height=4,)
        
        #Valores Detalle Tabla
        tree.heading('#1', text='RUT')
        tree.heading('#2', text='NOMBRE')
        tree.heading('#3', text='SEXO')
        tree.heading('#4', text='CARGO')

        #Campos Detalle Tabla
        tree.column("# 1",anchor=CENTER)
        tree.column("# 2",anchor=CENTER)
        tree.column("# 3",anchor=CENTER)
        tree.column("# 4",anchor=CENTER)

        #Agregar los datos a la tabla y Mostrar la tabla
        for row in listarTrabajador():
             tree.insert('', 0, text=row[1], values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
        
        tree.pack()

        base.mainloop()

    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))

def nuevoRegistro():
        limpiarCampos()
        messagebox.showinfo("Información","Ingrese Nuevo Trabajador y de click en Guardar Nuevo")
#Limpiamos los campos:
def limpiarCampos():
        comboSexoCarga.delete(0,END)
        comboCargoCarga.delete(0,END)
        comboAreaCarga.delete(0,END)
        comboDptoCarga.delete(0,END)

FormularioT()
