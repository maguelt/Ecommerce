class Factura:
    def __init__(self, cedula_cli: str, nombre_cli: str, email_cli: str, items: list) -> None:
        self.cedula_cli = cedula_cli,
        self.nombre_cli = nombre_cli,
        self.email_cli = email_cli,        
        self.items = items
        self.estado = 'ACTIVA'
    
    def guardar(self) -> bool:
        # TODO Guardar la factura.
        return True

    def anular(self) -> bool:
        # TODO Anular la factura.
        return True

    def cobrar(self) -> bool:
        # TODO Recibir el pago de la factura.
        return True
    
    def pagar_impuestos(self) -> bool:
        # TODO G
        return True
    
    def __str__(self) -> str:
        return f'(Cédula: {self.cedula_cli}, Nombre: {self.nombre_cli}, Email: {self.email_cli}, Items: {self.items}, Estado: {self.estado})'