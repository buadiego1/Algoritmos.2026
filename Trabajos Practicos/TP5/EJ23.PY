class Nodo:
    def __init__(self, nombre, derrotado_por):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = ""
        self.capturada = ""
        self.izq = None
        self.der = None


# =====================================================
# INSERTAR
# =====================================================

def insertar(raiz, nombre, derrotado_por):
    if raiz is None:
        return Nodo(nombre, derrotado_por)

    if nombre < raiz.nombre:
        raiz.izq = insertar(raiz.izq, nombre, derrotado_por)
    else:
        raiz.der = insertar(raiz.der, nombre, derrotado_por)

    return raiz


# =====================================================
# BÚSQUEDA EXACTA
# =====================================================

def buscar(raiz, nombre):
    if raiz is None:
        return None

    if raiz.nombre == nombre:
        return raiz

    if nombre < raiz.nombre:
        return buscar(raiz.izq, nombre)
    else:
        return buscar(raiz.der, nombre)


# =====================================================
# A. LISTADO INORDEN
# =====================================================

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)

        print("Criatura:", raiz.nombre)
        print("Derrotado por:", raiz.derrotado_por)
        print("Descripcion:", raiz.descripcion)
        print("Capturada por:", raiz.capturada)
        print("-----------------------------")

        inorden(raiz.der)


# =====================================================
# B. CARGAR DESCRIPCIÓN
# =====================================================

def cargar_descripcion(raiz, nombre, descripcion):
    nodo = buscar(raiz, nombre)

    if nodo is not None:
        nodo.descripcion = descripcion
        return True

    return False


# =====================================================
# C. MOSTRAR TODA LA INFORMACIÓN DE TALOS
# =====================================================

def mostrar_talos(raiz):
    nodo = buscar(raiz, "Talos")

    if nodo is not None:
        print("INFORMACIÓN DE TALOS")
        print("Nombre:", nodo.nombre)
        print("Derrotado por:", nodo.derrotado_por)
        print("Descripcion:", nodo.descripcion)
        print("Capturada por:", nodo.capturada)
    else:
        print("No se encontró Talos")


# =====================================================
# D. CONTAR CUÁNTAS CRIATURAS DERROTÓ CADA HÉROE
# =====================================================

def contar_derrotas(raiz, nombres, cantidades):
    if raiz is not None:

        if raiz.derrotado_por != "-":
            encontrado = False

            for i in range(len(nombres)):
                if nombres[i] == raiz.derrotado_por:
                    cantidades[i] = cantidades[i] + 1
                    encontrado = True

            if encontrado == False:
                nombres.append(raiz.derrotado_por)
                cantidades.append(1)

        contar_derrotas(raiz.izq, nombres, cantidades)
        contar_derrotas(raiz.der, nombres, cantidades)


def mostrar_tres_mayores(raiz):
    nombres = []
    cantidades = []

    contar_derrotas(raiz, nombres, cantidades)

    # Ordenamos de mayor a menor
    for i in range(len(cantidades) - 1):
        for j in range(i + 1, len(cantidades)):
            if cantidades[j] > cantidades[i]:

                aux = cantidades[i]
                cantidades[i] = cantidades[j]
                cantidades[j] = aux

                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux

    print("TOP 3 HÉROES O DIOSES")
    
    limite = 3

    if len(nombres) < 3:
        limite = len(nombres)

    for i in range(limite):
        print(nombres[i], "-", cantidades[i], "criaturas")


# =====================================================
# E. CRIATURAS DERROTADAS POR HERACLES
# =====================================================

def criaturas_de_heracles(raiz):
    if raiz is not None:

        criaturas_de_heracles(raiz.izq)

        if raiz.derrotado_por == "Heracles":
            print(raiz.nombre)

        criaturas_de_heracles(raiz.der)


# =====================================================
# F. CRIATURAS NO DERROTADAS
# =====================================================

def no_derrotadas(raiz):
    if raiz is not None:

        no_derrotadas(raiz.izq)

        if raiz.derrotado_por == "-":
            print(raiz.nombre)

        no_derrotadas(raiz.der)


# =====================================================
# G. CARGAR CAPTURADA
# =====================================================

def capturar_criatura(raiz, nombre, heroe):
    nodo = buscar(raiz, nombre)

    if nodo is not None:
        nodo.capturada = heroe
        return True

    return False


# =====================================================
# H. HERACLES CAPTURÓ 4 CRIATURAS
# =====================================================

def capturas_heracles(raiz):
    capturar_criatura(raiz, "Cerbero", "Heracles")
    capturar_criatura(raiz, "Toro de Creta", "Heracles")
    capturar_criatura(raiz, "Cierva de Cerinea", "Heracles")
    capturar_criatura(raiz, "Jabalí de Erimanto", "Heracles")


# =====================================================
# I. BÚSQUEDA POR COINCIDENCIA
# =====================================================

def buscar_coincidencia(raiz, texto):
    if raiz is not None:

        buscar_coincidencia(raiz.izq, texto)

        if texto.lower() in raiz.nombre.lower():
            print(raiz.nombre)

        buscar_coincidencia(raiz.der, texto)


# =====================================================
# ELIMINAR NODO
# =====================================================

def eliminar(raiz, nombre):

    if raiz is None:
        return None

    if nombre < raiz.nombre:
        raiz.izq = eliminar(raiz.izq, nombre)

    elif nombre > raiz.nombre:
        raiz.der = eliminar(raiz.der, nombre)

    else:

        # Caso 1: no tiene hijos
        if raiz.izq is None and raiz.der is None:
            return None

        # Caso 2: solo tiene hijo derecho
        if raiz.izq is None:
            return raiz.der

        # Caso 3: solo tiene hijo izquierdo
        if raiz.der is None:
            return raiz.izq

        # Caso 4: tiene dos hijos
        sucesor = raiz.der

        while sucesor.izq is not None:
            sucesor = sucesor.izq

        raiz.nombre = sucesor.nombre
        raiz.derrotado_por = sucesor.derrotado_por
        raiz.descripcion = sucesor.descripcion
        raiz.capturada = sucesor.capturada

        raiz.der = eliminar(raiz.der, sucesor.nombre)

    return raiz


# =====================================================
# J. ELIMINAR BASILISCO Y SIRENAS
# =====================================================

def eliminar_basilisco_y_sirenas(raiz):
    raiz = eliminar(raiz, "Basilisco")
    raiz = eliminar(raiz, "Sirenas")

    return raiz


# =====================================================
# K. AVES DEL ESTÍNFALO
# =====================================================

def modificar_aves(raiz):
    nodo = buscar(raiz, "Aves del Estínfalo")

    if nodo is not None:
        nodo.derrotado_por = "Heracles"


# =====================================================
# L. CAMBIAR LÁDON POR DRAGÓN LÁDON
# =====================================================

def cambiar_ladon(raiz):

    nodo = buscar(raiz, "Ladón")

    if nodo is not None:

        derrotado_por = nodo.derrotado_por
        descripcion = nodo.descripcion
        capturada = nodo.capturada

        raiz = eliminar(raiz, "Ladón")

        raiz = insertar(raiz, "Dragón Ladón", derrotado_por)

        nuevo = buscar(raiz, "Dragón Ladón")

        nuevo.descripcion = descripcion
        nuevo.capturada = capturada

    return raiz


# =====================================================
# M. LISTADO POR NIVEL
# =====================================================

def por_nivel(raiz):

    if raiz is None:
        return

    cola = []
    cola.append(raiz)

    while len(cola) > 0:

        nodo = cola.pop(0)

        print(nodo.nombre)

        if nodo.izq is not None:
            cola.append(nodo.izq)

        if nodo.der is not None:
            cola.append(nodo.der)


# =====================================================
# N. CRIATURAS CAPTURADAS POR HERACLES
# =====================================================

def capturadas_por_heracles(raiz):
    if raiz is not None:

        capturadas_por_heracles(raiz.izq)

        if raiz.capturada == "Heracles":
            print(raiz.nombre)

        capturadas_por_heracles(raiz.der)


# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

arbol = None


# =====================================================
# CARGA DE CRIATURAS
# =====================================================

arbol = insertar(arbol, "Ceto", "-")
arbol = insertar(arbol, "Tifón", "Zeus")
arbol = insertar(arbol, "Equidna", "Argos Panoptes")
arbol = insertar(arbol, "Dino", "-")
arbol = insertar(arbol, "Pefredo", "-")
arbol = insertar(arbol, "Enio", "-")
arbol = insertar(arbol, "Escila", "-")
arbol = insertar(arbol, "Caribdis", "-")
arbol = insertar(arbol, "Euríale", "-")
arbol = insertar(arbol, "Esteno", "-")
arbol = insertar(arbol, "Medusa", "Perseo")
arbol = insertar(arbol, "Ladón", "Heracles")
arbol = insertar(arbol, "Águila del Cáucaso", "-")
arbol = insertar(arbol, "Quimera", "Belerofonte")
arbol = insertar(arbol, "Hidra de Lerna", "Heracles")
arbol = insertar(arbol, "León de Nemea", "Heracles")
arbol = insertar(arbol, "Esfinge", "Edipo")
arbol = insertar(arbol, "Dragón de la Cólquida", "-")
arbol = insertar(arbol, "Cerbero", "-")

arbol = insertar(arbol, "Cerda de Cromión", "Teseo")
arbol = insertar(arbol, "Ortro", "Heracles")
arbol = insertar(arbol, "Toro de Creta", "Teseo")
arbol = insertar(arbol, "Jabalí de Calidón", "Atalanta")
arbol = insertar(arbol, "Carcinos", "-")
arbol = insertar(arbol, "Gerión", "Heracles")
arbol = insertar(arbol, "Cloto", "-")
arbol = insertar(arbol, "Láquesis", "-")
arbol = insertar(arbol, "Átropos", "-")
arbol = insertar(arbol, "Minotauro de Creta", "Teseo")
arbol = insertar(arbol, "Harpías", "-")
arbol = insertar(arbol, "Argos Panoptes", "Hermes")
arbol = insertar(arbol, "Aves del Estínfalo", "-")
arbol = insertar(arbol, "Talos", "Medea")
arbol = insertar(arbol, "Sirenas", "-")
arbol = insertar(arbol, "Pitón", "Apolo")
arbol = insertar(arbol, "Cierva de Cerinea", "-")
arbol = insertar(arbol, "Basilisco", "-")
arbol = insertar(arbol, "Jabalí de Erimanto", "-")


# =====================================================
# B. CARGAR DESCRIPCIONES
# =====================================================

cargar_descripcion(
    arbol,
    "Talos",
    "Gigante de bronce que protegía la isla de Creta."
)

cargar_descripcion(
    arbol,
    "Medusa",
    "Criatura cuya mirada convertía en piedra."
)

cargar_descripcion(
    arbol,
    "Cerbero",
    "Perro de tres cabezas que custodiaba el inframundo."
)


# =====================================================
# A. INORDEN
# =====================================================

print("\nA. LISTADO INORDEN")
inorden(arbol)


# =====================================================
# C. INFORMACIÓN DE TALOS
# =====================================================

print("\nC. INFORMACIÓN DE TALOS")
mostrar_talos(arbol)


# =====================================================
# D. TOP 3
# =====================================================

print("\nD. TRES HÉROES O DIOSES QUE MÁS CRIATURAS DERROTARON")
mostrar_tres_mayores(arbol)


# =====================================================
# E. CRIATURAS DERROTADAS POR HERACLES
# =====================================================

print("\nE. CRIATURAS DERROTADAS POR HERACLES")
criaturas_de_heracles(arbol)


# =====================================================
# F. NO DERROTADAS
# =====================================================

print("\nF. CRIATURAS NO DERROTADAS")
no_derrotadas(arbol)


# =====================================================
# H. CAPTURAS DE HERACLES
# =====================================================

capturas_heracles(arbol)


# =====================================================
# I. BÚSQUEDA POR COINCIDENCIA
# =====================================================

print("\nI. BÚSQUEDA POR COINCIDENCIA: 'dragón'")
buscar_coincidencia(arbol, "dragón")


# =====================================================
# J. ELIMINAR BASILISCO Y SIRENAS
# =====================================================

arbol = eliminar_basilisco_y_sirenas(arbol)


# =====================================================
# K. AVES DEL ESTÍNFALO
# =====================================================

modificar_aves(arbol)


# =====================================================
# L. CAMBIAR LÁDON
# =====================================================

arbol = cambiar_ladon(arbol)


# =====================================================
# M. RECORRIDO POR NIVEL
# =====================================================

print("\nM. LISTADO POR NIVEL")
por_nivel(arbol)


# =====================================================
# N. CRIATURAS CAPTURADAS POR HERACLES
# =====================================================

print("\nN. CRIATURAS CAPTURADAS POR HERACLES")
capturadas_por_heracles(arbol)