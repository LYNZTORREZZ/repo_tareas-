while True:
    numero = int(input("Ingrese el numero para ver su tabla de multiplicar: "))
    
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        
    respuesta = input("\n¿Desea consultar otra tabla? (S/N): ").upper()
    if respuesta != "S":
        print("Programa finalizado.")
        break
