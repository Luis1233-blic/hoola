
# Función con parámetro por omisión
def calcular_descuento(precio, descuento=10):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    precio_final = precio * (1 - descuento / 100)
    return precio_final


def main():
    precios = []
    print("Introduce al menos 3 precios de productos. Escribe 'fin' para terminar.")
    while len(precios) < 3:
        entrada = input(f"Precio #{len(precios)+1}: ")
        if entrada.lower() == 'fin':
            print("Debe ingresar al menos 3 precios.")
            continue
        try:
            valor = float(entrada)
            if valor < 0:
                print("El precio no puede ser negativo. Intenta de nuevo.")
                continue
            precios.append(valor)
        except ValueError:
            print("Entrada inválida. Escribe un número o 'fin'.")

    # calcula el  total con descuento aplicado a cada producto
    total = 0
    for p in precios:
        total += calcular_descuento(p)
    print(f"Total a pagar después de aplicar descuentos: {total:.2f}")
if __name__ == '__main__':
    main()
