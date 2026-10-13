respuesta_valida = False

while not respuesta_valida:
    respuesta = input("¿Acepta los terminos? (S/N): ").upper()
    
    if respuesta == "S" or respuesta == "N":
        respuesta_valida = True
        print(f"Opcion valida seleccionada: {respuesta}")
    else:
        print("Entrada incorrecta. Por favor ingrese unicamente S o N.")
