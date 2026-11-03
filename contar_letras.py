def contar_letras(nombre):
    # Quitamos los espacios al principio y al final del nombre
    nombre = nombre.strip()

    # Contamos solo las letras, ignorando espacios internos
    total = sum(1 for caracter in nombre if caracter.isalpha())

    # Definimos las vocales (con tildes y diéresis) para poder excluirlas
    vocales = "aeiouáéíóúüàèìòù"

    # Contamos las consonantes: letras que no son vocales
    total_consonantes = sum(
        1 for caracter in nombre if caracter.isalpha() and caracter.lower() not in vocales
    )

    # Devolvemos el total de letras y el total de consonantes
    return total, total_consonantes


if __name__ == "__main__":
    # Pedimos al usuario que escriba un nombre
    nombre = input("Escribe un nombre: ")

    # Llamamos a la función para contar las letras y las consonantes
    resultado, consonantes = contar_letras(nombre)

    # Mostramos el resultado por pantalla
    print(f"El nombre '{nombre}' tiene {resultado} letras y {consonantes} consonantes.")
