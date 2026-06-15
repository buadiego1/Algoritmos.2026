#Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.

def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)
print (fibo(6))

#Implementar una función que calcule la suma de todos los números enteros comprendidos
# entre cero y un número entero positivo dado.
def fun(suma):
    if suma == 0:
        return 0
    else:
        return suma + fun(suma-1)
print(fun(5))

#Implementar una función para calcular el producto de dos números enteros dados.
def prod(a,b):
    if a == 0 or b== 0:
        return 0
    else:
        return a + prod (a,b-1)
print (prod(5,5))


#18. Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.
def mat(matriz,fila=0,col=0):
    if fila == len(matriz):
        return 
    print (matriz[fila][col])
    
    if (col+1) < len(matriz[fila]):
        mat(matriz, fila, col + 1)
    else:
        mat(matriz, fila + 1, 0)

mi_matriz= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print (mat(mi_matriz))

#Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
def bin(n):
    if n > 1:
        bin(n // 2)  # Llamada recursiva con el cociente
    print(n % 2)  # Imprime el resto

numero = 25
print(f"El número {numero} en binario es: ")
bin(numero)