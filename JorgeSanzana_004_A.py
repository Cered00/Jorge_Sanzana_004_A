entradas_vendidas = [0] * 100
lista_asistentes = []
ganancias = {'Platinum': 0, 'Gold': 0, 'Silver': 0}

def mostrar_menu():
    print("---- Concert VIP Michael Jam ----")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def comprar_entradas():
    try:
        cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
        if cantidad < 1 or cantidad > 3:
            print("Cantidad inválida. Intente nuevamente.")
            return
    
        for i in range(cantidad):
            print("Ubicaciones disponibles:")
            for j in range(len(entradas_vendidas)):
                if entradas_vendidas[j] == 0:
                    print(f"Asiento {j+1} - Disponible")
                else:
                    print(f"Asiento {j+1} - X")
                
            ubicacion = int(input("Seleccione una ubicación: ")) - 1
     
            if entradas_vendidas[ubicacion] == 0:
                entradas_vendidas[ubicacion] = 1
                run = int(input("Ingrese el RUN del asistente: "))
                lista_asistentes.append(run)
            
                if ubicacion < 20:
                    ganancias['Platinum'] += 120000
                elif ubicacion < 50:
                    ganancias['Gold'] += 80000
                else:
                    ganancias['Silver'] += 50000
                
                print("Compra de entradas realizada correctamente.")
            else:
                print("Ubicación no disponible. Por favor, seleccione otra.")
     
    except ValueError:
        print("Debe ingresar un número entero válido para la cantidad de entradas.")

def mostrar_ubicaciones_disponibles():
    print("---- Ubicaciones Disponibles ----")
    for i in range(100):
        if entradas_vendidas[i] == 0:
            print(f"Asiento {i+1} - Disponible")
        else:
            print(f"Asiento {i+1} - X")

def ver_listado_asistentes():
    print("---- Listado de Asistentes ----")
    lista_asistentes.sort()
    for asistente in lista_asistentes:
        print(f"RUN: {asistente}")

def mostrar_ganancias_totales():
    print("---- Ganancias Totales ----")
    print("Tipo Entrada    Cantidad    Total")
    for tipo, total in ganancias.items():
        cantidad = total // (120000 if tipo == 'Platinum' else 80000 if tipo == 'Gold' else 50000)
        print(f"{tipo:<15} {cantidad:<11} ${total:,.0f}")
    print(f"{'TOTAL':<15} {sum(entradas_vendidas):<11} ${sum(ganancias.values()):,.0f}")

def salir():
    print("Gracias por su tiempo.")



while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    while opcion not in ["1", "2", "3", "4", "5"]:
        print("Opción inválida. Intente nuevamente")
        opcion = input("Seleccione una opción: ")
    if opcion == "1":
        comprar_entradas()
    elif opcion == "2":
        mostrar_ubicaciones_disponibles()
    elif opcion == "3":
        ver_listado_asistentes()
    elif opcion == "4":
        mostrar_ganancias_totales()
    else:
        salir()
        break

