import sys
sys.path.append("../..") 
from inventario.modelos.producto import Producto

class Item:
    def __init__(self, id: int, producto: Producto, cantidad: int) -> None:
        self.id = id,
        self.producto = producto,
        self.cantidad = cantidad


    def __str__(self) -> str:
        return f'(Id.: {self.id}, Producto: {self.producto}, Cantidad: {self.cantidad})'