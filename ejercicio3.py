#esta funcion me analiza el texto y me cuenta las vocales y las palabras
def analizar_texto(*args, contar_vocales=True, contar_palabras=True, **kwargs):
    texto_completo = " ".join(args)
    total_vocales = 0
    total_palabras = 0

    if contar_vocales:
        for c in texto_completo.lower():
            if c in 'aeiouáéíóúü':
                total_vocales += 1

    if contar_palabras:
        # dividir por espacios en blanco
        total_palabras = len(texto_completo.split())

    if contar_vocales:
        print(f"Total de vocales: {total_vocales}")
    if contar_palabras:
        print(f"Total de palabras: {total_palabras}")


def main():
    print("Ejemplo de uso de analizar_texto: \n")
    analizar_texto("Hola Mundo", "Python es genial", contar_vocales=True, contar_palabras=True)



if __name__ == '__main__':
    main()
