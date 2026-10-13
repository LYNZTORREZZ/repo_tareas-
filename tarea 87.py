numero = int(input("Ingrese el numero 1: "))
mayor = numero
menor = numero

for i in range(2, 11):
    numero = int(input(f"Ingrese el numero {i}: "))
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")
