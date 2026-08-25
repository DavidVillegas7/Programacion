saldo = 50000

while True:
    print("""
===== CAJERO AUTOMATICO =====

1. Consultar saldo
2. Ingresar dinero
3. Retirar dinero
4. Salir
""")

    opcion = input("Elija una opcion: ")

    match opcion:

        case "1":
            print(f"\nSu saldo actual es: ${saldo}")

        case "2":
            ingreso = input("Ingrese la cantidad a depositar: ")
            if ingreso.isdigit():
                ingreso = int(ingreso)
                if ingreso > 0:
                    saldo += ingreso
                    print(f"Se han ingresado ${ingreso}. Su nuevo saldo es: ${saldo}")
                else:
                    print("Error: Ingrese una cantidad mayor a 0.")
            else:
                print("Error: Debe ingresar un número válido.")

        case "3":
            retiro = input("Ingrese la cantidad a retirar: ")
            if retiro.isdigit():
                retiro = int(retiro)
                if retiro > 0 and retiro <= saldo:
                    saldo -= retiro
                    print(f"Se han retirado ${retiro}. Su nuevo saldo es: ${saldo}")
                elif retiro > saldo:
                    print("Fondos insuficientes.")
                else:
                    print("Error: Ingrese una cantidad mayor a 0.")
            else:
                print("Error: Debe ingresar un número válido.")

        case "4":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break

        case _:
            print("Opción inválida. Ingrese un número del 1 al 4.")