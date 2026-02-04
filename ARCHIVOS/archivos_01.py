# Vas a abrir un archivo de texto en modo lectura, leer todo su contenido y luego cerrarlo manualmente.

# Usar open() en modo "r" para abrir un archivo llamado "prueba.txt"
# Leer el contenido usando read()
# Imprimir el contenido en consola
# Cerrar el archivo usando close()

# 🔹 Observaciones importantes:

# Si el archivo no existe, Python lanzará un FileNotFoundError

# Verificar si el archivo realmente se cerró con archivo.closed
try:
    archivo = open("ARCHIVOS/prueba.txt", "r")
    contenido = archivo.read()
    # archivo.close()
    print(contenido)
    print("===========================")
    print("===========================")
    contenido_2 = archivo.read() # no se puede acceder porque el archivo ya fue cerrado (line16)
    print(contenido_2)
    print(f"Verificar si archivo está cerrado: {archivo.closed}")

except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    archivo.close()
    print(f"Verificar si archivo está cerrado: {archivo.closed}")
