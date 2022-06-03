from distutils.log import debug
from dao.productos_dao import ProductosDAO
from ml_utils.ml_pricile import PrediccionPricile
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Wordl"

# Obtiene todos los registros de la tabla PRODUCTOS
@app.route("/productos", methods=['GET'])
def getAllProductos():
    dao = ProductosDAO()
    if request.method == 'GET':
        return jsonify(dao.listar_productos())

# Obtiene los datos predictivos de los precios de venta
@app.route("/pred-precio")
def predecir_precios():
    dao = ProductosDAO()
    pricile = PrediccionPricile()
    return jsonify(pricile.predecir_precio_venta_producto(dao.listar_productos()))

if __name__ == "__main__":
    app.run(debug=True)