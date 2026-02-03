# Contexto: 🙌
# En una aplicación de cálculo de distancias, necesitamos convertir kilómetros a millas. Sin embargo, la entrada del usuario no siempre es válida, y puede generar errores si no se maneja correctamente.

# Consigna: ✍️
# Implementá un programa en Python que:
# Solicite al usuario una distancia en kilómetros
# Verifique si la entrada es numérica válida
# Convierta el valor a millas (1 km = 0.621371 mi)
# Muestre un mensaje de error si el valor ingresado no es un número

# Paso a paso: ⚙️
# Usá un bloque try/except para capturar ValueError
# Si es válida, hacé la conversión y mostrala con 2 decimales
# Si falla, mostrale un mensaje amable al usuario
# Podés usar un bucle para reintentar hasta que ingrese bien

FACTOR_MILLAS = 0.621371


print("Bienvenido al conversor de unidades (km -> millas)")
while True:
    try:
        km = float(input("Ingresa el valor en kilómetros: "))
        millas = km * FACTOR_MILLAS
        print(F"{km} km equivalen a {millas:.2f} millas.")
        print("Gracias por utilizar esta app.")
        break
    except ValueError:
        print(f"Error: Ingrese un número válido.")
