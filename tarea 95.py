pares = 0
impares = 0
positivos = 0
negativos = 0

while True:
    numero = int(input("Ingrese un numero (0 para salir): "))
    if numero == 0:
        break
        
    if numero > 0:
        positivos += 1
    else:
        negativos += 1
        
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Positivos: {positivos} | Negativos: {negativos}")
print(f"Pares: {pares} | Impares: {impares}")
