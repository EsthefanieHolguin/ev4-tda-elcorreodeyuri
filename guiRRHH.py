import tkinter
import tkinter as tk
from tkinter import ttk
from trabajador_dao import listar


def barra_menu(root):
    barra_menu = tkinter.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio=tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear registro en DB')
    menu_inicio.add_command(label='Eliminar registro en DB')
    menu_inicio.add_command(label='Salir', command = root.destroy)
    barra_menu.add_cascade(label='Consultas', )
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')
    
#Declaracion de Frame    
class Frame(tk.Frame):
    def _init_(self, root =None):
        super()._init_(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg='green')
        #Listar trabajadores
        self.tabla_trabajadores()
        
    def tabla_trabajadores(self):
        #Recupera Lista de trabajadores
        self.lista_trabajadores = listar()
        
        #Titulos Header Tabla
        self.tabla = ttk.Treeview(self, column=('Sexo','Cargo', 'Area', 'Departamento'))
        
        #Se define la posición de la ventana donde se mostrará
        self.tabla.grid(row=4, column=0, columnspan=4)

        
        #Valores Detalle Tabla
        self.tabla.heading('#0', text='Sexo')
        self.tabla.heading('#1', text='Cargo')
        self.tabla.heading('#2', text='Area')
        self.tabla.heading('#3', text='Departamento')

        #Muestra listado en duro - para debug
        #self.tabla.insert('', 0, text='1', values=('Los vengadores', '2.35', 'Accion'))**

        #Iterar lista trabajadores de base de datos
        for t in self.lista_trabajadores:
             self.tabla.insert('', 0, text=t[0], values=(t[1],t[2],t[3]))