
# Contexto: 🙌
# Muchos programas realizan cálculos entre números. La división es una operación común, pero puede romperse si los datos no están controlados correctamente.

# Consigna: ✍️
# Creá una función que:
# Pida al usuario dos números
# Intente dividir el primero por el segundo
# Maneje dos errores posibles:
# Entrada inválida (ValueError)
# División por cero (ZeroDivisionError)
# Imprima mensajes personalizados para cada uno


# Paso a paso: ⚙️
# Capturá cada excepción en un bloque separado
# Usá else para mostrar el resultado si todo salió bien
# Usá finally para imprimir siempre un cierre como “Proceso finalizado”
# Probalo con entradas correctas y con fallos para ver los resultados

# Recibir los datos del usuario


def division():
    while True:
        try:
            a = float(input("Ingresa el primer número: ")) #valueError
            b = float(input("Ingresa el segundo número: ")) #valueError
            resultado = a / b # ZeroDivisionError
            print(f"Resultado de la división: {resultado}")
        except ValueError:
            print("Error: Ingresa valores numéricos!")
            continue
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
            continue
        finally:
         print("Proceso finalizado.")
        break


division()
