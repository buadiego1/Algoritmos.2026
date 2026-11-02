from graph import Graph

personajes = [
    {'name': 'Luke Skywalker', 'episodes': [3, 4, 5, 6, 7, 8, 9]},
    {'name': 'Darth Vader', 'episodes': [1, 2, 3, 4, 5, 6]},
    {'name': 'Yoda', 'episodes': [1, 2, 3, 5, 6, 8]},
    {'name': 'Boba Fett', 'episodes': [2, 5, 6]},
    {'name': 'C-3PO', 'episodes': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {'name': 'Leia', 'episodes': [3, 4, 5, 6, 7, 8, 9]},
    {'name': 'Rey', 'episodes': [7, 8, 9]},
    {'name': 'Kylo Ren', 'episodes': [7, 8, 9]},
    {'name': 'Chewbacca', 'episodes': [3, 4, 5, 6, 7, 8, 9]},
    {'name': 'Han Solo', 'episodes': [4, 5, 6, 7]},
    {'name': 'R2-D2', 'episodes': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {'name': 'BB-8', 'episodes': [7, 8, 9]},
]

g = Graph(is_dir=False)

# A - vertices con el nombre y aristas con la cantidad de episodios compartidos
for personaje in personajes:
    g.add_vertex(personaje['name'], personaje)

for i in range(len(personajes)):
    for j in range(i + 1, len(personajes)):
        compartidos = 0
        for episode in personajes[i]['episodes']:
            if episode in personajes[j]['episodes']:
                compartidos += 1
        if compartidos > 0:
            g.add_edge(compartidos, personajes[i]['name'], personajes[j]['name'])

# B - arbol de expansion minimo desde C-3PO, Yoda y Leia
for origen in ['C-3PO', 'Yoda', 'Leia']:
    print()
    print(f'arbol de expansion minimo desde {origen}:')
    min_tree = g.kruskal(origen)
    peso_total = 0
    for edge in min_tree.split(';'):
        origin, destination, weight = edge.split('/')
        print(f'{origin} - {destination} ({weight})')
        peso_total += int(weight)
    print(f'peso total: {peso_total}')

# C - maximo de episodios compartidos y pares que coinciden
maximo = 0
for vertex in g:
    for edge in vertex.edges:
        if edge.weight > maximo:
            maximo = edge.weight

print()
print(f'maximo de episodios compartidos: {maximo}')
for vertex in g:
    for edge in vertex.edges:
        if edge.weight == maximo and vertex.value < edge.destination:
            print(f'{vertex.value} - {edge.destination}')

# D - camino mas corto de C-3PO a R2-D2 y de Yoda a Darth Vader
def camino_mas_corto(origen, destination):
    paths = g.dijkstra(origen)
    peso_total = None
    camino_completo = []

    while paths.size() > 0:
        value = paths.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]
    camino_completo.reverse()
    print(f'el camino mas corto es: {" -> ".join(camino_completo)} con un costo de {peso_total}')

print()
camino_mas_corto('C-3PO', 'R2-D2')
camino_mas_corto('Yoda', 'Darth Vader')

# E - personajes que aparecieron en los nueve episodios
print()
print('personajes que aparecieron en los nueve episodios:')
for vertex in g:
    if len(vertex.other_values['episodes']) == 9:
        print(vertex.value)
