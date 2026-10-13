while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "5":
        print("Saliendo de la calculadora.")
        break
        
    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingrese primer numero: "))
        num2 = float(input("Ingrese segundo numero: "))
        
        if opcion == "1":
            print(f"Resultado: {num1 + num2}")
        elif opcion == "2":
            print(f"Resultado: {num1 - num2}")
        elif opcion == "3":
            print(f"Resultado: {num1 * num2}")
        elif opcion == "4":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("Opcion invalida.")
