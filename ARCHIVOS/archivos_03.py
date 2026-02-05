# ¿En qué consistirá la Demo?
# Vas a abrir un archivo nuevo, escribir texto línea por línea con write() y luego usar writelines() para agregar más líneas.


# Abrir un archivo llamado "demo_escritura.txt" en modo "w"
# Escribir un par de líneas usando write()
# Crear una lista de textos y escribirla usando writelines()
# Cerrar automáticamente el archivo usando with open()

# 🔹 Qué observar:

# write() necesita agregar manualmente \n para los saltos de línea

with open("demo_escritura.txt", "w") as archivo:
    archivo.write("Bienvenidos\n")
    archivo.write("Hola mundo de nuevo\n")

# writelines() escribe todos los elementos tal como están, no agrega saltos de línea automáticamente
    lineas = [
    "Tercera linea\n",
    "Cuarta Linea\n"
    ]

    archivo.writelines(lineas)