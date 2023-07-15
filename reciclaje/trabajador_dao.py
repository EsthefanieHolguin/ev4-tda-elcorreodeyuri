from reciclaje.conexion_db import ConexionDB
from tkinter import messagebox


#Query Select
def listar():
    conexion = ConexionDB()
    #Arreglo para retonar listado.
    listado_trabajadores = []
    sql = "SELECT * FROM Trabajadores;"
    try:
        cursor=conexion.cursor.execute(sql)   
        print("EJECUTA QUERY SELECT \n")
        listado_trabajadores = cursor.fetchall()
    # #Imprime listado en el log- para debug
    #     for row in rows:
    #         print(row)
          
    
    except Exception as ex:
        #Imprime error por pantalla
        print("Error durante la conexión: {}".format(ex))
        #Messagge Box para usuario
        titulo='Conexion al registro'
        mensaje='Revisar la tabla en la base de datos'
        messagebox.showwarning(titulo,mensaje)
    finally:
        conexion.cerrar()
        logQuery()
    return listado_trabajadores

#Query Insert
def ingresarTrabajador(rut,nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono):
    conexion = ConexionDB()
    #sql = "Insert into Trabajadores(RutTrabajador, Nombre, SexoTrabajador, CargoTrabajador, FechaIngreso, Area, Departamento, Direccion,TelefonoTrabajador)    VALUES('2222-9','ADMIN2','NA','NA','2023/07/11','RRHH''RRHH','Coyancura 2288',    '987654321');"
    sql ="insert into Trabajadores values(?,?,?,?,?,?,?,?,?);"
    valores = (rut,nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono)
    
    print (sql)
    print(valores)

    try:
        conexion.cursor.execute(sql,valores)   
        print("EJECUTA QUERY INSERT \n")
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()
        
#Query Delete
def eliminar():
    conexion = ConexionDB()
    sql = "delete from Trabajadores where RutTrabajador = '2222-9';"
    try:
        conexion.cursor.execute(sql)   
        print("EJECUTA QUERY ELIMINAR \n")
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()

def logQuery():
    a=" ******************************\n"
    b="*      QUERY FINALIZADA      *\n"
    c="******************************\n"
    print(a,b,c)



