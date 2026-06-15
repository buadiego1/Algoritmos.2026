#EJ 10


class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, item): 
        self.items.append(item)
        
    def desencolar(self): 
        return self.items.pop(0) if not self.esta_vacia() else None
        
    def esta_vacia(self): 
        return len(self.items) == 0
    
    # Método auxiliar solo para visualizar la cola en este ejemplo
    def mostrar_estado(self):
        for item in self.items:
            print(f"  [{item['hora']}] {item['app']}: {item['mensaje']}")

class Pila:
    def __init__(self):
        self.items = []
        
    def apilar(self, item): 
        self.items.append(item)
        
    def desapilar(self): 
        return self.items.pop() if not self.esta_vacia() else None
        
    def esta_vacia(self): 
        return len(self.items) == 0


#A.escribir una función que elimine de la cola todas las notificaciones de Facebook;
def eliminar_facebook(cola_notificaciones):
    cola_aux = Cola()
    
    while not cola_notificaciones.esta_vacia():
        notificacion = cola_notificaciones.desencolar()
        if notificacion["app"] != "Facebook":
            cola_aux.encolar(notificacion)
            
    while not cola_aux.esta_vacia():
        cola_notificaciones.encolar(cola_aux.desencolar())


#B.escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
def mostrar_twitter_python(cola_notificaciones):
    cola_aux = Cola()
    
    while not cola_notificaciones.esta_vacia():
        notificacion = cola_notificaciones.desencolar()
        
        if notificacion["app"] == "Twitter" and "Python" in notificacion["mensaje"]:
            print(f"  -> [{notificacion['hora']}] {notificacion['mensaje']}")
            
        cola_aux.encolar(notificacion)
        
    while not cola_aux.esta_vacia():
        cola_notificaciones.encolar(cola_aux.desencolar())


#C.utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son. 
def contar_rango_horario(cola_notificaciones):
    pila_temp = Pila()
    cola_aux = Cola()
    
    while not cola_notificaciones.esta_vacia():
        notificacion = cola_notificaciones.desencolar()
        
        if "11:43" <= notificacion["hora"] <= "15:57":
            pila_temp.apilar(notificacion)
            
        cola_aux.encolar(notificacion)
        
    while not cola_aux.esta_vacia():
        cola_notificaciones.encolar(cola_aux.desencolar())
        
    cantidad = 0
    while not pila_temp.esta_vacia():
        pila_temp.desapilar()
        cantidad += 1
        
    return cantidad


# EJECUCIÓN
if __name__ == "__main__":
    # Creamos la cola y cargamos datos de prueba
    mi_cola = Cola()
    
    notificaciones_prueba = [
        {"hora": "10:15", "app": "Facebook", "mensaje": "Juan comentó tu foto."},
        {"hora": "11:50", "app": "Twitter", "mensaje": "Nuevo tutorial de Python disponible."},
        {"hora": "12:30", "app": "Instagram", "mensaje": "A María le gusta tu reel."},
        {"hora": "14:20", "app": "Twitter", "mensaje": "Me encanta programar en Java."}, # Twitter, pero sin 'Python'
        {"hora": "15:00", "app": "Facebook", "mensaje": "Tienes un nuevo recuerdo de hace 2 años."},
        {"hora": "15:50", "app": "Twitter", "mensaje": "Buscando trabajo como desarrollador Python..."},
        {"hora": "16:10", "app": "WhatsApp", "mensaje": "Mensaje de mamá."}
    ]
    
    for n in notificaciones_prueba:
        mi_cola.encolar(n)

    print("=== ESTADO INICIAL DE LA COLA ===")
    mi_cola.mostrar_estado()
    print("\n" + "-"*50 + "\n")

    # Ejecución Punto B (Lo hacemos antes del A para ver todas las notificaciones originales)
    print("=== PUNTO B: Mostrando notificaciones de Twitter con 'Python' ===")
    mostrar_twitter_python(mi_cola)
    print("\n" + "-"*50 + "\n")

    # Ejecución Punto C (También antes del A, para contar las de Facebook en ese horario)
    print("=== PUNTO C: Contando notificaciones entre 11:43 y 15:57 ===")
    cantidad_rango = contar_rango_horario(mi_cola)
    print(f"  -> Total de notificaciones en ese rango horario: {cantidad_rango}")
    print("\n" + "-"*50 + "\n")

    # Ejecución Punto A
    print("=== PUNTO A: Eliminando notificaciones de Facebook ===")
    eliminar_facebook(mi_cola)
    print("  -> Eliminación completa. Estado actual de la cola:")
    mi_cola.mostrar_estado()
    print("\n" + "="*50)

#EJ 22


from collections import deque

# 1. Definimos la cola y la llenamos con datos de ejemplo del MCU
cola_mcu = deque([
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"personaje": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
    {"personaje": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"}
])

def procesar_cola_mcu(cola):
    # Variables auxiliares para guardar los resultados solicitados
    nombre_capitana_marvel = None
    superheroes_femeninos = []
    personajes_masculinos = []
    superheroe_scott_lang = None
    empiezan_con_s = []
    carol_danvers_en_cola = False
    superheroe_carol_danvers = None

    # Guardamos el tamaño original para procesar exactamente todos los elementos una vez
    tamaño_cola = len(cola)

    # Procesamos la cola
    for _ in range(tamaño_cola):
        # Desencolamos el primer elemento
        elemento = cola.popleft()

        personaje = elemento["personaje"]
        superheroe = elemento["superheroe"]
        genero = elemento["genero"]

        # a. determinar el nombre del personaje de la superhéroe Capitana Marvel
        if superheroe == "Capitana Marvel":
            nombre_capitana_marvel = personaje

        # b. mostrar los nombres de los superhéroes femeninos
        if genero == "F":
            superheroes_femeninos.append(superheroe)

        # c. mostrar los nombres de los personajes masculinos
        if genero == "M":
            personajes_masculinos.append(personaje)

        # d. determinar el nombre del superhéroe del personaje Scott Lang
        if personaje == "Scott Lang":
            superheroe_scott_lang = superheroe

        # e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con 'S'
        if personaje.startswith("S") or superheroe.startswith("S"):
            empiezan_con_s.append(elemento)

        # f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su superhéroe
        if personaje == "Carol Danvers":
            carol_danvers_en_cola = True
            superheroe_carol_danvers = superheroe

        # Volvemos a encolar el elemento para no perder la información original
        cola.append(elemento)

    #Resultados
    print("-" * 40)
    print("RESULTADOS DEL ANÁLISIS DE LA COLA")
    print("-" * 40)
    
    # a
    print(f"a. Personaje de Capitana Marvel: {nombre_capitana_marvel}")
    
    # b
    print("\nb. Nombres de superhéroes femeninos:")
    for heroina in superheroes_femeninos:
        print(f"   - {heroina}")
        
    # c
    print("\nc. Nombres de personajes masculinos:")
    for hombre in personajes_masculinos:
        print(f"   - {hombre}")
        
    #d
    print(f"\nd. Superhéroe de Scott Lang: {superheroe_scott_lang}")
    
    # e
    print("\ne. Datos de personajes o superhéroes que comienzan con 'S':")
    for s_char in empiezan_con_s:
        print(f"   - Personaje: {s_char['personaje']} | Superhéroe: {s_char['superheroe']} | Género: {s_char['genero']}")
        
    #f
    print("\nf. ¿Está Carol Danvers en la cola?")
    if carol_danvers_en_cola:
        print(f"   Sí, se encuentra en la cola. Su superhéroe es: {superheroe_carol_danvers}")
    else:
        print("   No, no se encuentra en la cola.")
    print("-" * 40)

# Ejecuto la función
procesar_cola_mcu(cola_mcu)