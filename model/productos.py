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