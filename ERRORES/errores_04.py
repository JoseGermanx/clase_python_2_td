

entrada = input("Ingresa un número entero: ")

try:
    numero = int(entrada) #ValueError
    10/numero
    print(f"Número válido: {numero}")
except Exception as e:
    print(e)





print("Fin del proceso")