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