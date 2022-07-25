import ui
from inventario.logica import InventarioService
from ventas.logica import VentasService
from ventas.modelos.item import Item

inventario_service = InventarioService()
ventas_service = VentasService()

def main() -> None:
    while True:
        menu_principal = {  'A': 'AGREGAR PRODUCTO',
                            'B': 'QUITAR PRODUCTO',
                            'C': 'LISTAR PRODUCTOS',
                            'D': 'AÑADIR PRODUCTO AL CARRITO',
                            'E': 'QUITAR PRODUCTO DEL CARRITO',
                            'F': 'FACTURAR',
                            'G': 'SALIR' }

        ui.mostrar_menu('MENÚ PRINCIPAL', '¿Qué opción desea ejecutar?', menu_principal)
        opcion = ui.capturar_opcion_menu(menu_principal.keys())
        
        if opcion == 'A':
            ejecutar_opc_agregar_producto()
        elif opcion == 'B':
            ejecutar_opc_quitar_producto()
        elif opcion == 'C':            
            ejecutar_opc_listar_productos(hacer_pausa=True)
        elif opcion == 'D':
            ejecutar_opc_agregar_a_carrito()
        elif opcion == 'E':
            pass
        elif opcion == 'F':
            ejecutar_opc_facturar()
        else:
            break
        

def ejecutar_opc_agregar_producto() -> None:
    ui.mostrar_mensaje(' --- INVENTARIO: INGRESO DE PRODUCTO --- ')
    producto = ui.capturar_producto()
    try:
        inventario_service.agregar_producto(producto)
        ui.mostrar_mensaje(f'El producto {producto.codigo} se agregó exitosamente.')
    except Exception as ex:
        ui.mostrar_mensaje(ex)

    ui.pausar_ejecucion()


def ejecutar_opc_quitar_producto() -> None:
    ui.mostrar_mensaje(' --- INVENTARIO: ELIMINACIÓN DE PRODUCTO --- ')
    codigo = ui.capturar_codigo_producto()
    try:
        inventario_service.quitar_producto(codigo)
        ui.mostrar_mensaje(f'El producto {codigo} se eliminó exitosamente.')
    except Exception as ex:
        ui.mostrar_mensaje(ex)
    
    ui.pausar_ejecucion()


def ejecutar_opc_listar_productos(hacer_pausa: bool) -> None:
    ui.mostrar_mensaje(' --- LISTA DE PRODUCTOS --- ')
    ui.mostrar_lista_en_formato_tabular(['CÓDIGO', 'NOMBRE', 'PRECIO'])

    for producto in inventario_service.obtener_productos():
        ui.mostrar_lista_en_formato_tabular(producto.__dict__.values())

    if hacer_pausa:
        ui.pausar_ejecucion()


def ejecutar_opc_agregar_a_carrito() -> None:
    ui.mostrar_mensaje(' --- CARRITO: AÑADIR PRODUCTO --- ')

    ui.mostrar_mensaje('Seleccione el producto que desea añadir.')
    ejecutar_opc_listar_productos(hacer_pausa=False)

    codigo = ui.capturar_codigo_producto()    
    try:
        producto = inventario_service.obtener_producto_por_codigo(codigo)        
        cantidad = ui.capturar_numero('Ingrese la cantidad: ')
        item = Item(None, producto, cantidad)
        ventas_service.agregar_al_carrito(item)
        ui.mostrar_mensaje(f'El producto {codigo} se agregó exitosamente al carrito.')

    except Exception as ex:
        ui.mostrar_mensaje(ex)
        
    ui.pausar_ejecucion()


def ejecutar_opc_facturar():
    ui.mostrar_mensaje(' --- FACTURAR --- ')
    
    if len(ventas_service.obtener_items_del_carrito()) == 0:
        ui.mostrar_mensaje('No ha añadido items al carrito.')
    else:    
        cedula = ui.capturar_texto('Ingrese la cédula del cliente: ')
        nombre = ui.capturar_texto('Ingrese el nombre del cliente: ')
        email = ui.capturar_texto('Ingrese el email del cliente: ')

        try:
            ventas_service.facturar(cedula, nombre, email)
            ui.mostrar_mensaje('La factura se guardó correctamente.')
        except Exception as ex:
            ui.mostrar_mensaje(ex)

    ui.pausar_ejecucion()

if __name__ == "__main__":
    main()