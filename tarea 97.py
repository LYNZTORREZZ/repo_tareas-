saldo = 1000.0  # Saldo inicial de prueba

while True:
    print("\n--- CAJERO AUTOMATICO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "4":
        print("Gracias por usar el sistema bancario.")
        break
    elif opcion == "1":
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == "2":
        deposito = float(input("Monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Deposito exitoso. Nuevo saldo: ${saldo}")
        else:
            print("Monto invalido.")
    elif opcion == "3":
        retiro = float(input("Monto a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
        else:
            print("Fondos insuficientes.")
    else:
        print("Opcion incorrecta.")
