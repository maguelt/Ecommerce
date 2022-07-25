from inventario.modelos.producto import Producto

def mostrar_mensaje(mensaje: str) -> None:
    print()
    print(mensaje)


def mostrar_menu(titulo: str, instruccion: str, menu: dict) -> None:    
    print()
    print(titulo.upper())    
    print(instruccion)
    print()

    for key, value in menu.items():
        print(f' {key} = {value}')


def capturar_opcion_menu(opciones_permitidas: list) -> str:
    while True:
        print()
        opcion = input('Ingrese la opción >> ').strip().upper()

        if opcion not in opciones_permitidas:
            print('Opción inválida. Las opciones permitidas son: [' + ', '.join(opciones_permitidas) + ']. Intente de nuevo!')
            continue
        else:
            return opcion


def capturar_texto(instruccion: str) -> str:
    return input(f'{instruccion}')


def capturar_numero(instruccion: str) -> float:
    while True:
        try:
            return float(input(f'{instruccion}'))
        except ValueError:
            print('Debe digitar un número válido. Intente de nuevo.')


def capturar_producto() -> Producto:
    print()
    codigo = input("Ingrese el código: ").strip().upper()
    nombre = input("Ingrese el nombre: ").strip()
    precio = capturar_numero("Ingrese el precio: ")

    return Producto(codigo, nombre, precio)


def capturar_codigo_producto() -> str:
    print()
    codigo = input("Ingrese el código del producto: ").strip().upper()
    return codigo


def mostrar_lista_en_formato_tabular(valores: list) -> None:
    print(*valores, sep='\t\t\t')


def pausar_ejecucion() -> None:
    input('Presione Enter para continuar >')