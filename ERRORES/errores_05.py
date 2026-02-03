# ¿En qué consistirá la Demo?
# Vas a crear una función que recibe una edad, y lanza una excepción si el valor ingresado no es válido.

#  Objetivo funcional:

# Controlar que la edad sea un número positivo
# Lanzar una excepción con un mensaje personalizado si no se cumple

# 🔹 Pasos esperados:

# Definí una función validar_edad(edad)
# Usá raise ValueError("La edad no puede ser negativa") si la edad es menor a 0
# Si la edad es válida, imprimí un mensaje como “Edad válida: X años”
# Probalo con validar_edad(25) y luego con validar_edad(-3)

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    return edad


try:
    print(f"La edad es válida: {validar_edad(-3)}")
except ValueError as error:
    print(f"Hubo un error:{error} ")