# Vas a trabajar con un archivo existente, primero cambiándole el nombre y luego trasladándolo a una carpeta diferente.

# Crear un archivo llamado "demo_archivo.txt" si no existe
# Usar os.rename() para renombrarlo a "archivo_renombrado.txt"
# Crear manualmente una carpeta llamada "nueva_carpeta"
# Usar shutil.move() para mover "archivo_renombrado.txt" a "nueva_carpeta/"

# 🔹 Qué observar:

# El archivo ya no estará en su carpeta original

# Si la carpeta destino no existe, shutil.move() lanzará un error

import os
import shutil
#definiciones de nombres del archivo
nombre_original = "demo_archivo.txt"
nombre_renombrado = "archivo_renombrado.txt"

CARPETA_DETINO = "nueva_carpeta"

#crear un nuevo archivo
with open(nombre_original, "w") as archivo:
    archivo.write("Archivo de prueba.")

#renombrar el archivo
os.rename(nombre_original, nombre_renombrado)

#verifica si la nueva carpeta exite y si no existe, la crea
if not os.path.exists(CARPETA_DETINO):
    os.mkdir(CARPETA_DETINO)

#se mueve el archivo renombrado a la carpeta
shutil.move(nombre_renombrado, CARPETA_DETINO)