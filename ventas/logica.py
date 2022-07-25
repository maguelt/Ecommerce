from .modelos.factura import Factura
from .modelos.item import Item

class VentasService:
    def __init__(self) -> None:
        self.carrito = []
        

    def agregar_al_carrito(self, item: Item) -> None:
        if item.id == None:
            item.id = len(self.carrito) + 1

        self.carrito.append(item)


    def quitar_del_carrito(self, id: int) -> None:
        for item in self.carrito:
            if item.id == id:
                self.carrito.remove(item)


    def obtener_items_del_carrito(self) -> list:
        return self.carrito


    def facturar(self, cedula_cli: str, nombre_cli: str, email_cli: str) -> bool:
        if len(self.carrito) == 0:
            raise Exception("No exiten productos en el carrito.")

        factura = Factura(cedula_cli, nombre_cli, email_cli, self.carrito)
        factura.guardar()