def sumar_con_kwargs(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        suma += value
    return suma


'''
NOTA Acerca de **kwargs

En **kwargs se recibe un numero indeterminado de argumentos desde cualquier
variable de tipo dict
'''
valores = {
    'numero1': 5,
    'numero2': 10,
    'numero3': 15,
    'numero4': 20
}
resultado = sumar_con_kwargs(**valores)
print("La suma de los números es:", resultado)
