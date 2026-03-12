
# esta funcion  verifica si es un numero primo o no
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        valor = int(input("Introduce un número positivo: "))
    except ValueError:
        print("Error: debes escribir un número entero.")
        return

    if valor < 0:
        print("Error: el número debe ser positivo.")
        return

    contador = 0
    print(f"Números primos menores o iguales a {valor}:")
    for num in range(2, valor + 1):
        if es_primo(num):
            print(num)
            contador += 1

    print(f"Se encontraron {contador} números primos.")


if __name__ == '__main__':
    main()
