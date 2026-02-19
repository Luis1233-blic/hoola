
servicios = {
    "desarrollo": 2000,
    "soporte": 500,
    "consultoria": 200,
    "auditoria": 1500
}

clientes = []

def registrar_cliente():
    print("\n=== REGISTRO DE CLIENTE ===")

    while True:
        nombre = input("Nombre: ").strip()
        if nombre:
            break
        print(" El nombre no puede estar vacío.")

    while True:
        gmail = input("Gmail: ").strip()
        if "@" in gmail and "." in gmail:
            break
        print(" Gmail inválido. Debe contener '@' y '.'")

    while True:
        telefono = input("Teléfono: ").strip()
        if telefono.isdigit():
            break
        print(" El teléfono debe contener solo números.")

    while True:
        direccion = input("Dirección: ").strip()
        if direccion.replace(" ", "").isalnum():
            break
        print(" La dirección debe ser alfanumérica.")

    cliente = {
        "nombre": nombre,
        "gmail": gmail,
        "telefono": telefono,
        "direccion": direccion
    }

    clientes.append(cliente)
    print(" Cliente registrado correctamente.")

def mostrar_clientes():
    if not clientes:
        print("\nNo hay clientes registrados.")
        return

    print("\n=== CLIENTES REGISTRADOS ===")
    for i, c in enumerate(clientes, start=1):
        print(f"{i}. {c['nombre']} - {c['gmail']} - {c['telefono']}")

def seleccionar_servicios():
    print("\n=== SERVICIOS DISPONIBLES ===")

    lista_servicios = list(servicios.items())
    for i, (nombre, precio) in enumerate(lista_servicios, start=1):
        print(f"{i}. {nombre} : {precio} USD")

    seleccionados = set()

    while True:
        opcion = input("Selecciona el número del servicio (0 para terminar): ")

        if opcion == "0":
            break

        if opcion.isdigit():
            opcion = int(opcion)

            if 1 <= opcion <= len(lista_servicios):
                servicio_nombre = lista_servicios[opcion - 1][0]

                if servicio_nombre in seleccionados:
                    print(" Ese servicio ya fue agregado.")
                else:
                    seleccionados.add(servicio_nombre)
                    print(f" Agregado: {servicio_nombre}")
            else:
                print(" Número fuera de rango.")
        else:
            print(" Debes escribir un número.")

    return list(seleccionados)

def calcular_total(servicios_seleccionados):
    total = sum(servicios[s] for s in servicios_seleccionados)

    pares = len(servicios_seleccionados) // 2
    descuento = total * 0.30 if pares > 0 else 0

    total_final = total - descuento

    return total, descuento, total_final

def mostrar_factura(cliente, servicios_seleccionados, subtotal, descuento, total):
    print("\n===== FACTURA =====")
    print(f"Cliente: {cliente['nombre']}")
    print(f"Gmail: {cliente['gmail']}")
    print(f"Teléfono: {cliente['telefono']}")
    print(f"Dirección: {cliente['direccion']}")

    print("\nServicios adquiridos:")
    for s in servicios_seleccionados:
        print(f"- {s} : {servicios[s]} USD")

    print("\nSubtotal:", subtotal, "USD")
    print("Descuento:", descuento, "USD")
    print("TOTAL A PAGAR:", total, "USD")
    print("====================\n")

def crear_pedido():
    if not clientes:
        print("\n Primero debes registrar un cliente.")
        return

    mostrar_clientes()

    opcion = input("Selecciona el número del cliente: ")

    if not opcion.isdigit():
        print(" Entrada inválida.")
        return

    opcion = int(opcion)

    if 1 <= opcion <= len(clientes):
        cliente = clientes[opcion - 1]
    else:
        print(" Cliente inválido.")
        return

    servicios_elegidos = seleccionar_servicios()

    if not servicios_elegidos:
        print("No seleccionaste servicios.")
        return

    subtotal, descuento, total = calcular_total(servicios_elegidos)
    mostrar_factura(cliente, servicios_elegidos, subtotal, descuento, total)



def menu():
    while True:
        print("\n=== TECH SOLUTIONS ===")
        print("1. Registrar cliente")
        print("2. Crear pedido")
        print("3. Ver clientes")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            crear_pedido()
        elif opcion == "3":
            mostrar_clientes()
        elif opcion == "4":
            print("👋 Gracias por usar el sistema.")
            break
        else:
            print(" Opción inválida.")



menu()
