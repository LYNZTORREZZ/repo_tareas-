n = int(input("Suma y promedio. ¿Cuantos numeros desea ingresar?: "))
suma = 0

for i in range(n):
    numero = float(input(f"Ingrese el numero {i+1}: "))
    suma += numero

if n > 0:
    promedio = suma / n
else:
    promedio = 0

print(f"Suma total: {suma}")
print(f"Promedio: {promedio}")
