
# Vas a abrir un archivo de texto y leerlo usando los tres métodos principales, observando qué devuelve cada uno.

# Abrí el archivo "prueba_2.txt" en modo lectura ("r")
# Probá cada método por separado:
# Usá read() y mostrale el contenido completo
# Volvé a abrir el archivo y usá readline() para leer línea por línea
# Volvé a abrirlo y usá readlines() para guardar todas las líneas en una lista
# Mostrá los resultados por consola

# 🔹 Qué observar:



# read() trae todo como un solo string
archivo = open("ARCHIVOS/prueba_2.txt", "r")

contenido = archivo.read() #leer todo el contenido y lo almacena como str
archivo.close()

#print(contenido)

# readline() devuelve una línea a la vez (se puede iterar)
archivo = open("ARCHIVOS/prueba_2.txt", "r")
linea = archivo.readline()
while linea:
    #print(linea)
    linea = archivo.readline()
archivo.close()


# readlines() devuelve una lista de líneas

archivo = open("ARCHIVOS/prueba_2.txt", "r")
lineas = archivo.readlines()

for linea in lineas:
    print(linea)