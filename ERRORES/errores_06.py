class ErrorEdadInvalida(Exception):
    pass


def validar_edad(edad):
    if edad < 0:
        raise ErrorEdadInvalida("La edad no puede ser negativa.")
    return edad


try:
    print(f"La edad es válida: {validar_edad(-3)}")
except ErrorEdadInvalida as error:
    print(f"Hubo un error:{error} ")