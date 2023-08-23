def sumar_con_args(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma


numeros = [5, 10, 15, 20]
resultado = sumar_con_args(*numeros)
print("La suma de los números es:", resultado)
