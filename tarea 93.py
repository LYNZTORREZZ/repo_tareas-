notas = []
continuar = "S"

while continuar == "S":
    nota = float(input("Ingrese una nota del estudiante: "))
    notas.append(nota)
    
    continuar = input("¿Desea ingresar otra nota? (S/N): ").upper()

if len(notas) > 0:
    suma = sum(notas)
    promedio = suma / len(notas)
    mayor = max(notas)
    menor = min(notas)
    
    print(f"\nPromedio de notas: {promedio}")
    print(f"Nota mayor: {mayor}")
    print(f"Nota menor: {menor}")
else:
    print("No se ingresaron notas.")
