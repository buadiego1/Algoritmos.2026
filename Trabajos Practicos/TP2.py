#Ejercicio 20

def registrar_movimientos():

    pila_movimientos = []
    
    print("--- INICIO DE REGISTRO ---")
    print("Direcciones: N, S, E, O, NE, NO, SE, SO (Escriba 'FIN' para salir)")
    
    while True:
        direccion = input("\nDirección: ").upper()
        
        if direccion == "FIN":
            break
            
        pasos = int(input("Cantidad de pasos: "))
        
        pila_movimientos.append([pasos, direccion])
        
    return pila_movimientos

def vuelta(pila_ida):
    opuestos = {
        "N": "S", "S": "N", "E": "O", "O": "E",
        "NE": "SO", "NO": "SE", "SE": "NO", "SO": "NE"
    }
    
    print("\n--- GENERANDO CAMINO DE REGRESO ---")
    
    while len(pila_ida) > 0:
        ultimo_movimiento = pila_ida.pop()
        
        pasos = ultimo_movimiento[0]
        direccion_ida = ultimo_movimiento[1]
        
        direccion_vuelta = opuestos[direccion_ida]
        
        print(f"Mover {pasos} pasos hacia el {direccion_vuelta}")
        
# Paso 1: El robot se mueve y se registra
recorrido = registrar_movimientos()

# Paso 2: El robot vuelve al origen usando la pila
if len(recorrido) > 0:
    vuelta(recorrido)
else:
    print("No se registraron movimientos.")




#Ejercicio 24

class Pila:
    def __init__(self):
        self.datos = []

    def apilar(self, elemento):
        self.datos.append(elemento)

    def desapilar(self):
        return self.datos.pop()

    def vacia(self):
        return len(self.datos) == 0


# a
def posicion_personajes(pila):
    aux = Pila()
    pos = 1
    rocket = None
    groot = None

    while not pila.vacia():
        personaje = pila.desapilar()

        if personaje["nombre"] == "Rocket Raccoon":
            rocket = pos
        if personaje["nombre"] == "Groot":
            groot = pos

        aux.apilar(personaje)
        pos += 1

    # restaurar pila
    while not aux.vacia():
        pila.apilar(aux.desapilar())

    return rocket, groot


# b
def mas_de_5(pila):
    aux = Pila()
    resultado = []

    while not pila.vacia():
        personaje = pila.desapilar()

        if personaje["peliculas"] > 5:
            resultado.append((personaje["nombre"], personaje["peliculas"]))

        aux.apilar(personaje)

    while not aux.vacia():
        pila.apilar(aux.desapilar())

    return resultado


# c
def black_widow(pila):
    aux = Pila()
    peliculas = 0

    while not pila.vacia():
        personaje = pila.desapilar()

        if personaje["nombre"] == "Black Widow":
            peliculas = personaje["peliculas"]

        aux.apilar(personaje)

    while not aux.vacia():
        pila.apilar(aux.desapilar())

    return peliculas


# d
def iniciales(pila):
    aux = Pila()
    resultado = []

    while not pila.vacia():
        personaje = pila.desapilar()

        if personaje["nombre"][0] in ["C", "D", "G"]:
            resultado.append(personaje["nombre"])

        aux.apilar(personaje)

    while not aux.vacia():
        pila.apilar(aux.desapilar())

    return resultado

pila = Pila()

pila.apilar({"nombre": "Iron Man", "peliculas": 10})
pila.apilar({"nombre": "Groot", "peliculas": 6})
pila.apilar({"nombre": "Captain America", "peliculas": 9})
pila.apilar({"nombre": "Rocket Raccoon", "peliculas": 5})
pila.apilar({"nombre": "Black Widow", "peliculas": 8})
pila.apilar({"nombre": "Doctor Strange", "peliculas": 4})


# a
rocket, groot = posicion_personajes(pila)
print("a) Rocket:", rocket)
print("a) Groot:", groot)

# b
print("b) Más de 5 películas:")
for nombre, cant in mas_de_5(pila):
    print(nombre, cant)

# c
print("c) Black Widow:", black_widow(pila))

# d
print("d) Iniciales C, D, G:")
for nombre in iniciales(pila):
    print(nombre)