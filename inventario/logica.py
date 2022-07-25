from .modelos.inventario import Inventario
from .modelos.producto import Producto

class InventarioService:
    def __init__(self) -> None:
        self.inventario = Inventario()


    def agregar_producto(self, producto: Producto) -> None:
        producto_existente = self.inventario.buscar_producto_por_codigo(producto.codigo)
        if producto_existente == None:
            self.inventario.agregar_producto(producto)
        else:
            raise Exception(f'El producto {producto.codigo} ya existe en el inventario')


    def quitar_producto(self, codigo_producto: str) -> None:
        producto_existente = self.inventario.buscar_producto_por_codigo(codigo_producto)
        if producto_existente == None:
            raise Exception(f'El producto {codigo_producto} no existe en el inventario')
        else:            
            self.inventario.quitar_producto(producto_existente)
    
    
    def obtener_productos(self) -> list:
        return self.inventario.productos

    
    def obtener_producto_por_codigo(self, codigo_producto: str) -> Producto:
        producto_existente = self.inventario.buscar_producto_por_codigo(codigo_producto)
        if producto_existente == None:
            raise Exception(f'El producto {codigo_producto} no existe en el inventario')