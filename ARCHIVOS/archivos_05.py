# Vas a abrir y leer un archivo usando la estructura with, garantizando que se cierre automáticamente.

# Crear o usar un archivo existente llamado "lectura_segura.txt"
# Abrirlo usando with open("lectura_segura.txt", "r") as archivo
# Leer el contenido con read()
# Imprimir el contenido en pantalla
# Verificar si el archivo está cerrado después del bloque (archivo.closed)


# 🔹 Qué observar:

# El archivo se cierra automáticamente al salir del bloque with

# No es necesario llamar manualmente a close()

ruta_archivo = "lectura_segura.txt"

with open(ruta_archivo, "w") as archivo_1:
    archivo_1.write("Hola mundo desde archivo de lectura segura.")
    print("File", archivo_1.fileno())


print("Cerrado: ", archivo_1.closed)

with open(ruta_archivo, "r") as archivo_2:
    contenido = archivo_2.read()
    print(contenido)
    print("File", archivo_2.fileno())

print("Cerrado: ", archivo_2.closed)