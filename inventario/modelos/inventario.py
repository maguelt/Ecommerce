from .producto import Producto

class Inventario:
    def __init__(self) -> None:
        self.productos = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def buscar_producto_por_codigo(self, codigo_producto: str) -> Producto:
        for producto in self.productos:
            if producto.codigo == codigo_producto:
                return producto
        return None

    def quitar_producto(self, producto: Producto) -> None:
        self.productos.remove(producto)