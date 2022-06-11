from connection.conexion import ConexionOracle
from model.productos import Productos

class ProductosDAO():

    # Lista todos los registros de la tabla
    def listar_productos(self):
        list_productos = []
        sql = "SELECT * FROM productos"
        try:
            con = ConexionOracle().getConexion()
            cur = con.cursor()

            # Ejecuta la consulta
            cur.execute(sql)
            rows = cur.fetchall()

            # Mapear los datos al modelo
            for i, row in enumerate(rows):
                record = Productos(sku=row[0], codigo=row[1], descripcion=row[2], precio_venta=row[3], costo=row[4])
                # Serializa los registros y los agrega a la lista
                list_productos.append(record.serializable())
        except Exception as e:
            print('Error:'+str(e))
        
        finally:
            if cur:
                cur.close()
            
            if con:
                con.close()
        return list_productos



