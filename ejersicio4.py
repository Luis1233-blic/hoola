#los try me sirven para manejar las excepciones 
def main():
    try:
        a = int(input("Introduce el primer número entero: "))
        b = int(input("Introduce el segundo número entero: "))
    except ValueError:
        print("Error: debes ingresar un número entero.")
        return

    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    else:
        print(f"El resultado de {a} / {b} es {resultado}")


if __name__ == '__main__':
    main()
