

entrada = input("Ingresa un número entero: ")

try:
    numero = int(entrada) #ValueError
    print(f"Número válido: {numero}")
except ValueError:
    print("Error: debes ingresar un número válido.")





print("Fin del proceso")