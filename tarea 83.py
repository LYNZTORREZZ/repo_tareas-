dividendo = float(input("Ingrese el dividendo (numero a dividir): "))
divisor = 0.0

while divisor == 0:
    divisor = float(input("Ingrese el divisor (no puede ser cero): "))
    if divisor == 0:
        print("Error: El divisor no puede ser cero.")

resultado = dividendo / divisor
print(f"El resultado de la division es: {resultado}")
