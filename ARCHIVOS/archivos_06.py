# Vas a intentar abrir un archivo que puede no existir, manejar el error si ocurre, y garantizar siempre el cierre del recurso.

# Intentar abrir un archivo llamado "archivo_seguro.txt" en modo lectura ("r")
# Capturar la excepción FileNotFoundError si el archivo no existe
# Usar un bloque finally para intentar cerrar el archivo si fue abierto correctamente
# Mostrar un mensaje al final indicando el cierre

# 🔹 Qué observar:

# El flujo normal cuando el archivo existe

# El manejo del error si el archivo no está

# El cierre garantizado sin importar el resultado
archivo = None
ruta_archivo = "archivo_seguro.txt"


try:
    archivo = open(ruta_archivo, "r")
    contenido = archivo.read()
    print("Imprimiendo contenido del archivo.")
    print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    print("Terminando proceso.... verificando archivos para cerrar...")
    if archivo is not None:
        archivo.close()
        if archivo.closed:
            print(f"Archivo {archivo.name} cerrado correctamente.")
    else:
        print("No hay archivo para cerrar.")
