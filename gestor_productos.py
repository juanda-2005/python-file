# Lista de productos
productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    try:
        precio = int(input("Introduce el precio del producto en guaraníes: "))
        cantidad = int(input("Introduce la cantidad disponible: "))
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        productos.append(producto)
        print(f"Producto '{nombre}' añadido correctamente.")
    except ValueError:
        print("Error: Por favor, introduce un precio y una cantidad válidos en números enteros.")

def ver_productos():
    if productos:
        print("\nLista de productos:")
        for producto in productos:

            precio_formateado = f"{producto['precio']:,.0f}".replace(",", ".")
            print(f"Nombre: {producto['nombre']}, Precio: {precio_formateado} Gs, Cantidad: {producto['cantidad']}")
    else:
        print("\nNo hay productos para mostrar.")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto que deseas actualizar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {producto}")
            try:
                nuevo_nombre = input("Introduce el nuevo nombre del producto (deja en blanco para no cambiarlo): ")
                nuevo_precio = input("Introduce el nuevo precio en guaraníes (deja en blanco para no cambiarlo): ")
                nueva_cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiarlo): ")

                if nuevo_nombre:
                    producto["nombre"] = nuevo_nombre
                if nuevo_precio:
                    producto["precio"] = int(nuevo_precio)
                if nueva_cantidad:
                    producto["cantidad"] = int(nueva_cantidad)

                print("Producto actualizado correctamente.")
            except ValueError:
                print("Error: Introduce valores válidos para el precio y cantidad.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto que deseas eliminar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print("Producto no encontrado.")

def guardar_datos():
    with open("productos.txt", "w") as file:
        # Escribimos una cabecera
        file.write(f"{'Nombre':<20}{'Precio (Gs)':>15}{'Cantidad':>10}\n")
        file.write("="*45 + "\n")  # Línea divisoria
        
        # Escribimos cada producto en líneas bien formateadas
        for producto in productos:
            nombre = producto["nombre"]
            precio = f"{producto['precio']:,}".replace(",", ".")
            cantidad = producto["cantidad"]
            file.write(f"{nombre:<20}{precio:>15}{cantidad:>10}\n")

    print("Datos guardados en productos.txt.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as file:
            next(file)  # Omitir la cabecera
            next(file)  # Omitir la línea divisoria
            for line in file:
                if line.strip():  # Ignorar líneas vacías
                    nombre = line[:20].strip()
                    precio = int(line[20:35].strip().replace(".", ""))
                    cantidad = int(line[35:].strip())
                    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
                    productos.append(producto)
        print("Datos cargados desde productos.txt.")
    except FileNotFoundError:
        print("No se encontró productos.txt. Se iniciará con una lista de productos vacía.")
    except ValueError:
        print("Error en el formato de productos.txt.")

def menu():
    cargar_datos()
    while True:
        print("\nSistema de Gestión de Productos")
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
            print("Gracias por usar el sistema de gestión de productos.")
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()
