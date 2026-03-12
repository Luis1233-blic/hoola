# Mini sistema de gestión de estudiantes
def main():
    estudiantes = []
    print("Ingrese los datos de los estudiantes. Escriba 'fin' para terminar.")
    while True:
        nombre = input("Nombre: ")
        if nombre.lower() == 'fin':
            break
        try:
            nota = float(input("Nota: "))
        except ValueError:
            print("Nota inválida. Introduce un número.")
            continue
        estudiantes.append({"nombre": nombre, "nota": nota})

    print("\nLista de estudiantes registrados:")
    for est in estudiantes:
        print(f"{est['nombre']} - {est['nota']}")

if __name__ == '__main__':
    main()
