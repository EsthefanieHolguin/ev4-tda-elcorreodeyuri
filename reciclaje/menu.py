import tkinter as tk
from reciclaje.gui_inicio import Frame, barra_menu
#import model.trabajador_dao as mt
#from gui.gui_listado import Frame, barra_menu
#from gui.gui_nuevo_trabajador import Frame, barra_menu
def main():
    root = tk.Tk()
    
    print("hola")
    
    #Ventana de interfaz de salida
    root.title('EL CORREO DE YURI')
    root.iconbitmap('img/logo.ico')
    #root.resizable(0,0)      #Cambia el tamaño de la ventana
    barra_menu(root)

    app = Frame(root = root)

    #Fin de ejecución
    app.mainloop()

if __name__ == '__main__':
    main()  