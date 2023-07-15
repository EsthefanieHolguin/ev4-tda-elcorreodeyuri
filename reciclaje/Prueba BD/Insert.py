import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=sqlserver.cjnplcvfcn4g.sa-east-1.rds.amazonaws.com;DATABASE=Yury;UID=admin;PWD=TDA123456.')
    consulta = ("Insert into Trabajadores(RutTrabajador, Nombre, SexoTrabajador, CargoTrabajador, FechaIngreso, Area, Departamento, Direccion, TelefonoTrabajador) VALUES('99999999-5','ADMIN2','NA','NA','2023/07/11','RRHH','RRHH','Coyancura 2288','987654321');")
    print("Conexión exitosa.")
    cursor = connection.cursor()
    cursor.execute(consulta)
    cursor.commit()
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()
    print("La conexión ha finalizado.")