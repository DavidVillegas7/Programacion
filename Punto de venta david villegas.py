ticket = 0

while True:
    print("""===== PUNTO DE VENTA =====
    1. Agregar Hamburguesa ($4500)
    2. Agregar Papas Fritas ($2000)
    3. Agregar Bebida ($1500)
    4. Pagar el pedido (Cierra el ticket)
    5. Salir
    """)

    opcion = input("Elija una opción: ")

    match opcion:
        case "1":
            ticket += 4500
            print(f"Hamburguesa agregada. Total del ticket: ${ticket}")

        case "2":
            ticket += 2000
            print(f"Papas Fritas agregadas. Total del ticket: ${ticket}")

        case "3":
            ticket += 1500
            print(f"Bebida agregada. Total del ticket: ${ticket}")

        case "4":
            print(f"Total a pagar: ${ticket}")
            ticket = 0

        case "5":
            print("Gracias por su compra.")
            break

        case _:
            print("Opción no válida. Por favor, elija una opción válida.")