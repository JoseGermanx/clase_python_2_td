
archivo = None

try:
    print("Intentando abrir el archivo")
    archivo = open("ERRORES/info.txt", "r")
    contenido = archivo.read()
    print("El contenido del archivo es: ")
    print(contenido)
except FileNotFoundError:
    print("No se encontró el archivo en esa ubicación")
finally:
    if archivo:
        archivo.close()
        print("Archivo cerrando!!")
    print("Proceso finalizado!!")