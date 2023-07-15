from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pyodbc

root=Tk()
root.title("Login")
root.geometry("500x300")
root.resizable(width=False, height=False)

usuario = Label(root, text="RutTabajador")
usuario.pack()
usuario1 = StringVar()
usu=Entry(root, width=30, textvariable=usuario1)
usu.pack()

contraseña = Label(root, text="Contraseña")
contraseña.pack()

contra= StringVar()
contra1=Entry(root, width=30, textvariable=contra, show="*")
contra1.pack()


def validar():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=sqlserver.cjnplcvfcn4g.sa-east-1.rds.amazonaws.com;DATABASE=Yury;UID=admin;PWD=TDA123456.')
        cursor = connection.cursor()
        cursor.execute("SELECT TipoUsuario FROM UsuarioSistema WHERE RutTrabajador='"+usuario1.get()+"' and Contraseña='"+contra.get()+"'")
        
        if cursor.fetchval():
            messagebox.showinfo("Inicio secion Exitoso","Inicio secion Exitoso")
            cursor.execute("SELECT TipoUsuario FROM UsuarioSistema WHERE RutTrabajador='"+usuario1.get()+"' and Contraseña='"+contra.get()+"'")
            TipoUsuario  = cursor.fetchval()
            if TipoUsuario == "Admin":
                messagebox.showinfo("pagina inicio","Inicio secion Exitoso Admin")
            elif TipoUsuario == "RRHH":
                messagebox.showinfo("pagina inicio","Inicio secion Exitoso RRHH")
            elif TipoUsuario == "Trabajador":
                messagebox.showinfo("pagina inicio","Inicio secion Exitoso Trabajador")

        else:
            messagebox.showwarning("Inicio secion fallido","Rut o contraseña Incorrecto")

    except Exception as ex:
        messagebox.showerror("Error durante la conexión: {}".format(ex))
    finally:
        connection.close()

Button (root, text="Iniciar Sesion", width=30, command = validar).pack()


root.mainloop()
