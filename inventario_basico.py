inventario = []
while True:
    print("\n=== MENÚ DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        inventario.append(producto)
        print("Producto agregado correctamente.")
    elif opcion == "2":
        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            print("\nProductos en el inventario:")
            for i, producto in enumerate(inventario, start=1):
                print(f"{i}. {producto}")
    elif opcion == "3":
        print("Saliendo del sistema de inventario...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")