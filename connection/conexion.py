from sqlite3 import DatabaseError
import cx_Oracle

# Clase para manejar la conexión a la base de datos
class ConexionOracle():

    def getConexion(self):
        user = 'CHATBOT'
        password = 'CHATBOT'
        host = '25.79.181.200'
        port = 1521
        dbName = 'xe'
        try:
            con = cx_Oracle.connect(f'{user}/{password}@{host}:{port}/{dbName}')
            print(con.version)
        except cx_Oracle.DatabaseError as e:
            print("Ocurrió un problema al conectar", e)
        
        return con
        