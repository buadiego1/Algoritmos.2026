class Superheroe:
    def __init__(self, nombre, anio, casa, biografia):
        self.nombre = nombre
        self.anio = anio
        self.casa = casa
        self.biografia = biografia


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaSuperheroes:
    def __init__(self):
        self.inicio = None

    # Insertar un superhéroe al final
    def insertar(self, superheroe):
        nuevo = Nodo(superheroe)

        if self.inicio is None:
            self.inicio = nuevo
        else:
            aux = self.inicio

            while aux.siguiente is not None:
                aux = aux.siguiente

            aux.siguiente = nuevo

    # a) Eliminar el nodo de Linterna Verde
    def eliminar(self, nombre):
        if self.inicio is None:
            return

        # Si el nodo a eliminar es el primero
        if self.inicio.dato.nombre == nombre:
            self.inicio = self.inicio.siguiente
            return

        anterior = self.inicio
        actual = self.inicio.siguiente

        while actual is not None:
            if actual.dato.nombre == nombre:
                anterior.siguiente = actual.siguiente
                return

            anterior = actual
            actual = actual.siguiente

    # b) Mostrar el año de aparición de Wolverine
    def mostrar_anio(self, nombre):
        aux = self.inicio

        while aux is not None:
            if aux.dato.nombre == nombre:
                print("Año de aparición de", nombre, ":", aux.dato.anio)
                return

            aux = aux.siguiente

        print("No se encontró el superhéroe.")

    # c) Cambiar la casa de Dr. Strange a Marvel
    def cambiar_casa(self, nombre, nueva_casa):
        aux = self.inicio

        while aux is not None:
            if aux.dato.nombre == nombre:
                aux.dato.casa = nueva_casa
                return

            aux = aux.siguiente

    # d) Mostrar superhéroes cuya biografía menciona "traje" o "armadura"
    def buscar_traje_armadura(self):
        aux = self.inicio

        while aux is not None:
            biografia = aux.dato.biografia.lower()

            if "traje" in biografia or "armadura" in biografia:
                print(aux.dato.nombre)

            aux = aux.siguiente

    # e) Mostrar nombre y casa de los superhéroes anteriores a 1963
    def anteriores_1963(self):
        aux = self.inicio

        while aux is not None:
            if aux.dato.anio < 1963:
                print("Nombre:", aux.dato.nombre)
                print("Casa:", aux.dato.casa)
                print()

            aux = aux.siguiente

    # f) Mostrar la casa de Capitana Marvel y Mujer Maravilla
    def mostrar_casa(self, nombre):
        aux = self.inicio

        while aux is not None:
            if aux.dato.nombre == nombre:
                print(nombre, "pertenece a", aux.dato.casa)
                return

            aux = aux.siguiente

        print("No se encontró el superhéroe.")

    # g) Mostrar toda la información de Flash y Star-Lord
    def mostrar_informacion(self, nombre):
        aux = self.inicio

        while aux is not None:
            if aux.dato.nombre == nombre:
                print("Nombre:", aux.dato.nombre)
                print("Año de aparición:", aux.dato.anio)
                print("Casa:", aux.dato.casa)
                print("Biografía:", aux.dato.biografia)
                print()
                return

            aux = aux.siguiente

        print("No se encontró el superhéroe.")

    # h) Listar superhéroes que comienzan con B, M o S
    def comenzar_bms(self):
        aux = self.inicio

        while aux is not None:
            primera_letra = aux.dato.nombre.upper()[0]

            if primera_letra in ["B", "M", "S"]:
                print(aux.dato.nombre)

            aux = aux.siguiente

    # i) Determinar cuántos superhéroes hay de cada casa
    def contar_por_casa(self):
        marvel = 0
        dc = 0

        aux = self.inicio

        while aux is not None:

            if aux.dato.casa.lower() == "marvel":
                marvel += 1

            elif aux.dato.casa.lower() == "dc":
                dc += 1

            aux = aux.siguiente

        print("Cantidad de superhéroes de Marvel:", marvel)
        print("Cantidad de superhéroes de DC:", dc)


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

lista = ListaSuperheroes()

# Cargar superhéroes
lista.insertar(Superheroe(
    "Superman",
    1938,
    "DC",
    "Superhéroe proveniente del planeta Krypton que posee gran fuerza y utiliza un traje característico."
))

lista.insertar(Superheroe(
    "Batman",
    1939,
    "DC",
    "Héroe humano que combate el crimen utilizando tecnología, inteligencia y una armadura."
))

lista.insertar(Superheroe(
    "Mujer Maravilla",
    1941,
    "DC",
    "Guerrera amazona que utiliza un traje especial y armas mágicas."
))

lista.insertar(Superheroe(
    "Flash",
    1940,
    "DC",
    "Superhéroe capaz de moverse a gran velocidad gracias a la Fuerza de la Velocidad."
))

lista.insertar(Superheroe(
    "Linterna Verde",
    1940,
    "DC",
    "Miembro de los Green Lantern Corps que utiliza un anillo de poder y un traje."
))

lista.insertar(Superheroe(
    "Spider-Man",
    1962,
    "Marvel",
    "Peter Parker obtiene poderes de una araña y utiliza un traje para combatir el crimen."
))

lista.insertar(Superheroe(
    "Wolverine",
    1974,
    "Marvel",
    "Mutante con garras de adamantium, gran capacidad de regeneración y sentidos aumentados."
))

lista.insertar(Superheroe(
    "Dr. Strange",
    1963,
    "DC",
    "Médico que se convierte en un poderoso hechicero y utiliza magia para proteger el mundo."
))

lista.insertar(Superheroe(
    "Capitana Marvel",
    1967,
    "Marvel",
    "Heroína con grandes poderes cósmicos que lucha para proteger la Tierra."
))

lista.insertar(Superheroe(
    "Star-Lord",
    1976,
    "Marvel",
    "Líder de los Guardianes de la Galaxia que utiliza tecnología avanzada y un traje especial."
))

lista.insertar(Superheroe(
    "Black Panther",
    1966,
    "Marvel",
    "Rey de Wakanda que utiliza una avanzada armadura de vibranium."
))

lista.insertar(Superheroe(
    "Ms. Marvel",
    2013,
    "Marvel",
    "Heroína que posee poderes especiales y utiliza un traje para combatir el crimen."
))


# ==========================================================
# a) ELIMINAR LINERNA VERDE
# ==========================================================

lista.eliminar("Linterna Verde")


# ==========================================================
# b) MOSTRAR AÑO DE APARICIÓN DE WOLVERINE
# ==========================================================

lista.mostrar_anio("Wolverine")


# ==========================================================
# c) CAMBIAR LA CASA DE DR. STRANGE A MARVEL
# ==========================================================

lista.cambiar_casa("Dr. Strange", "Marvel")


# ==========================================================
# d) SUPERHÉROES CON "TRAJE" O "ARMADURA" EN SU BIOGRAFÍA
# ==========================================================

print("\nSuperhéroes cuya biografía menciona traje o armadura:")
lista.buscar_traje_armadura()


# ==========================================================
# e) SUPERHÉROES ANTERIORES A 1963
# ==========================================================

print("\nSuperhéroes anteriores a 1963:")
lista.anteriores_1963()


# ==========================================================
# f) CASA DE CAPITANA MARVEL Y MUJER MARAVILLA
# ==========================================================

print("\nCasa de Capitana Marvel:")
lista.mostrar_casa("Capitana Marvel")

print("\nCasa de Mujer Maravilla:")
lista.mostrar_casa("Mujer Maravilla")


# ==========================================================
# g) INFORMACIÓN DE FLASH Y STAR-LORD
# ==========================================================

print("\nInformación de Flash:")
lista.mostrar_informacion("Flash")

print("Información de Star-Lord:")
lista.mostrar_informacion("Star-Lord")


# ==========================================================
# h) SUPERHÉROES QUE COMIENZAN CON B, M O S
# ==========================================================

print("Superhéroes que comienzan con B, M o S:")
lista.comenzar_bms()


# ==========================================================
# i) CANTIDAD DE SUPERHÉROES POR CASA
# ==========================================================

print("\nCantidad de superhéroes por casa:")
lista.contar_por_casa()



#EJ 15

# ============================================================
# LISTA DE LISTAS - ENTRENADORES POKÉMON
# ============================================================

# Cada entrenador se guarda como una lista:
# [nombre, torneos_ganados, batallas_perdidas, batallas_ganadas, lista_pokemon]
#
# Cada Pokémon se guarda como una lista:
# [nombre, nivel, tipo, subtipo]


# ============================================================
# FUNCIONES
# ============================================================

# a) Obtener la cantidad de Pokémon de un determinado entrenador
def cantidad_pokemon(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0].lower() == nombre_entrenador.lower():
            return len(entrenador[4])

    return 0


# b) Listar entrenadores que hayan ganado más de tres torneos
def entrenadores_mas_de_tres_torneos(entrenadores):
    for entrenador in entrenadores:
        if entrenador[1] > 3:
            print(entrenador[0])


# c) Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_mejor_entrenador(entrenadores):

    if len(entrenadores) == 0:
        return

    # Buscar el entrenador con más torneos ganados
    mejor_entrenador = entrenadores[0]

    for entrenador in entrenadores:
        if entrenador[1] > mejor_entrenador[1]:
            mejor_entrenador = entrenador

    # Buscar el Pokémon de mayor nivel
    if len(mejor_entrenador[4]) == 0:
        print("El entrenador no tiene Pokémon.")
        return

    pokemon_mayor = mejor_entrenador[4][0]

    for pokemon in mejor_entrenador[4]:
        if pokemon[1] > pokemon_mayor[1]:
            pokemon_mayor = pokemon

    print("Entrenador con más torneos:", mejor_entrenador[0])
    print("Torneos ganados:", mejor_entrenador[1])
    print("Pokémon de mayor nivel:")
    print("Nombre:", pokemon_mayor[0])
    print("Nivel:", pokemon_mayor[1])
    print("Tipo:", pokemon_mayor[2])
    print("Subtipo:", pokemon_mayor[3])


# d) Mostrar todos los datos de un entrenador y sus Pokémon
def mostrar_entrenador(entrenadores, nombre_entrenador):

    for entrenador in entrenadores:

        if entrenador[0].lower() == nombre_entrenador.lower():

            print("===================================")
            print("ENTRENADOR")
            print("===================================")
            print("Nombre:", entrenador[0])
            print("Torneos ganados:", entrenador[1])
            print("Batallas perdidas:", entrenador[2])
            print("Batallas ganadas:", entrenador[3])

            print("\nPOKÉMON:")
            
            if len(entrenador[4]) == 0:
                print("No tiene Pokémon.")
            else:
                for pokemon in entrenador[4]:
                    print("-------------------------------")
                    print("Nombre:", pokemon[0])
                    print("Nivel:", pokemon[1])
                    print("Tipo:", pokemon[2])
                    print("Subtipo:", pokemon[3])

            print("===================================")
            return

    print("No se encontró el entrenador.")


# e) Entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79%
def entrenadores_mas_79(entrenadores):

    for entrenador in entrenadores:

        batallas_ganadas = entrenador[3]
        batallas_perdidas = entrenador[2]

        total_batallas = batallas_ganadas + batallas_perdidas

        if total_batallas > 0:
            porcentaje = (batallas_ganadas / total_batallas) * 100

            if porcentaje > 79:
                print(
                    entrenador[0],
                    "- Porcentaje de victorias:",
                    round(porcentaje, 2),
                    "%"
                )


# f) Entrenadores que tengan Pokémon:
#    - tipo fuego y subtipo planta
#    - O tipo agua y subtipo volador
def entrenadores_fuego_planta_o_agua_volador(entrenadores):

    for entrenador in entrenadores:

        for pokemon in entrenador[4]:

            tipo = pokemon[2].lower()
            subtipo = pokemon[3].lower()

            if ((tipo == "fuego" and subtipo == "planta") or
                (tipo == "agua" and subtipo == "volador")):

                print(entrenador[0])
                break


# g) Promedio de nivel de los Pokémon de un determinado entrenador
def promedio_nivel(entrenadores, nombre_entrenador):

    for entrenador in entrenadores:

        if entrenador[0].lower() == nombre_entrenador.lower():

            if len(entrenador[4]) == 0:
                print("El entrenador no tiene Pokémon.")
                return

            suma = 0

            for pokemon in entrenador[4]:
                suma += pokemon[1]

            promedio = suma / len(entrenador[4])

            print(
                "Promedio de nivel de",
                entrenador[0],
                ":",
                round(promedio, 2)
            )
            return

    print("No se encontró el entrenador.")


# h) Determinar cuántos entrenadores tienen a un determinado Pokémon
def cantidad_entrenadores_con_pokemon(entrenadores, nombre_pokemon):

    cantidad = 0

    for entrenador in entrenadores:

        for pokemon in entrenador[4]:

            if pokemon[0].lower() == nombre_pokemon.lower():
                cantidad += 1
                break

    print(
        "Cantidad de entrenadores que tienen a",
        nombre_pokemon,
        ":",
        cantidad
    )


# i) Mostrar entrenadores que tienen Pokémon repetidos
def entrenadores_con_pokemon_repetidos(entrenadores):

    for entrenador in entrenadores:

        nombres_pokemon = []

        repetido = False

        for pokemon in entrenador[4]:

            if pokemon[0].lower() in nombres_pokemon:
                repetido = True
                break

            nombres_pokemon.append(pokemon[0].lower())

        if repetido:
            print(entrenador[0])


# j) Entrenadores que tengan uno de estos Pokémon:
#    Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemon_especiales(entrenadores):

    buscados = ["tyrantrum", "terrakion", "wingull"]

    for entrenador in entrenadores:

        for pokemon in entrenador[4]:

            if pokemon[0].lower() in buscados:
                print(entrenador[0])
                break


# k) Determinar si un entrenador X tiene al Pokémon Y
def entrenador_tiene_pokemon(entrenadores):

    nombre_entrenador = input("Ingrese el nombre del entrenador: ")
    nombre_pokemon = input("Ingrese el nombre del Pokémon: ")

    for entrenador in entrenadores:

        if entrenador[0].lower() == nombre_entrenador.lower():

            for pokemon in entrenador[4]:

                if pokemon[0].lower() == nombre_pokemon.lower():

                    print("\nEl entrenador tiene ese Pokémon.\n")

                    print("DATOS DEL ENTRENADOR")
                    print("Nombre:", entrenador[0])
                    print("Torneos ganados:", entrenador[1])
                    print("Batallas perdidas:", entrenador[2])
                    print("Batallas ganadas:", entrenador[3])

                    print("\nDATOS DEL POKÉMON")
                    print("Nombre:", pokemon[0])
                    print("Nivel:", pokemon[1])
                    print("Tipo:", pokemon[2])
                    print("Subtipo:", pokemon[3])

                    return

            print("El entrenador NO tiene ese Pokémon.")
            return

    print("No se encontró el entrenador.")


# ============================================================
# DATOS DE EJEMPLO
# ============================================================

entrenadores = [

    [
        "Ash",
        5,
        10,
        45,
        [
            ["Pikachu", 80, "Eléctrico", "Ninguno"],
            ["Charizard", 75, "Fuego", "Volador"],
            ["Bulbasaur", 40, "Planta", "Veneno"]
        ]
    ],

    [
        "Misty",
        2,
        8,
        22,
        [
            ["Starmie", 60, "Agua", "Psíquico"],
            ["Gyarados", 70, "Agua", "Volador"],
            ["Wingull", 20, "Agua", "Volador"]
        ]
    ],

    [
        "Brock",
        4,
        15,
        40,
        [
            ["Onix", 65, "Roca", "Tierra"],
            ["Tyrantrum", 80, "Roca", "Dragón"],
            ["Geodude", 30, "Roca", "Tierra"]
        ]
    ],

    [
        "Gary",
        6,
        5,
        50,
        [
            ["Blastoise", 85, "Agua", "Ninguno"],
            ["Terrakion", 90, "Roca", "Lucha"],
            ["Blastoise", 70, "Agua", "Ninguno"]
        ]
    ],

    [
        "Serena",
        1,
        20,
        15,
        [
            ["Sylveon", 55, "Hada", "Ninguno"],
            ["Pancham", 30, "Lucha", "Ninguno"]
        ]
    ]
]


# ============================================================
# PRUEBA DE LAS FUNCIONES
# ============================================================

print("\n========== a) CANTIDAD DE POKÉMON ==========")
print("Cantidad de Pokémon de Ash:",
    cantidad_pokemon(entrenadores, "Ash"))


print("\n========== b) MÁS DE 3 TORNEOS ==========")
entrenadores_mas_de_tres_torneos(entrenadores)


print("\n========== c) POKÉMON DE MAYOR NIVEL ==========")
pokemon_mayor_nivel_mejor_entrenador(entrenadores)


print("\n========== d) DATOS DE UN ENTRENADOR ==========")
mostrar_entrenador(entrenadores, "Ash")


print("\n========== e) MÁS DEL 79% DE VICTORIAS ==========")
entrenadores_mas_79(entrenadores)


print("\n========== f) FUEGO/PLANTA O AGUA/VOLADOR ==========")
entrenadores_fuego_planta_o_agua_volador(entrenadores)


print("\n========== g) PROMEDIO DE NIVEL ==========")
promedio_nivel(entrenadores, "Ash")


print("\n========== h) CUÁNTOS TIENEN UN POKÉMON ==========")
cantidad_entrenadores_con_pokemon(entrenadores, "Pikachu")


print("\n========== i) POKÉMON REPETIDOS ==========")
entrenadores_con_pokemon_repetidos(entrenadores)


print("\n========== j) TYRANTRUM, TERRAKION O WINGULL ==========")
entrenadores_con_pokemon_especiales(entrenadores)


print("\n========== k) BUSCAR ENTRENADOR Y POKÉMON ==========")
entrenador_tiene_pokemon(entrenadores)