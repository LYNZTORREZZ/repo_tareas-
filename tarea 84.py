buscando_multiplo = True

while buscando_multiplo:
    numero = int(input("Ingrese un numero: "))
    
    if numero % 10 == 0:
        print(f"¡Correcto! El numero {numero} es multiplo de 10.")
        buscando_multiplo = False
    else:
        print("No es multiplo de 10. Siga intentando.")
