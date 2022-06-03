from distutils.log import debug
from dao.productos_dao import ProductosDAO
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Wordl"

# Obtiene todos los registros de la tabla PRODUCTOS
@app.route('/productos', methods=['GET'])
def getAllProductos():

    return ProductosDAO.listar_productos()


if __name__ == "__main__":
    app.run(debug=True)