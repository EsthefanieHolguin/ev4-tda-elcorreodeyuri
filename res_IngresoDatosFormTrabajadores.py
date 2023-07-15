from Conexion import *

class IngresoTrabajador:

    # def mostrarTrabajadores():
    #     try:
    #         cone = CConexion.ConexionBaseDatos()
    #         cursor = cone.cursor()
    #         cursor.execute("select * from Trabajadores;")
    #         miResultado = cursor.fetchall()
    #         cone.commit()
    #         cone.close()
    #         return miResultado

    #     except mysql.connector.Error as error:
    #         print("Error de despliegue de datos: {}".format(error))



    # def ingresarTrabajador(rut,nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono):

    #     try:
    #         cone = CConexion.ConexionBaseDatos()
    #         cursor = cone.cursor()
    #         sql ="insert into Trabajadores values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    #         #La variable valores tiene que ser una tupla
    #         #Como minima expresion es: (valor,) la coma hace que sea una tupla
    #         valores = (rut,nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono)
    #         cursor.execute(sql,valores)
    #         cone.commit()
    #         print(cursor.rowcount,"Registro Ingresado")
    #         cone.close()

    #     except mysql.connector.Error as error:
    #         print("Error de ingreso de datos: {}".format(error))



    def modificarDatosTrabajador(rut,nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono):

        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql ="update Trabajadores SET Trabajadores.Nombre = %s,Trabajadores.SexoTrabajador = %s,Trabajadores.CargoTrabajador = %s,Trabajadores.FechaIngreso = %s,Trabajadores.Area = %s,Trabajadores.Departamento = %s,Trabajadores.Direccion = %s,Trabajadores.TelefonoTrabajador = %s where Trabajadores.RutTrabajador =%s;"
            valores = (nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono,rut)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de actualización de datos: {}".format(error))


    def eliminarTrabajador(rut):

        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql ="delete from Trabajadores where Trabajadores.RutTrabajador = %s;"
            sql2 ="delete from ContactoEmergencia where ContactoEmergencia.RutTrabajador = %s;"
            sql3 ="delete from CargaFamiliar where CargaFamiliar.RutTrabajador = %s;"
            valores = (rut)
            cursor.execute(sql,valores)
            cone.commit()
            cursor.execute(sql2,valores)
            cone.commit()
            cursor.execute(sql3,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de eliminacion de datos: {}".format(error))



    def ingresarCargaTrabajador(rutCarga,nombreCarga,rutTrabajador,parentesco,sexoCarga):

        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql ="insert into CargaFamiliar values(%s,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla
            #Como minima expresion es: (valor,) la coma hace que sea una tupla
            valores = (rutCarga,nombreCarga,rutTrabajador,parentesco,sexoCarga)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Carga Familiar Ingresada")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de datos de carga familiar: {}".format(error))


    def ingresarContactoTrabajador(rutContacto,nombreContacto,rutTrabajador,relacion,telefonoContacto):

        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql ="insert into ContactoEmergencia values(%s,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla
            #Como minima expresion es: (valor,) la coma hace que sea una tupla
            valores = (rutContacto,nombreContacto,rutTrabajador,relacion,telefonoContacto)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Carga Familiar Ingresada")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de datos de carga familiar: {}".format(error))
            

    def modificarContactoTrabajador(rutContacto,nombreContacto,rutTrabajador,relacion,telefonoContacto):

        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql ="update ContactoEmergencia SET ContactoEmergencia.RutContacto = %s,ContactoEmergencia.NombreContactoEmergencia = %s,ContactoEmergencia.RutTrabajador = %s,ContactoEmergencia.Relacion = %s,ContactoEmergencia.TelefonoContactoEmergencia = %s where Trabajadores.RutTrabajador =%s;"
            valores = (rutContacto,nombreContacto,rutTrabajador,relacion,telefonoContacto)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de actualización de datos: {}".format(error))

    def modificarCargaTrabajador(rutCarga,nombreCarga,rutTrabajador,parentesco,secoCarga):

        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql ="update CargaFamiliar SET CargaFamiliar.RutCarga = %s,CargaFamiliar.NombreCarga = %s,CargaFamiliar.RutTrabajador = %s,CargaFamiliar.Parentesco = %s,CargaFamiliar.SexoCargaFamiliar = %s where Trabajadores.RutTrabajador =%s;"
            valores = (rutCarga,nombreCarga,rutTrabajador,parentesco,secoCarga)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de actualización de datos: {}".format(error))