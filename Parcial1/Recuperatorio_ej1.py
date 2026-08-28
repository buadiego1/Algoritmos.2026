# Ejercicio 1: Lista simple de 15 superhéroes Realizar dos funciones recursivas:
# 1. Buscar si "Capitán América" está en la lista.
# 2. Listar todos los superhéroes de la lista.


# Lista de 15 superhéroes
superheroes = [
    "Iron Man",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Captain Marvel",
    "Ant-Man",
    "Scarlet Witch",
    "Vision",
    "Falcon",
    "Capitán América",
    "Star-Lord"
]


# Función recursiva para buscar un superhéroe
def buscar_capitanamerica(lista, objetivo, indice=0):

    # Caso base: llego al final de la lista
    if indice == len(lista):
        return False

    # Caso base encuentro a Capitan America
    if lista[indice] == objetivo:
        return True

    # Llamada recursiva, sigo buscando en el siguiente elemento
    return buscar_capitanamerica(lista, objetivo, indice + 1)


# Función recursiva para listar los superhéroes
def listar_superheroes(lista, indice=0):

    # Caso base: llego al final de la lista
    if indice == len(lista):
        return

    # Muestro el superhéroe actual
    print(lista[indice])

    # Llamada recursiva: avanzo al siguiente elemento
    listar_superheroes(lista, indice + 1)


# Programa principal
if __name__ == "__main__":
    print("Lista de superhéroes")
    listar_superheroes(superheroes)

    print("\nBúsqueda")
    encontrado = buscar_capitanamerica(superheroes, "Capitán América")

    if encontrado:
        print("Capitán América SÍ está en la lista.")
    else:
        print("Capitán América NO está en la lista.")