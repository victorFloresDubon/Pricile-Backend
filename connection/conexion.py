from sqlite3 import DatabaseError
import cx_oracle

class ConexionOracle():

    def getConexion(self):
        user = 'CHATBOT'
        password = 'CHATBOT'
        host = '25.79.181.200'
        port = 1521
        dbName = ''
        try:
            url = f'{user}/{password}@{host}:{port}/{dbName}'
            con = cx_oracle.connect(url)
            print(con.version)
        except cx_oracle.DatabaseError as e:
            print("Ocurrió un problema al conectar", e)
        
        return con
        