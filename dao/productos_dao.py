from connection.conexion import ConexionOracle
from model.productos import Productos

class ProductosDAO():

    # Lista todos los registros de la tabla
    def listar_productos():
        list_productos = []

        sql = "SELECT * FROM productos"
        try:
            con = ConexionOracle().getConexion()
            cur = con.cursor()

            # Ejecuta la consulta
            cur.execute(sql)
            rows = cur.fetchAll()

            # Mapear los datos al modelo
            for i in rows:
                record = Productos(sku=rows[0], codigo=rows[1], descripcion=rows[3], precio_venta=rows[4], costo=rows[5])
                list_productos.append(record)

        except Exception as e:
            print('Error:'+str(e))
        
        finally:
            if cur:
                cur.close()
            
            if con:
                con.close()
        
        return list_productos



