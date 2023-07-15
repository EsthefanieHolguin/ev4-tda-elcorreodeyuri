from .conexionDB import ConexionDB
from tkinter import messagebox


#Query Select
def listarTrabajador():
    conexion = ConexionDB()
    #Arreglo para retonar listado.
    listado_trabajadores = []
    sql = "SELECT * FROM Trabajadores;"
    try:
        cursor=conexion.cursor.execute(sql)   
        print("EJECUTA QUERY SELECT \n")
        listado_trabajadores = cursor.fetchall()
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

#Query Select Carga
def listarCamposCarga(rutTrabajador):
    conexion = ConexionDB()
    #Arreglo para retonar listado.
    sql = "SELECT * FROM CargaFamiliar where rutTrabajador = ?;"
    try:
        cursor=conexion.cursor.execute(sql,rutTrabajador)   
        print("EJECUTA QUERY SELECT CARGA \n")
        camposCarga = cursor.fetchall()
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
    return camposCarga

#Query Select
def listarCamposContacto(rutTrabajador):
    conexion = ConexionDB()
    #Arreglo para retonar listado.
    sql = "SELECT * FROM ContactoEmergencia where rutTrabajador = ?;"
    try:
        cursor=conexion.cursor.execute(sql,rutTrabajador)   
        print("EJECUTA QUERY SELECT CONTACTO\n")
        camposContacto = cursor.fetchall()
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
    return camposContacto

#Query Delete
def eliminarTrabajador():
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

#Query delete
def eliminarTrabajador(rut):
    conexion = ConexionDB()
    sqll ="delete from Trabajadores where RutTrabajador = ?;"
    sql2 ="delete from ContactoEmergencia where RutTrabajador = ?;"
    sql3 ="delete from CargaFamiliar where RutTrabajador = ?;"
    try:
        conexion.cursor.execute(sqll,rut)   
        conexion.commit()
        conexion.cursor.execute(sql2,rut)   
        conexion.commit()
        conexion.cursor.execute(sql3,rut)   
        conexion.commit()
        print(conexion.rowcount,"Registro Eliminado")

    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()


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
        
#Query Insert Carga Trabajadores
def ingresarCargaTrabajador(rutCarga,nombreCarga,rutTrabajador,parentesco,sexoCarga):
    conexion = ConexionDB()
    sql ="insert into Trabajadores values(?,?,?,?,?);"
    #La variable valores tiene que ser una tupla
    #Como minima expresion es: (valor,) la coma hace que sea una tupla
    valores = (rutCarga,nombreCarga,rutTrabajador,parentesco,sexoCarga)
    
    print (sql)
    print(valores)

    try:
        conexion.cursor.execute(sql,valores)   
        print("EJECUTA QUERY INGRESAR CARGA FAMILIAR \n")
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()
        
#Query Insert Carga Trabajadores
def ingresarContactoTrabajador(rutContacto,nombreContacto,rutTrabajador,relacion,telefonoContacto):
    conexion = ConexionDB()
    sql ="insert into Trabajadores values(?,?,?,?,?);"
    #La variable valores tiene que ser una tupla
    #Como minima expresion es: (valor,) la coma hace que sea una tupla
    valores = (rutContacto,nombreContacto,rutTrabajador,relacion,telefonoContacto)
    
    print (sql)
    print(valores)

    try:
        conexion.cursor.execute(sql,valores)   
        print("EJECUTA QUERY INGRESAR CONTACTO TRABAJADOR \n")
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()

#Query Modificar Carga Trabajadores
def modificarDatosTrabajador(rut,nombre,sexo,cargo,fechaingreso,area,departamento,direccion,telefono):
    conexion = ConexionDB()
    sql ="update Trabajadores SET Nombre = ?,SexoTrabajador = ?,CargoTrabajador = ?,FechaIngreso = ?,Area = ? , Departamento=?, Direccion=? , TelefonoTrabajador = ? where RutTrabajador = ? ;"

    valores = (nombre,sexo,cargo,fechaingreso,area,departamento,direccion,telefono,rut)
    
    print (sql)
    print(valores)

    try:
        conexion.cursor.execute(sql,valores)   
        print("EJECUTA QUERY MODIFICAR DATOA TRABAJADOR \n")
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()        
        
#Query Update Contacto
def modificarContactoTrabajador(rutContacto,nombreContacto,rutTrabajador,relacion,telefonoContacto):
    conexion = ConexionDB()
    sql ="update ContactoEmergencia SET RutContacto = ?,NombreContactoEmergencia = ?,RutTrabajador = ?,Relacion = ?,TelefonoContactoEmergencia = ? where RutTrabajador =?;"
    valores = (rutContacto,nombreContacto,rutTrabajador,relacion,telefonoContacto,rutTrabajador)    
    
    print (sql)
    print(valores)

    try:
        conexion.cursor.execute(sql,valores)   
        print("EJECUTA QUERY UPDATE CONTACTO  \n")
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()

#Query Update Carga Trabajadores
def modificarCargaTrabajador(rutCarga,nombreCarga,rutTrabajador,parentesco,sexoCarga):
    conexion = ConexionDB()
    sql ="update CargaFamiliar SET RutCarga = ?,NombreCarga = ?,RutTrabajador = ?,Parentesco = ?,SexoCargaFamiliar = ? where RutTrabajador = ? ;"

    valores = (rutCarga,nombreCarga,rutTrabajador,parentesco,sexoCarga,rutTrabajador)
    
    print (sql)
    print(valores)

    try:
        conexion.cursor.execute(sql,valores)   
        print("EJECUTA QUERY MODIFICAR CARGA FAMILIAR \n")
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()        
        
#para generarquery log        
def logQuery():
    a=" ******************************\n"
    b="*      QUERY FINALIZADA      *\n"
    c="******************************\n"
    print(a,b,c)