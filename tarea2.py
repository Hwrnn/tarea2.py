import os


productos = []


def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
        print("Datos cargados correctamente.")
    else:
        print("No se encontraron datos previos.")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente.")

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el precio y la cantidad.")
    
    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    if productos:
        print("Lista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos registrados.")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto que deseas actualizar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print(f"Producto encontrado: {producto['nombre']}")
            while True:
                print("1: Actualizar nombre")
                print("2: Actualizar precio")
                print("3: Actualizar cantidad")
                print("4: Volver al menú")
                opcion = input("Selecciona una opción: ")
                
                if opcion == '1':
                    producto['nombre'] = input("Introduce el nuevo nombre: ")
                    print("Nombre actualizado correctamente.")
                elif opcion == '2':
                    while True:
                        try:
                            producto['precio'] = float(input("Introduce el nuevo precio: "))
                            print("Precio actualizado correctamente.")
                            break
                        except ValueError:
                            print("Por favor, introduce un precio válido.")
                elif opcion == '3':
                    while True:
                        try:
                            producto['cantidad'] = int(input("Introduce la nueva cantidad: "))
                            print("Cantidad actualizada correctamente.")
                            break
                        except ValueError:
                            print("Por favor, introduce una cantidad válida.")
                elif opcion == '4':
                    break
                else:
                    print("Opción no válida, intenta de nuevo.")
            break
    else:
        print(f"El producto '{nombre}' no se encontró.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto que deseas eliminar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            break
    else:
        print(f"El producto '{nombre}' no se encontró.")

def menu():
    cargar_datos()  
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos() 
            break
        else:
            print("Por favor, selecciona una opción válida.")


menu()
