class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f'(Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio})'