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

    global textBoxFechaIngreso
    textBoxFechaIngreso =None

    global textBoxAreaTrabajador
    textBoxAreaTrabajador =None

    global textBoxDepartamento
    textBoxDepartamento =None

    global textBoxRutContacto
    textBoxRutContacto =None

    global textBoxNombreContacto
    textBoxNombreContacto =None

    global textBoxRelacionTrabajador
    textBoxRelacionTrabajador =None

    global textBoxTelefonoContacto
    textBoxTelefonoContacto =None

    global textBoxRutCarga
    textBoxRutCarga =None

    global textBoxNombreCarga
    textBoxNombreCarga =None

    global textBoxParentesco
    textBoxParentesco =None

    global comboSexoCarga
    comboSexoCarga =None

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
    global textBoxCargoTrabajador
    global textBoxFechaIngreso
    global textBoxAreaTrabajador
    global textBoxDepartamento
    global textBoxRutContacto
    global textBoxNombreContacto
    global textBoxRelacionTrabajador
    global textBoxTelefonoContacto
    global textBoxRutCarga
    global textBoxNombreCarga
    global textBoxParentesco
    global comboSexoCarga
    global groupBox
    global tree


    try:
        base = Tk()
        base.geometry("1450x800")
        base.title("Ficha Ingreso Trabajador")

        groupBox = LabelFrame(base,text="Datos Personales del Trabajador",padx=5,pady=5)
        groupBox.grid(row=0,column=0,padx=10,pady=10)

        labelRutTrabajador=Label(groupBox,text="RUT:",width=20,font=("arial",11)).grid(row=0,column=0)
        textBoxRutTrabajador = Entry(groupBox)
        textBoxRutTrabajador.grid(row=0,column=1)

        labelNombreTrabajador=Label(groupBox,text="Nombre Completo:",width=20,font=("arial",11)).grid(row=1,column=0)
        textBoxNombreTrabajador = Entry(groupBox)
        textBoxNombreTrabajador.grid(row=1,column=1)

        labelDireccionTrabajador=Label(groupBox,text="Direccion:",width=20,font=("arial",11)).grid(row=2,column=0)
        textBoxDireccionTrabajador = Entry(groupBox)
        textBoxDireccionTrabajador.grid(row=2,column=1)

        labelTelefonoTrabajador=Label(groupBox,text="Telefono:",width=20,font=("arial",11)).grid(row=3,column=0)
        textBoxTelefonoTrabajador = Entry(groupBox)
        textBoxTelefonoTrabajador.grid(row=3,column=1)

        labelSexoTrabajador=Label(groupBox,text="Sexo:",width=20,font=("arial",11)).grid(row=4,column=0)
        seleccionSexo = tk.StringVar()
        comboSexo = ttk.Combobox(groupBox,values=["Masculino","Femenino"," Prefiero no responder"], textvariable=seleccionSexo)
        comboSexo.grid(row=4,column=1)



        groupBox = LabelFrame(base,text="Datos Laborales",padx=5,pady=5)
        groupBox.grid(row=1,column=0,padx=10,pady=10)

        labelCargoTrabajador=Label(groupBox,text="Cargo:",width=20,font=("arial",11)).grid(row=0,column=0)
        textBoxCargoTrabajador = Entry(groupBox)
        textBoxCargoTrabajador.grid(row=0,column=1)

        labelFechaIngreso=Label(groupBox,text="Fecha Ingreso:",width=20,font=("arial",11)).grid(row=1,column=0)
        textBoxFechaIngreso = Entry(groupBox)
        textBoxFechaIngreso.grid(row=1,column=1)

        labelAreaTrabajador=Label(groupBox,text="Area:",width=20,font=("arial",11)).grid(row=2,column=0)
        textBoxAreaTrabajador = Entry(groupBox)
        textBoxAreaTrabajador.grid(row=2,column=1)

        labelDepartamento=Label(groupBox,text="Departamento:",width=20,font=("arial",11)).grid(row=3,column=0)
        textBoxDepartamento = Entry(groupBox)
        textBoxDepartamento.grid(row=3,column=1)



        groupBox = LabelFrame(base,text="Contactos de Emergencia",padx=5,pady=5)
        groupBox.grid(row=2,column=0,padx=10,pady=10)

        labelRutContacto=Label(groupBox,text="RUT Contacto:",width=20,font=("arial",11)).grid(row=0,column=0)
        textBoxRutContacto = Entry(groupBox)
        textBoxRutContacto.grid(row=0,column=1)

        labelNombreContacto=Label(groupBox,text="Nombre Contacto:",width=20,font=("arial",11)).grid(row=1,column=0)
        textBoxNombreContacto = Entry(groupBox)
        textBoxNombreContacto.grid(row=1,column=1)

        labelRelacionTrabajador=Label(groupBox,text="Relación:",width=20,font=("arial",11)).grid(row=2,column=0)
        textBoxRelacionTrabajador = Entry(groupBox)
        textBoxRelacionTrabajador.grid(row=2,column=1)

        labelTelefonoContacto=Label(groupBox,text="Telefono:",width=20,font=("arial",11)).grid(row=3,column=0)
        textBoxTelefonoContacto = Entry(groupBox)
        textBoxTelefonoContacto.grid(row=3,column=1)


        groupBox = LabelFrame(base,text="Cargas Familiares",padx=5,pady=5)
        groupBox.grid(row=3,column=0,padx=10,pady=10)

        labelRutCarga=Label(groupBox,text="RUT:",width=20,font=("arial",11)).grid(row=0,column=0)
        textBoxRutCarga = Entry(groupBox)
        textBoxRutCarga.grid(row=0,column=1)

        labelNombreCarga=Label(groupBox,text="Nombre Completo:",width=20,font=("arial",11)).grid(row=1,column=0)
        textBoxNombreCarga = Entry(groupBox)
        textBoxNombreCarga.grid(row=1,column=1)

        labelParentesco=Label(groupBox,text="Parentesco:",width=20,font=("arial",11)).grid(row=2,column=0)
        textBoxParentesco = Entry(groupBox)
        textBoxParentesco.grid(row=2,column=1)

        labelSexoCarga=Label(groupBox,text="Sexo:",width=20,font=("arial",11)).grid(row=4,column=0)
        seleccionSexoCarga = tk.StringVar()
        comboSexoCarga = ttk.Combobox(groupBox,values=["Masculino","Femenino"," Prefierono responder"], textvariable=seleccionSexoCarga)
        comboSexoCarga.grid(row=4,column=1)

        groupBox = LabelFrame(base,padx=3,pady=3)
        groupBox.grid(row=5,column=0,padx=1,pady=1)
        Button(groupBox,text="Modificar",width=14,command=modificarRegistros).grid(row=0,column=1)
        Button(groupBox,text="Eliminar",width=14,command=eliminarRegistros).grid(row=0,column=2)
        Button(groupBox,text="Limpiar",width=14,command=limpiarCampos).grid(row=0,column=3)
        Button(groupBox,text="Nuevo",width=14,command=nuevoRegistro).grid(row=1,column=1)
        Button(groupBox,text="Guardar Nuevo",width=14,command=guardarRegistros).grid(row=1,column=2)
        Button(groupBox,text="Salir",width=14,command=base.destroy).grid(row=1,column=3)




        groupBox = LabelFrame(base,text="Lista de Trabajadores",padx=5,pady=5)
        groupBox.grid(row=0,column=1,padx=10,pady=10)

        #Crear un Treeview

        #Crea Tabla y Titulos Header 
        tree = ttk.Treeview(groupBox,columns=("Rut","Nombre","Sexo","Cargo","Fecha de Ingreso"),show='headings',height=5,)
        
        #Valores Detalle Tabla
        tree.heading('#1', text='RUT')
        tree.heading('#2', text='NOMBRE')
        tree.heading('#3', text='SEXO')
        tree.heading('#4', text='CARGO')
        tree.heading('#5', text='FECHA DE INGRESO')

        #Campos Detalle Tabla
        tree.column("# 1",anchor=CENTER)
        tree.column("# 2",anchor=CENTER)
        tree.column("# 3",anchor=CENTER)
        tree.column("# 4",anchor=CENTER)
        tree.column("# 5",anchor=CENTER)

        #Agregar los datos a la tabla y Mostrar la tabla
        for row in listarTrabajador():
             tree.insert('', 0, text=row[1], values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
        
        #Ejecutar la función de hacer clic y mostrar los entry
        tree.bind("<<TreeviewSelect>>",seleccionarRegistro)

        tree.pack()

        base.mainloop()

    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))


    
def guardarRegistros():

    global textBoxRutTrabajador,textBoxNombreTrabajador,textBoxDireccionTrabajador,textBoxTelefonoTrabajador,comboSexo,textBoxCargoTrabajador,textBoxFechaIngreso,textBoxAreaTrabajador,textBoxDepartamento,textBoxRutContacto,textBoxNombreContacto,textBoxRelacionTrabajador,textBoxTelefonoContacto,textBoxRutCarga,textBoxNombreCarga,textBoxParentesco,comboSexoCarga,groupBox

    try:
        #verificar si los widgets estan inicializados
        if textBoxRutTrabajador is None or textBoxNombreTrabajador is None or textBoxDireccionTrabajador is None or textBoxTelefonoTrabajador is None or comboSexo is None or textBoxCargoTrabajador is None or textBoxFechaIngreso is None or textBoxAreaTrabajador is None or textBoxDepartamento is None or textBoxRutContacto is None or textBoxNombreContacto is None or textBoxRelacionTrabajador is None or textBoxTelefonoContacto is None or textBoxRutCarga is None or textBoxNombreCarga is None or textBoxParentesco is None or comboSexoCarga is None:
            print("Los widgets no estan inicializados.")
            return
        
        
        rutTrabajador = textBoxRutTrabajador.get()
        nombreTrabajador = textBoxNombreTrabajador.get()
        direccionTrabajador = textBoxDireccionTrabajador.get()
        telefonoTrabajador = textBoxTelefonoTrabajador.get()
        sexoTrabajador = comboSexo.get()
        cargoTrabajador = textBoxCargoTrabajador.get()
        fechaIngreso = textBoxFechaIngreso.get()
        area = textBoxAreaTrabajador.get()
        departamento = textBoxDepartamento.get()

        rutContacto = textBoxRutContacto.get()
        nombreContacto = textBoxNombreContacto.get()
        relacionTrabajador = textBoxRelacionTrabajador.get()
        telefonoContacto = textBoxTelefonoContacto.get()
        rutCarga = textBoxRutCarga.get()
        nombreCarga = textBoxNombreCarga.get()
        parentesco = textBoxParentesco.get()
        sexoCarga = comboSexoCarga.get()

        #Se llama al metodo ingresarTrabajador() para guardar en la tabla Trabajadores, los datos personales
        ingresarTrabajador(rutTrabajador,nombreTrabajador,sexoTrabajador,cargoTrabajador,fechaIngreso,area,departamento,direccionTrabajador,telefonoTrabajador)
        messagebox.showinfo("Información","Los datos personales fueron guardados.")

        #Se llama al metodo ingresarCargaTrabajador() para guardar en la tabla CargaFamiliar los datos respectivos a la carga familiar
        ingresarCargaTrabajador(rutCarga,nombreCarga,rutTrabajador,parentesco,sexoCarga)
        messagebox.showinfo("Información","La carga familiar fue guardada.")

        #Se llama al metodo ingresarContactoTrabajador() para guardar en la tabla ContactoEmergencia los datos de contacto de emergencia del trabajador
        ingresarContactoTrabajador(rutContacto,nombreContacto,rutTrabajador,relacionTrabajador,telefonoContacto)
        messagebox.showinfo("Información","El contacto de emergencia fue guardado.")

        actualizarTreeView()

        #Limpiamos los campos:
        limpiarCampos()

    except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def nuevoRegistro():
        limpiarCampos()
        messagebox.showinfo("Información","Ingrese Nuevo Trabajador y de click en Guardar Nuevo")
#Limpiamos los campos:
def limpiarCampos():
        textBoxRutTrabajador.delete(0,END)
        textBoxNombreTrabajador.delete(0,END)
        textBoxDireccionTrabajador.delete(0,END)
        textBoxTelefonoTrabajador.delete(0,END)
        comboSexo.delete(0,END)
        textBoxCargoTrabajador.delete(0,END)
        textBoxFechaIngreso.delete(0,END)
        textBoxAreaTrabajador.delete(0,END)
        textBoxDepartamento.delete(0,END)
        textBoxRutContacto.delete(0,END)
        textBoxNombreContacto.delete(0,END)
        textBoxRelacionTrabajador.delete(0,END)
        textBoxTelefonoContacto.delete(0,END)
        textBoxRutCarga.delete(0,END)
        textBoxNombreCarga.delete(0,END)
        textBoxParentesco.delete(0,END)
        comboSexoCarga.delete(0,END)

def actualizarTreeView():
     global tree

     try:
          #Borrar los elementos actuales del TreeView
          tree.delete(*tree.get_children())

          #Insertar los nuevos datos en el TreeView
          for row in listarTrabajador():
                tree.insert('', 0, text=row[1], values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
     except ValueError as error:
          print("Error al actualizar la tabla {}".format(error))


def seleccionarRegistro(event):
     try:
          itemSeleccionado = tree.focus()

          if itemSeleccionado:
               #Obtener el PK del elemento seleccionado
               values = tree.item(itemSeleccionado)['values']
               
            #    #Genera Campos Contacto y Carga
            #    rutTrabajador=values[0]
            #    #Agregar los datos a la tabla y Mostrar la tabla
            #    listarCamposContacto(rutTrabajador)
            #    for row in listarCamposContacto:
            #         tree.insert('', 0, text=row[9], values=(row[9],row[10],row[11],row[12]))
                
            #    listarCamposContacto(rutTrabajador)
            #    for row in listarCamposContacto:
            #         tree.insert('', 0, text=row[13], values=(row[14],row[1],row[11],row[12]))

               #Establecer los valores en los Widgets Entry
               limpiarCampos()
               textBoxRutTrabajador.insert(0,values[0])
               textBoxNombreTrabajador.insert(0,values[1])
               comboSexo.set(values[2])
               textBoxCargoTrabajador.insert(0,values[3])
               textBoxFechaIngreso.insert(0,values[4])
               textBoxAreaTrabajador.insert(0,values[5])
               textBoxDepartamento.insert(0,values[6])
               textBoxDireccionTrabajador.insert(0,values[7])
               textBoxTelefonoTrabajador.insert(0,values[8])
            #    textBoxRutContacto.insert(0,values[9])
            #    textBoxNombreContacto.insert(0,values[10])
            #    textBoxRelacionTrabajador.insert(0,values[11])
            #    textBoxTelefonoContacto.insert(0,values[12])
            #    textBoxRutCarga.insert(0,values[13])
            #    textBoxNombreCarga.insert(0,values[14])
            #    textBoxParentesco.insert(0,values[15])
            #    comboSexoCarga.insert(0,values[16])


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))
               
               
               
               
def modificarRegistros():

    global textBoxRutTrabajador,textBoxNombreTrabajador,textBoxDireccionTrabajador,textBoxTelefonoTrabajador,comboSexo,textBoxCargoTrabajador,textBoxFechaIngreso,textBoxAreaTrabajador,textBoxDepartamento,textBoxRutContacto,textBoxNombreContacto,textBoxRelacionTrabajador,textBoxTelefonoContacto,textBoxRutCarga,textBoxNombreCarga,textBoxParentesco,comboSexoCarga,groupBox

    try:
        #verificar si los widgets estan inicializados
        if textBoxRutTrabajador is None or textBoxNombreTrabajador is None or textBoxDireccionTrabajador is None or textBoxTelefonoTrabajador is None or comboSexo is None or textBoxCargoTrabajador is None or textBoxFechaIngreso is None or textBoxAreaTrabajador is None or textBoxDepartamento is None or textBoxRutContacto is None or textBoxNombreContacto is None or textBoxRelacionTrabajador is None or textBoxTelefonoContacto is None or textBoxRutCarga is None or textBoxNombreCarga is None or textBoxParentesco is None or comboSexoCarga is None:
            print("Los widgets no estan inicializados.")
            return
        
        
        rutTrabajador = textBoxRutTrabajador.get()
        nombreTrabajador = textBoxNombreTrabajador.get()
        direccionTrabajador = textBoxDireccionTrabajador.get()
        telefonoTrabajador = textBoxTelefonoTrabajador.get()
        sexoTrabajador = comboSexo.get()
        cargoTrabajador = textBoxCargoTrabajador.get()
        fechaIngreso = textBoxFechaIngreso.get()
        area = textBoxAreaTrabajador.get()
        departamento = textBoxDepartamento.get()
        rutContacto = textBoxRutContacto.get()
        nombreContacto = textBoxNombreContacto.get()
        relacionTrabajador = textBoxRelacionTrabajador.get()
        telefonoContacto = textBoxTelefonoContacto.get()
        rutCarga = textBoxRutCarga.get()
        nombreCarga = textBoxNombreCarga.get()
        parentesco = textBoxParentesco.get()
        sexoCarga = comboSexoCarga.get()

        #Se llama al metodo modificarDatosTrabajador() para actualizar en la tabla Trabajadores, los datos personales
        modificarDatosTrabajador(rutTrabajador,nombreTrabajador,sexoTrabajador,cargoTrabajador,fechaIngreso,area,departamento,direccionTrabajador,telefonoTrabajador)
        messagebox.showinfo("Información","Los datos fueron actualizados")

        #Se llama al metodo modificarContactoTrabajador() para guardar en la tabla ContactoEmergencia, los datos de contacto de emergencia del trabajador
        modificarContactoTrabajador(rutContacto,nombreContacto,rutTrabajador,relacionTrabajador,telefonoContacto)
        messagebox.showinfo("Información","Los datos de contacto de emergencia fueron guardados.")

        #Se llama al metodo modificarCargaTrabajador() para guardar en la tabla CargaFamiliar los datos respectivos a la carga familiar
        modificarCargaTrabajador(rutCarga,nombreCarga,rutTrabajador,parentesco,sexoCarga)
        messagebox.showinfo("Información","La carga familiar fue guardada.")


        actualizarTreeView()

        #Limpiamos los campos:
        limpiarCampos()

    except ValueError as error:
            print("Error al modificar los datos {}".format(error))


def eliminarRegistros():

    global textBoxRutTrabajador,textBoxNombreTrabajador,textBoxDireccionTrabajador,textBoxTelefonoTrabajador,comboSexo,textBoxCargoTrabajador,textBoxFechaIngreso,textBoxAreaTrabajador,textBoxDepartamento,textBoxDepartamento,textBoxRutContacto,textBoxNombreContacto,textBoxRelacionTrabajador,textBoxTelefonoContacto,textBoxRutCarga,textBoxNombreCarga,textBoxParentesco,comboSexoCarga

    try:
        #verificar si los widgets estan inicializados
        if textBoxRutTrabajador is None:

            print("Los widgets no estan inicializados.")
            return
        
        
        rutTrabajador = textBoxRutTrabajador.get()

        eliminarTrabajador(rutTrabajador)
        messagebox.showinfo("Información","Los datos fueron eliminados")

        actualizarTreeView()

        #Limpiamos los campos:
        limpiarCampos()

    except ValueError as error:
            print("Error al modificar los datos {}".format(error))

FormularioT()
