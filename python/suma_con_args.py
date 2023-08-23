def sumar_con_args(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma


'''
NOTA Acerca de *args

En *args se recibe un numero indeterminado de argumentos desde cualquier
variable de tipo list o tuple
'''
numeros = [5, 10, 15, 20]
resultado = sumar_con_args(*numeros)
print("La suma de los números es:", resultado)
