total = 0.0

while True:
    print("\n1. Registrar Producto")
    print("2. Finalizar Compra")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "2":
        break
    elif opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input(f"Precio de {nombre}: "))
        total += precio
    else:
        print("Opcion no valida.")

print(f"\nEl total acumulado de la compra es: {total}")
