aprobados = 0
reprobados = 0

for i in range(10):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    if nota >= 51:
        aprobados += 1
    else:
        reprobados += 1

print("\n--- ESTADISTICAS ---")
print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de reprobados: {reprobados}")
