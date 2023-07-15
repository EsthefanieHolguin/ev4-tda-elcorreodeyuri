import tkinter
import tkinter as tk
from tkinter import ttk
from model.trabajadorDao import listarTrabajador


def barra_menu(root):
    barra_menu = tkinter.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio=tk.Menu(barra_menu, tearoff=0)
    menu_inicio2=tk.Menu(barra_menu, tearoff=0) #
    
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    barra_menu.add_cascade(label='RRHH', menu=menu_inicio2) #


    menu_inicio.add_command(label='Crear registro en DB')
    menu_inicio.add_command(label='Eliminar registro en DB')
    menu_inicio.add_command(label='Salir', command = root.destroy)

    menu_inicio2.add_command(label='Busqueda por Genero') #Aqui
    menu_inicio2.add_command(label='Busqueda por Cargo') #Aqui
    menu_inicio2.add_command(label='Busqueda por Area') #Aqui
    menu_inicio2.add_command(label='Busqueda por Depa') #Aqui
    menu_inicio2.add_command(label='Salir', command=root.destroy) #

    #barra_menu.add_cascade(label='RRHH Consultas', )
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')

    
#Declaracion de Frame    
class Frame(tk.Frame):
    def __init__(self, root =None):
        super().__init__(root, width=300, height=300)
        self.root = root
        self.pack()
        self.config(bg='green')
        #Listar trabajadores
        self.tabla_trabajadores()
        
    def tabla_trabajadores(self):
        #Recupera Lista de trabajadores
        self.lista_trabajadores = listarTrabajador()        
        #Titulos Header Tabla
        self.tabla = ttk.Treeview(self, column=('Rut','Nombre', 'Sexo', 'Cargo', 'Fecha_Ingreso', 'Area', 'Departamento', 'Direccion', 'Telefono'))        
        #Se define la posición de la ventana donde se mostrará
        self.tabla.grid(row=4, column=0, columnspan=4)        
        #Valores Detalle Tabla
        self.tabla.heading('#0', text='RUT')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='SEXO')
        self.tabla.heading('#3', text='CARGO')
        self.tabla.heading('#4', text='FECHA INGRESO')
        self.tabla.heading('#5', text='AREA')
        self.tabla.heading('#6', text='DEPARTAMENTO')
        self.tabla.heading('#7', text='DIRECCION')
        self.tabla.heading('#8', text='TELEFONO')

        #Muestra listado en duro - para debug
        #self.tabla.insert('', 0, text='1', values=('Los vengadores', '2.35', 'Accion'))

        #Iterar lista trabajadores de base de datos
        for t in self.lista_trabajadores:
             self.tabla.insert('', 0, text=t[0], values=(t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8])) 
