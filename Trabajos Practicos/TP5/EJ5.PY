class Nodo:
    def __init__(self, nombre, hero):
        self.nombre = nombre
        self.hero = hero
        self.izq = None
        self.der = None


# -------------------------------------------------
# INSERTAR EN EL ÁRBOL
# -------------------------------------------------

def insertar(raiz, nombre, hero):
    if raiz is None:
        return Nodo(nombre, hero)

    if nombre < raiz.nombre:
        raiz.izq = insertar(raiz.izq, nombre, hero)

    else:
        raiz.der = insertar(raiz.der, nombre, hero)

    return raiz


# -------------------------------------------------
# BARRIDO ORDENADO
# -------------------------------------------------

def barrido_inorden(raiz):
    if raiz is not None:
        barrido_inorden(raiz.izq)
        print(raiz.nombre)
        barrido_inorden(raiz.der)


# -------------------------------------------------
# BARRIDO INVERSO
# -------------------------------------------------

def barrido_inverso(raiz):
    if raiz is not None:
        barrido_inverso(raiz.der)
        print(raiz.nombre)
        barrido_inverso(raiz.izq)


# -------------------------------------------------
# B. LISTAR LOS VILLANOS ORDENADOS
# -------------------------------------------------

def listar_villanos(raiz):
    if raiz is not None:
        listar_villanos(raiz.izq)

        if raiz.hero == False:
            print(raiz.nombre)

        listar_villanos(raiz.der)


# -------------------------------------------------
# C. SUPERHÉROES QUE EMPIEZAN CON C
# -------------------------------------------------

def heroes_con_c(raiz):
    if raiz is not None:
        heroes_con_c(raiz.izq)

        if raiz.hero == True and raiz.nombre.upper().startswith("C"):
            print(raiz.nombre)

        heroes_con_c(raiz.der)


# -------------------------------------------------
# D. CANTIDAD DE SUPERHÉROES
# -------------------------------------------------

def contar_heroes(raiz):
    if raiz is None:
        return 0

    cantidad = 0

    if raiz.hero == True:
        cantidad = 1

    cantidad = cantidad + contar_heroes(raiz.izq)
    cantidad = cantidad + contar_heroes(raiz.der)

    return cantidad


# -------------------------------------------------
# E. BÚSQUEDA POR PROXIMIDAD
# -------------------------------------------------

def buscar_proximidad(raiz, texto):
    if raiz is None:
        return None

    # Buscamos si el texto aparece dentro del nombre
    if texto.lower() in raiz.nombre.lower():
        return raiz

    nodo = buscar_proximidad(raiz.izq, texto)

    if nodo is not None:
        return nodo

    return buscar_proximidad(raiz.der, texto)


# -------------------------------------------------
# F. SUPERHÉROES EN ORDEN DESCENDENTE
# -------------------------------------------------

def heroes_descendente(raiz):
    if raiz is not None:

        heroes_descendente(raiz.der)

        if raiz.hero == True:
            print(raiz.nombre)

        heroes_descendente(raiz.izq)


# -------------------------------------------------
# CONTAR NODOS DE UN ÁRBOL
# -------------------------------------------------

def contar_nodos(raiz):
    if raiz is None:
        return 0

    return 1 + contar_nodos(raiz.izq) + contar_nodos(raiz.der)


# -------------------------------------------------
# G. GENERAR ÁRBOL DE HÉROES Y VILLANOS
# -------------------------------------------------

def generar_bosque(raiz, arbol_heroes, arbol_villanos):
    if raiz is not None:

        if raiz.hero == True:
            arbol_heroes = insertar(
                arbol_heroes,
                raiz.nombre,
                True
            )

        else:
            arbol_villanos = insertar(
                arbol_villanos,
                raiz.nombre,
                False
            )

        arbol_heroes, arbol_villanos = generar_bosque(
            raiz.izq,
            arbol_heroes,
            arbol_villanos
        )

        arbol_heroes, arbol_villanos = generar_bosque(
            raiz.der,
            arbol_heroes,
            arbol_villanos
        )

    return arbol_heroes, arbol_villanos


# =================================================
# PROGRAMA PRINCIPAL
# =================================================

arbol = None


# -------------------------------------------------
# CARGA DE DATOS
# -------------------------------------------------

arbol = insertar(arbol, "Iron Man", True)
arbol = insertar(arbol, "Captain America", True)
arbol = insertar(arbol, "Thor", True)
arbol = insertar(arbol, "Hulk", True)
arbol = insertar(arbol, "Black Widow", True)
arbol = insertar(arbol, "Hawkeye", True)
arbol = insertar(arbol, "Doctor Strnge", True)   # MAL CARGADO
arbol = insertar(arbol, "Spider-Man", True)
arbol = insertar(arbol, "Black Panther", True)
arbol = insertar(arbol, "Scarlet Witch", True)
arbol = insertar(arbol, "Vision", True)

arbol = insertar(arbol, "Thanos", False)
arbol = insertar(arbol, "Loki", False)
arbol = insertar(arbol, "Ultron", False)
arbol = insertar(arbol, "Hela", False)
arbol = insertar(arbol, "Red Skull", False)
arbol = insertar(arbol, "Killmonger", False)


# -------------------------------------------------
# B. VILLANOS ORDENADOS
# -------------------------------------------------

print("VILLANOS ORDENADOS")
listar_villanos(arbol)


# -------------------------------------------------
# C. HÉROES QUE EMPIEZAN CON C
# -------------------------------------------------

print()
print("SUPERHÉROES QUE EMPIEZAN CON C")
heroes_con_c(arbol)


# -------------------------------------------------
# D. CANTIDAD DE SUPERHÉROES
# -------------------------------------------------

print()
print("CANTIDAD DE SUPERHÉROES:")
print(contar_heroes(arbol))


# -------------------------------------------------
# E. CORREGIR DOCTOR STRANGE
# -------------------------------------------------

print()
print("BUSCANDO DOCTOR STRANGE...")

nodo = buscar_proximidad(arbol, "Strnge")

if nodo is not None:
    print("Encontrado:", nodo.nombre)

    nodo.nombre = "Doctor Strange"

    print("Nombre corregido:", nodo.nombre)

else:
    print("No se encontró")


# -------------------------------------------------
# F. SUPERHÉROES DESCENDENTE
# -------------------------------------------------

print()
print("SUPERHÉROES ORDENADOS DE MANERA DESCENDENTE")
heroes_descendente(arbol)


# -------------------------------------------------
# G. GENERAR BOSQUE
# -------------------------------------------------

arbol_heroes = None
arbol_villanos = None

arbol_heroes, arbol_villanos = generar_bosque(
    arbol,
    arbol_heroes,
    arbol_villanos
)


# -------------------------------------------------
# G.I. CANTIDAD DE NODOS
# -------------------------------------------------

print()
print("CANTIDAD DE NODOS DEL ÁRBOL DE HÉROES:")
print(contar_nodos(arbol_heroes))

print()
print("CANTIDAD DE NODOS DEL ÁRBOL DE VILLANOS:")
print(contar_nodos(arbol_villanos))


# -------------------------------------------------
# G.II. BARRIDO ORDENADO
# -------------------------------------------------

print()
print("ÁRBOL DE HÉROES ORDENADO ALFABÉTICAMENTE")
barrido_inorden(arbol_heroes)

print()
print("ÁRBOL DE VILLANOS ORDENADO ALFABÉTICAMENTE")
barrido_inorden(arbol_villanos)