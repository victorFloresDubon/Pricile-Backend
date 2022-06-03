import pandas as pd
import numpy as np
import json
from sklearn.linear_model import LinearRegression

class PrediccionPricile():

    def predecir_precio_venta_producto(self, productos):
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



