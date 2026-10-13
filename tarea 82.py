edad_valida = False

while not edad_valida:
    edad = int(input("Ingrese una edad: "))
    
    if edad >= 0:
        edad_valida = True
        print(f"Edad registrada con exito: {edad}")
    else:
        print("La edad no puede ser negativa. Intente nuevamente.")
