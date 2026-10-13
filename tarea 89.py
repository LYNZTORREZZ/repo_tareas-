n = int(input("Conteo de tipos. ¿Cuantos numeros desea ingresar?: "))
positivos = 0
negativos = 0
ceros = 0

for i in range(n):
    numero = float(input(f"Ingrese el numero {i+1}: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print(f"Cantidad de positivos: {positivos}")
print(f"Cantidad de negativos: {negativos}")
print(f"Cantidad de ceros: {ceros}")
