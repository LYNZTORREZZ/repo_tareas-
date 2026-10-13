acumulador = 0
continuar = "S"

while continuar == "S":
    numero = float(input("Ingrese un numero para acumular: "))
    acumulador += numero
    
    continuar = input("¿Desea ingresar otro numero? (S/N): ").upper()

print(f"La suma total acumulada es: {acumulador}")
