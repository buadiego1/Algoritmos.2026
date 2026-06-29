#Ejercicio 1
from super_heroes_data import superheroes

lista = superheroes[:15] #Uso solo los primeros 15 superheroes

def buscar_capitan(lista, indice):
    if indice >= len(lista):
        return False

    if lista[indice]["name"] == "Captain America":
        return True

    return buscar_capitan(lista, indice + 1)

def listar_superheroes(lista, indice):
    if indice >= len(lista):
        return

    print(lista[indice]["name"])
    listar_superheroes(lista, indice + 1)

# Invoco las funciones
if buscar_capitan(lista, 0):
    print("Capitan America está en la lista.")
else:
    print("Capitan America NO está en la lista.")

print("\nLista de superhéroes:")
listar_superheroes(lista, 0)

#---------------------------------------------------------------#

#Ejercicio 2
from super_heroes_data import superheroes
from collections import deque

# Trabajo solamente con los primeros 100 personajes
superheroes = superheroes[:100]

# a) Ordenados por nombre
print("a) Personajes ordenados por nombre\n")

lista_ordenada = sorted(superheroes, key=lambda personaje: personaje["name"])

for personaje in lista_ordenada:
    print(personaje["name"])


# b) Buscar posición de The Thing y Rocket Raccoon
print("\nb) Posiciones\n")

for posicion, personaje in enumerate(lista_ordenada):
    if personaje["name"] == "The Thing":
        print("The Thing está en la posición", posicion)

    if personaje["name"] == "Rocket Raccoon":
        print("Rocket Raccoon está en la posición", posicion)


# c) Mostrar villanos
print("\nc) Villanos\n")

for personaje in superheroes:
    if personaje["is_villain"]:
        print(personaje["name"])


# d) Villanos anteriores a 1980
print("\nd) Villanos antes de 1980\n")

cola = deque()

for personaje in superheroes:
    if personaje["is_villain"]:
        cola.append(personaje)

while len(cola) > 0:
    personaje = cola.popleft()

    if personaje["first_appearance"] < 1980:
        print(personaje["name"], "-", personaje["first_appearance"])


# e) Personajes que empiezan con Bl, G, My o W
print("\ne) Personajes que empiezan con Bl, G, My o W\n")

for personaje in superheroes:
    nombre = personaje["name"]

    if nombre.startswith("Bl") or nombre.startswith("G") or nombre.startswith("My") or nombre.startswith("W"):
        print(nombre)


# f) Ordenados por nombre real
print("\nf) Ordenados por nombre real\n")

lista_real = sorted(
    superheroes,
    key=lambda personaje: personaje["real_name"] if personaje["real_name"] else ""
)

for personaje in lista_real:
    print(personaje["real_name"], "-", personaje["name"])


# g) Ordenados por año de aparición
print("\ng) Ordenados por fecha de aparición\n")

lista_fecha = sorted(superheroes, key=lambda personaje: personaje["first_appearance"])

for personaje in lista_fecha:
    print(personaje["first_appearance"], "-", personaje["name"])


# h) Cambiar nombre real de Ant Man
print("\nh) Cambiar nombre real de Ant Man\n")

for personaje in superheroes:
    if personaje["name"] == "Ant Man":
        personaje["real_name"] = "Scott Lang"
        print(personaje)


# i) Biografías que contienen "time-traveling" o "suit"
print("\ni) Biografías que contienen 'time-traveling' o 'suit'\n")

for personaje in superheroes:
    texto = personaje["short_bio"].lower()

    if "time-traveling" in texto or "suit" in texto:
        print(personaje["name"])


# j) Eliminar Electro y Baron Zemo
print("\nj) Eliminar Electro y Baron Zemo\n")

for nombre in ["Electro", "Baron Zemo"]:

    eliminado = False

    for personaje in superheroes:
        if personaje["name"] == nombre:
            print("Se eliminó:")
            print(personaje)

            superheroes.remove(personaje)
            eliminado = True
            break

    if not eliminado:
        print(nombre, "no se encontró en la lista.")