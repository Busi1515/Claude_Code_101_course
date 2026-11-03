def contar_letras(nombre):
    # Quitamos los espacios al principio y al final del nombre
    nombre = nombre.strip()

    # Contamos solo las letras, ignorando espacios internos
    total = sum(1 for caracter in nombre if caracter.isalpha())

    # Definimos las vocales (con tildes y diéresis) para poder contarlas
    vocales = "aeiouáéíóúüàèìòù"

    # Contamos las vocales pasando cada carácter a minúscula
    total_vocales = sum(1 for caracter in nombre if caracter.lower() in vocales)

    # Devolvemos el total de letras y el total de vocales
    return total, total_vocales


if __name__ == "__main__":
    # Pedimos al usuario que escriba un nombre
    nombre = input("Escribe un nombre: ")

    # Llamamos a la función para contar las letras y las vocales
    resultado, vocales = contar_letras(nombre)

    # Mostramos el resultado por pantalla
    print(f"El nombre '{nombre}' tiene {resultado} letras y {vocales} vocales.")
