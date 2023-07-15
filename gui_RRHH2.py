import tkinter
import tkinter as tk
from tkinter import ttk
from trabajador_dao import listar
import pyodbc #


def barra_menu(root):
    barra_menu = tkinter.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    menu_inicio2 = tk.Menu(barra_menu, tearoff=0)
    
    barra_menu.add_cascade(label='INICIO', menu=menu_inicio)
    barra_menu.add_cascade(label='RRHH', menu=menu_inicio2)


    menu_inicio.add_command(label='Crear registro en DB')
    menu_inicio.add_command(label='Eliminar registro en DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    menu_genero=tk.Menu(menu_inicio2, tearoff=0)
    menu_inicio2.add_cascade(label='Busqueda por Genero', menu=menu_genero)
    menu_genero.add_command(label='Femenino', command=lambda: mostrar_trabajadores(frame, 'Femenino'))
    menu_genero.add_command(label='Masculino', command=lambda: mostrar_trabajadores(frame, 'Masculino'))
    menu_genero.add_command(label='NA', command=lambda: mostrar_trabajadores(frame, 'NA'))

    menu_cargo=tk.Menu(menu_inicio2, tearoff=0)
    menu_inicio2.add_cascade(label='Busqueda por Cargo', menu=menu_cargo)
    menu_cargo.add_command(label='Ejecutivos', command=lambda: mostrar_trabajadores(frame, 'Ejecutivos'))
    menu_cargo.add_command(label='Directorio', command=lambda: mostrar_trabajadores(frame, 'Directorio'))
    menu_cargo.add_command(label='Administracion', command=lambda: mostrar_trabajadores(frame, 'Administracion'))

    menu_area=tk.Menu(menu_inicio2, tearoff=0)
    menu_inicio2.add_cascade(label='Busqueda por Area', menu=menu_area)
    menu_area.add_command(label='TI', command=lambda: mostrar_trabajadores(frame, 'TI'))
    menu_area.add_command(label='RRHH', command=lambda: mostrar_trabajadores(frame, 'RRHH'))

    menu_departamento=tk.Menu(menu_inicio2, tearoff=0)
    menu_inicio2.add_cascade(label='Busqueda por Departamento', menu=menu_departamento)
    menu_departamento.add_command(label='Desarrollo', command=lambda: mostrar_trabajadores(frame, 'Desarrollo'))
    menu_departamento.add_command(label='RRHH', command=lambda: mostrar_trabajadores(frame, 'RRHH'))

    menu_inicio2.add_command(label='Salir', command=root.destroy)

    
    barra_menu.add_cascade(label='AYUDA')


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg='green')
        self.tabla_trabajadores()

    def tabla_trabajadores(self):
        self.tabla = ttk.Treeview(self, column=('Rut', 'Nombre', 'Sexo', 'Cargo', 'Fecha_Ingreso', 'Area', 'Departamento', 'Direccion', 'Telefono'))
        self.tabla.grid(row=4, column=0, columnspan=4)
        self.tabla.heading('#0', text='RUT')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='SEXO')
        self.tabla.heading('#3', text='CARGO')
        self.tabla.heading('#4', text='FECHA INGRESO')
        self.tabla.heading('#5', text='AREA')
        self.tabla.heading('#6', text='DEPARTAMENTO')
        self.tabla.heading('#7', text='DIRECCION')
        self.tabla.heading('#8', text='TELEFONO')

    def mostrar_trabajadores(self, lista_trabajadores):
        for t in lista_trabajadores:
            self.tabla.insert('', 0, text=t[0], values=(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8]))


#def mostrar_trabajadores(frame): ***

def mostrar_trabajadores(frame, genero):
    # Realizar consulta a la base de datos
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=sqlserver.cjnplcvfcn4g.sa-east-1.rds.amazonaws.com;DATABASE=Yury;UID=admin;PWD=TDA123456.')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Trabajadores WHERE Sexo Trabajador = '{genero}'")
    lista_trabajadores = cursor.fetchall()
    
    #lista_trabajadores = listar()  ***
    #     
    # Limpiar tabla antes de mostrar nuevos datos
    frame.tabla.delete(*frame.tabla.get_children())
    
    # Mostrar los trabajadores en la tabla
    frame.mostrar_trabajadores(lista_trabajadores)

    cursor.close() #***
    conn.close() #***



