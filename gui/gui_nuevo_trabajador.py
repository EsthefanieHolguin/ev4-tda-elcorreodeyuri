import tkinter
import tkinter as tk
from tkinter import ttk
#from model.trabajador_dao import listar


def barra_menu(root):
    barra_menu = tkinter.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio=tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear registro en DB')
    menu_inicio.add_command(label='Eliminar registro en DB')
    menu_inicio.add_command(label='Salir', command = root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')
    
#Declaracion de Frame    
class Frame(tk.Frame):
    def __init__(self, root =None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
       # self.config(bg='green')

    #Listar trabajadores
        self.tabla_trabajadores()

    def campos_trabajadores(self):
        #Label Nombre Completo
        self.label_nombre = tk.Label(self, text='Nombre Completo ')
        self.label_nombre.config(font= ('Arial', 12, 'bold'), bg='white')
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        #Label Rut
        self.label_rut = tk.Label(self, text='Rut Trabajador: ')
        self.label_rut.config(font=('Arial', 12, 'bold'), bg='white')
        self.label_rut.grid(row=1, column=0, padx=10, pady=10)
        #Label Sexo
        self.label_sexo = tk.Label(self, text='Sexo: ')
        self.label_sexo.config(font=('Arial', 12, 'bold'), bg='white')
        self.label_sexo.grid(row=1, column=0, padx=10, pady=10)
        #Label Dirección
        self.label_dir = tk.Label(self, text='Sexo: ')
        self.label_dir.config(font=('Arial', 12, 'bold'), bg='white')
        self.label_dir.grid(row=1, column=0, padx=10, pady=10)
        #Label Teléfono
        self.label_tel = tk.Label(self, text='Sexo: ')
        self.label_tel.config(font=('Arial', 12, 'bold'), bg='white')
        self.label_tel.grid(row=1, column=0, padx=10, pady=10)
                
        #Entrada Nombre Completo
        self.ent_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable= self.ent_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        #Entrada Rut
        self.ent_rut = tk.StringVar()
        self.entry_rut = tk.Entry(self, textvariable= self.ent_rut)
        self.entry_rut.config(width=50, font=('Arial', 12))
        self.entry_rut.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        #Entrada Sexo
        self.ent_dir = tk.StringVar()
        self.entry_dir = tk.Entry(self, textvariable= self.ent_dir)
        self.entry_dir.config(width=50, font=('Arial', 12))
        self.entry_dir.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
        #Entrada Teléfono
        self.ent_tel = tk.StringVar()
        self.entry_tel = tk.Entry(self, textvariable= self.ent_tel)
        self.entry_tel.config(width=50, font=('Arial', 12))
        self.entry_tel.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
        
        #Botones
        self.boton_nuevo= tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', activebackground='white')
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='yellow')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='turquoise', cursor='hand2', activebackground='pink')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)


    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='disable')
        self.entry_duracion.config(state='disable')
        self.entry_genero.config(state='disable')

        self.boton_guardar.config(state='disable')
        self.boton_cancelar.config(state='disable')

    def guardar_datos(self):

        self.deshabilitar_campos()

    def tabla_trabajadores(self):

        self.tabla = ttk.Treeview(self, column=('Nombre', 'Edad', 'Genero'))
        self.tabla.grid(row=4, column=0, columnspan=4)  #columnspan significa que usa 4 columnas

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='EDAD')
        self.tabla.heading('#3', text='GENERO')

        self.tabla.insert('', 0, text='1', values=('Los vengadores', '2.35', 'Accion'))

        #Boton Editar

        self.boton_editar = tk.Button(self, text='Editar')
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', activebackground='white')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        #Boton Eliminar

        self.boton_eliminar = tk.Button(self, text='Eliminar')
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', activebackground='white')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)