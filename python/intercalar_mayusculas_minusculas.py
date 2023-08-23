def intercalar_mayusculas_minusculas(cadena):
    resultado = ""
    mayuscula = True  # Empezamos con mayúscula

    for caracter in cadena:
        if caracter.isalpha():  # Si es una letra
            if mayuscula:
                resultado += caracter.upper()
            else:
                resultado += caracter.lower()

            mayuscula = not mayuscula  # Cambiamos para el siguiente caracter
        else:
            resultado += caracter  # Mantenemos caracteres no alfabéticos

    return resultado


cadena_original = input("Ingrese una cadena: ")
cadena_transformada = intercalar_mayusculas_minusculas(cadena_original)
print("Cadena transformada:", cadena_transformada)
