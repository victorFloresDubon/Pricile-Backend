<center><h1>Documentación interna Chatbot Pricille proyecto final Administración de tecnologias de información <h1></center>

## Integrantes:
    Nombre: Augusto Leonel Diaz Peña        Carnet:7690-16-5231
            Victor Guillermo Flores Dubon          7690-17-13943
            Claudia María Isabel Flores Dubon      7690-18-2542  


## Almacenamiento de datos 
 
Para poder almacenar los datos de de los productos del giro del negocio se definio utilizar una base de datos Oracle 11G en la cual se encuentra almacenada 4 tablas:
 
  * **PRODUCTOS** : Almacena los datos de los productos
  * **CLASIFICACIONES** : Almace las clasificaciones definidas  para los productos
  * **PROD_X_CLASIFICACION**: Guarda la clasificacion de los productos
  * **PROMOCIONES**: Almacena las promociones de los productos
  
<center> PRODUCTOS </center>

<center> <image src="./Imagenes/bb1.png"> </center>

<CENTER> CLASIFICACIONES </center>

<center>  <image src="./Imagenes/bb2.png"> </center>

<CENTER> PRODUCTOS POR CLASIFICACION </center>

<center>  <image src="./Imagenes/bb3.png"> </center>

<CENTER> PROMOCIONES </center>

<center>  <image src="./Imagenes/bb4.png"> </center>    

<center><h1><br>Creacion de API en Phyton para el Backend </br></h1></center>

## Clase conexion:

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

# Creamos una clase llamada ProductosDAO para manipular el objeto producto

from connection.conexion import ConexionOracle
from model.productos import Productos
import json

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

# Se manejaran los modelos necesarios

## Modelo productos

class Productos():

    def __init__(self) -> None:
        pass

    def __init__(self, sku, codigo, descripcion, precio_venta, costo):
        self.sku = sku
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_venta = precio_venta
        self.costo = costo

    def serializable(self):
        return {
            "sku": self.sku,
            "codigo": self.codigo,
            "descripcion": self.descripcion,
            "precio_venta": self.precio_venta,
            "costo": self.costo
        }

## Modelo Clasificaciones

class Clasificaciones:

    def __init__(self, clasificacion, descripcion):
        self.clasificacion = clasificacion
        self.descripcion = descripcion
        
## Modelo Promociones

class Promociones():

    def __init__(self) -> None:
        pass

    def __init__(self, sku, descripcion, descuento, tipo, fecha_inicio, fecha_fin):
        self.sku = sku
        self.descripcion = descripcion
        self.descuento = descuento
        self.tipo = tipo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

# Utilidades

## La utilidad ml_pricille nos ayudara para integrar el Machine Learning para poder aplicar inteligecia artificial en la prediccion de de precios.

### Importamos las librerias necesarias  
import pandas as pd  
import numpy as np  
import json  
from sklearn.linear_model import LinearRegression

class PrediccionPricile():

    def predecir_precio_venta_productos(self, productos):
        # Leemos el fichero para nuestro dataset
        precios = pd.DataFrame(productos)

        # Seleccionamos solo los datos numéricos
        datos_numericos = precios.select_dtypes(np.number)

        # Establecemos la columna objetivo
        objetivo = "precio_venta"

        # Establecemos las variables independientes
        independientes = datos_numericos.drop(columns=objetivo).columns

        # Creamos un modelo y lo ajustamos
        modelo = LinearRegression()
        modelo.fit(X=datos_numericos[independientes], y=datos_numericos[objetivo])

        # Creamos un conjunto solo con los datos de precios reales y precios predicción
        precios["precio_prediccion"] = modelo.predict(datos_numericos[independientes])

        resultado = precios.to_json(orient="records")
        parsed = json.loads(resultado)
        


        return parsed

   # Definomos nuestras rutas

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



<center><h1>Node.js</h1></center>
     

## Definimos el servidor

    const ServerConf = {
        url: 'http://localhost:5000'
    }

## Definimos una clase llamada PricilleService  
### Esta clase devolvera un objeto json con los productos almacenamos en la base de datos para mostrarselos al cliente.

    //const { ServerConf } = require("../server/server-conf");
    const HttpClient = require('request')

    class PricilleService {

        async getAllProducts () {
            HttpClient.get(ServerConf.url, (err, response, body) => {
                if(err){
                    return console.dir(err)
                }
        
             console.dir(JSON.parse(body))
            })        
        }

    }


<center><h1>Clase principal que conecta el proyecto con el Bot creado en TELEGRAM</h1></center>

    const TelegramBot = require('node-telegram-bot-api');
    const { options } = require('request');
    const { PricilleService } = require('./service/PricilleService');


    // Token de bot en telegram
    const token = '5490395184:AAGSFLXxZbp2baeO2XDgl0lngkEH1goLSHk';

    const opcionesPricile = [
        ['PRODUCTOS'],
        ['PROMOCIONES'],
        ['CLASIFICACIONES']
    ]

    // Crea una nueva instancia del bot con opción "pooling" para extraer nuevas actualizaciones
    const Pricille = new TelegramBot(token,{
        polling: true
    });

    // Comando "/start"
    Pricille.onText(/\/start/, (msj, match) => {
        var messageId = msj.message_id
        var chatId = msj.chat.id;
        var tipoChat = msj.chat.type;
        console.log(msj);
        // Opciones disponibles
        const opts = {
            reply_to_message_id: messageId,
            reply_markup : JSON.stringify({
                keyboard: [
                    ['PRODUCTOS'],
                    ['PROMOCIONES'],
                    ['CLASIFICACIONES']                            
                ],
                'one_time_keyboard': true            
            })
        }
        // Si el mensaje es del tipo "private", entonces desplegará el texto de bienvenida junto con las opciones
        if(tipoChat=="private"){
            Pricille.sendMessage(chatId, "¡Hola, mi nombre es Pricille! ¿Cómo puedo ayudarte?", opts);
        }
    });

    // Opción PRODUCTOS, lista todos los productos de la base de datos

    Pricille.onText(/\^PRODUCTOS (.*)/, (msj, match) => {
        var messageId = msj.message_id
        var chatId = msj.chat.id;
        var tipoChat = msj.chat.type;

        const resp = match[1]

        const newLocal = PricilleService.getAllProducts();

        Pricille.sendMessage(chatId, newLocal)

    })
