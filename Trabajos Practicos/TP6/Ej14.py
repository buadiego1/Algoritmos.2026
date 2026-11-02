# EJERCICIO 14 - MÉTODO DE LA BISECCIÓN (iterativo)
# Busca una raíz de f(x) en el intervalo [a, b].
# Condición: f(a) y f(b) deben tener signos distintos (f(a) * f(b) < 0),
# así por el teorema de Bolzano hay al menos una raíz en el intervalo.
# En cada iteración se calcula el punto medio y se descarta la mitad
# del intervalo donde no cambia el signo.


def biseccion(f, a: float, b: float, tolerancia: float = 1e-6, max_iteraciones: int = 100) -> float:
    if f(a) * f(b) > 0:
        print('f(a) y f(b) deben tener signos distintos')
        return None

    iteracion = 0
    medio = (a + b) / 2
    while (b - a) / 2 > tolerancia and iteracion < max_iteraciones:
        medio = (a + b) / 2
        if f(medio) == 0:
            # se encontró la raíz exacta
            return medio
        elif f(a) * f(medio) < 0:
            # la raíz está en la mitad izquierda
            b = medio
        else:
            # la raíz está en la mitad derecha
            a = medio
        iteracion += 1
        print(f'iteración {iteracion}: a={a:.6f}  b={b:.6f}  medio={medio:.6f}')

    return (a + b) / 2


# ejemplo 1: f(x) = x^2 - 2  ->  raíz = raíz cuadrada de 2 (1.414213...)
def f1(x: float) -> float:
    return x ** 2 - 2

raiz = biseccion(f1, 0, 2)
print('raíz de x^2 - 2 en [0, 2]:', raiz)
print()

# ejemplo 2: f(x) = x^3 - x - 2  ->  raíz aproximada 1.5213797
def f2(x: float) -> float:
    return x ** 3 - x - 2

raiz = biseccion(f2, 1, 2, tolerancia=1e-4)
print('raíz de x^3 - x - 2 en [1, 2]:', raiz)