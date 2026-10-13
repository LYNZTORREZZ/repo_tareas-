while True:
    print("\n--- MENU MATEMATICO ---")
    print("1. Calcular Factorial")
    print("2. Ver Tabla de Multiplicar")
    print("3. Verificar Par/Impar")
    print("4. Calcular Cuadrado")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "5":
        print("Fin del programa.")
        break
        
    if opcion in ["1", "2", "3", "4"]:
        numero = int(input("Ingrese el numero a evaluar: "))
        
        if opcion == "1":
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            print(f"El factorial de {numero} es: {factorial}")
            
        elif opcion == "2":
            print(f"Tabla del {numero}:")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
                
        elif opcion == "3":
            if numero % 2 == 0:
                print(f"El numero {numero} es Par.")
            else:
                print(f"El numero {numero} es Impar.")
                
        elif opcion == "4":
            print(f"El cuadrado de {numero} es: {numero ** 2}")
    else:
        print("Opcion invalida.")
