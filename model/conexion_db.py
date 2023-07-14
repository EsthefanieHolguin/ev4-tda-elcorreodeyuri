import pyodbc

class ConexionDB:
    def __init__(self):
        
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER=sqlserver.cjnplcvfcn4g.sa-east-1.rds.amazonaws.com;DATABASE=Yury;UID=admin;PWD=TDA123456.')
        self.cursor = self.connection.cursor()

    
    def cerrar(self):
        self.connection.commit()
        self.connection.close()
        print("La conexión ha finalizado.")
        




