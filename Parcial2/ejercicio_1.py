from random import shuffle

from pokemon_data import pokemons
from tree import BinaryTree

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

# carga aleatoria
shuffle(pokemons)

print(f'cantidad de pokemons: {len(pokemons)}')
for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['name'], pokemon)
    arbol_numero.insert_node(pokemon['number'], pokemon)
    for tipo in pokemon['types']:
        node = arbol_tipo.search(tipo)
        if node is None:
            arbol_tipo.insert_node(tipo, [pokemon['name']])
        else:
            node.other_values.append(pokemon['name'])

# B - datos de un pokemon por numero y por nombre (proximidad)
print()
numero = int(input('ingrese el numero del pokemon: '))
node = arbol_numero.search(numero)
if node is not None:
    print(node.other_values)
else:
    print('no encontrado')

print()
search_str = input('ingrese el nombre (o parte) del pokemon: ')
arbol_nombre.proxy_search_pokemon(search_str.lower())

# C - nombres de pokemons de un tipo
for tipo in ['fantasma', 'fuego', 'acero', 'eléctrico']:
    print()
    print(f'pokemons de tipo {tipo}:')
    node = arbol_tipo.search(tipo)
    if node is not None:
        for name in node.other_values:
            print(name)

# D - listado ascendente por numero, por nombre y por nivel por nombre
print()
print('listado por numero:')
arbol_numero.inorden_pokemon()

print()
print('listado por nombre:')
arbol_nombre.inorden_pokemon()

print()
print('listado por nivel por nombre:')
arbol_nombre.by_level()

# E - pokemons debiles frente a Jolteon, Lycanroc y Tyrantrum
for name in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    print()
    node = arbol_nombre.search(name)
    if node is not None:
        print(f'debiles frente a {name} {node.other_values["types"]}:')
        arbol_numero.inorden_weak_against(node.other_values['types'])

# F - tipos y cantidad de pokemons de cada tipo
print()
print('cantidad de pokemons por tipo:')
arbol_tipo.inorden_count_types()

# G - cantidad con megaevolucion
print()
print(f'cantidad de pokemons con megaevolucion: {arbol_numero.count_pokemon("mega")}')

# H - cantidad con forma gigamax
print(f'cantidad de pokemons con forma gigamax: {arbol_numero.count_pokemon("gigamax")}')
