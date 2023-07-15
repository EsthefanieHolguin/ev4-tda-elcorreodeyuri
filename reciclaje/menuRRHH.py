import tkinter as tk
from gui.guiRRHH import Frame, barra_menu

def main():
    root = tk.Tk()
    
        
    #Ventana de interfaz de salida
    root.title('EL CORREO DE YURIII')
    root.iconbitmap('img/barra_menu.ico')
    #root.resizable(0,0)      #Cambia el tamaño de la ventana
    barra_menu(root)

    app = Frame(root = root) #cambio

    #Fin de ejecución
    app.mainloop()

if __name__ == '__main__':
    main()  