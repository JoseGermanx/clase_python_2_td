# Contexto: 🙌
# Estás creando una herramienta que permita a los usuarios inspeccionar archivos locales. El objetivo es obtener información del archivo y mostrar su contenido de manera distinta según su tamaño, usando buenas prácticas de manejo de archivos en Python.

# Consigna: ✍️
# Implementá un programa en Python que:
# Solicite al usuario el nombre de un archivo
# Abra el archivo en modo lectura ("r")
# Obtenga y muestre:
# Nombre del archivo (.name)
# Modo de apertura (.mode)
# Estado de cierre (.closed)
# Tamaño en bytes usando os.stat()
# Lea el contenido:
# Si el archivo pesa menos de 500 bytes → leé todo el contenido con read()
# Si pesa más de 500 bytes → leé línea por línea con readline()
# Asegurate de cerrar el archivo y mostrar que fue cerrado correctamente
# Usá try/except para manejar errores si el archivo no existe

# Paso a paso: ⚙️
# Importar el módulo os
# Solicitar al usuario la ruta o nombre del archivo
# Intentar abrir el archivo en modo "r" usando try/except
# Mostrar atributos básicos del archivo (name, mode, closed)
# Obtener el tamaño usando os.stat().st_size

# Según el tamaño:
# Si es pequeño → leer todo con read()
# Si es grande → usar readline() en un bucle
# Cerrar el archivo
# Confirmar que el archivo está cerrado (.closed)
# En caso de error (archivo no encontrado), mostrar un mensaje claro al usuario

import os


print("=====Buscador de archivos .txt========")
nombre_archivo = input("Ingrese el nombre del archivo sin extensión: ")

ruta_archivo = f"ARCHIVOS/{nombre_archivo}.txt"

try:
    #lógica para abrir y mostrar información del archivo
    archivo = open(ruta_archivo, "r")
    print(f"Nombre: {archivo.name}")
    print(f"Nombre: {archivo.mode}")
    print(f"Nombre: {archivo.closed}")

    size = os.stat(ruta_archivo).st_size
    print(f"Tamaño: {size} bytes")

    #lógica según el tamaño
    if size < 500:
        contenido = archivo.read()
        print(contenido)
    else:
        linea = archivo.readline()
        while linea:
            print(linea)
            linea = archivo.readline()
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
     if "archivo" in locals():
         archivo.close()
         print(f"Cerrado: {archivo.closed}")
         print("Archivo cerrado correctamente.")
      