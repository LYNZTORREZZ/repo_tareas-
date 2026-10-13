n = int(input("¿Cuantas edades va a registrar?: "))
ninos = 0
adolescentes = 0
adultos = 0
mayores = 0

for i in range(n):
    edad = int(input(f"Ingrese la edad {i+1}: "))
    if edad <= 12:
        ninos += 1
    elif edad <= 17:
        adolescentes += 1
    elif edad <= 59:
        adultos += 1
    else:
        mayores += 1

print(f"\nResultados:\nNinos: {ninos}\nAdolescentes: {adolescentes}\nAdultos: {adultos}\nAdultos mayores: {mayores}")
