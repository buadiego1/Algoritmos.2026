# EJERCICIO 5 - N REINAS (backtracking)
# Colocar n reinas en un tablero de n x n sin que se amenacen.
# Se coloca una reina por fila; reinas[fila] = columna donde está la reina.
# Dos reinas se amenazan si están en la misma columna o en la misma diagonal
# (la distancia entre filas es igual a la distancia entre columnas).


def es_valida(reinas: list, fila: int, columna: int) -> bool:
    for fila_anterior in range(fila):
        columna_anterior = reinas[fila_anterior]
        if columna_anterior == columna:
            return False
        if abs(columna_anterior - columna) == abs(fila_anterior - fila):
            return False
    return True


def colocar_reinas(reinas: list, fila: int, n: int) -> bool:
    # caso base: ya se colocaron las n reinas
    if fila == n:
        return True
    else:
        for columna in range(n):
            if es_valida(reinas, fila, columna):
                reinas[fila] = columna
                if colocar_reinas(reinas, fila + 1, n):
                    return True
                # vuelta atrás: se quita la reina y se prueba la siguiente columna
                reinas[fila] = -1
        return False


def n_reinas(n: int) -> list:
    reinas = [-1] * n
    if colocar_reinas(reinas, 0, n):
        return reinas
    return None


def mostrar_tablero(reinas: list) -> None:
    n = len(reinas)
    for fila in range(n):
        linea = ''
        for columna in range(n):
            if reinas[fila] == columna:
                linea += ' R'
            else:
                linea += ' .'
        print(linea)


for n in [4, 8, 16]:
    solucion = n_reinas(n)
    print(f'{n} reinas en tablero de {n} x {n}')
    print('columna de la reina en cada fila:', solucion)
    mostrar_tablero(solucion)
    print()