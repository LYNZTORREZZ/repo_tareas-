while True:
    print("\n--- CALCULO DE AREAS ---")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Salir")
    opcion = input("Seleccione una figura: ")
    
    if opcion == "4":
        print("Programa terminado.")
        break
        
    if opcion == "1":
        lado = float(input("Ingrese el lado del cuadrado: "))
        print(f"Area del cuadrado: {lado * lado}")
    elif opcion == "2":
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        print(f"Area del triangulo: {(base * altura) / 2}")
    elif opcion == "3":
        radio = float(input("Ingrese el radio del circulo: "))
        print(f"Area del circulo: {3.1416 * (radio ** 2)}")
    else:
        print("Opcion no valida.")
