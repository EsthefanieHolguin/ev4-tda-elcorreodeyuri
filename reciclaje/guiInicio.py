import tkinter
import tkinter as tk
from tkinter import ttk
from model.trabajadorDao import listarTrabajador


def tabla_trabajadores(event = None):
    #Recupera Lista de trabajadores
    lista_trabajadores = listarTrabajador()
    
    #Titulos Header Tabla
    tabla = ttk.Treeview(column=('Rut','Nombre', 'Sexo', 'Cargo'))
    
    #Se define la posición de la ventana donde se mostrará
    tabla.grid(row=4, column=0, columnspan=4)

    
    #Valores Detalle Tabla
    tabla.heading('#0', text='RUT')
    tabla.heading('#1', text='NOMBRE')
    tabla.heading('#2', text='SEXO')
    tabla.heading('#3', text='CARGO')

    #Muestra listado en duro - para debug
    #self.tabla.insert('', 0, text='1', values=('Los vengadores', '2.35', 'Accion'))

    #Iterar lista trabajadores de base de datos
    for t in lista_trabajadores:
            tabla.insert('', 0, text=t[0], values=(t[1],t[2],t[3],t[4]))

#Barra Menú
def barra_menu(root):
    barra_menu = tkinter.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    #Boton Inicio
    menu_inicio=tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    #Salir
    barra_menu.add_separator()
    menu_inicio.add_command(label='Salir', command = root.destroy)

    #Boton Evento  
    menu_evento = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Evento', menu=menu_evento)
    menu_evento.add_command(label='Nuevo')
    menu_evento.add_command(label='Modificar ')
    menu_evento.add_command(label='Eliminar')
    menu_evento.add_command(label='Listar',command=tabla_trabajadores,compound=tk.LEFT)
   
    #Otros    
    barra_menu.add_cascade(label='Consultas', )
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')
    
#Declaracion de Frame    
class Frame(tk.Frame):
    def __init__(self, root =None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.image = tk.PhotoImage(file="img/inicio.png")
        # Insertarla en una etiqueta.
        self.label = ttk.Label(image=self.image)
        # label.pack()        
        self.label.pack()

