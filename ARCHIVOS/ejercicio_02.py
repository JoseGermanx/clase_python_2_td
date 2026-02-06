# Contexto: 🙌
# Queremos desarrollar una mini herramienta en Python que permita escribir datos en un archivo, moverlo a una carpeta nueva y garantizar su manejo seguro, contemplando posibles errores.

# Consigna: ✍️
# Implementá un programa en Python que:
# Solicite al usuario un nombre de archivo y un contenido para escribir
# Cree o sobrescriba el archivo usando with open() en modo "w"
# Escriba el contenido proporcionado
# Cree una carpeta llamada "backup" si no existe (usá os.makedirs())
# Mueva el archivo a la carpeta "backup/" usando shutil.move()
# Utilice try/except/finally para:
# Capturar posibles errores (FileNotFoundError, PermissionError)
# Garantizar el cierre correcto del archivo y mostrar un mensaje final

# Paso a paso: ⚙️
# Pedir el nombre del archivo y el contenido al usuario

# Escribir el contenido en el archivo usando with open()

# Crear la carpeta "backup" si no existe (os.makedirs("backup", exist_ok=True))

# Mover el archivo recién creado a "backup/"

# Asegurarse de capturar cualquier error que ocurra

# Mostrar un mensaje final como "Operación finalizada" en un bloque finally

import os
import shutil

carpeta_detino = "backup"

print("Sistema de creación de archivos de texto")
nombre_archivo = input("Ingresa el nombre del archivo: ")
contenido_archivo = input("Ingresa el contenido de tu documento de texto: ")

try:
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido_archivo)
        print("Archivo escrito correctamente.")

    os.makedirs(carpeta_detino, exist_ok=True)

    shutil.move(nombre_archivo, carpeta_detino)
    print("Archivo movido correctamente.")

    print(archivo.closed)

except FileNotFoundError:
    print("Archivo no encontrado.")

except PermissionError as error:
    print("No tienes permisos para ejecutar esta acción: ", error)
finally:
    if archivo is not archivo.closed:
        archivo.close()
        print("Archivo cerrado correctamente.")
    print("Gracias por utilizar el gestor de documentos de texto.")