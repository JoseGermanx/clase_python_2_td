# Definir la clase Libro con los atributos titulo, autor, anio
# Agregar un método mostrar_info() que imprima todos los datos
# Crear dos objetos Libro diferentes
# Llamar al método mostrar_info() de cada objeto

# 📌 Objetivo: reforzar cómo se usan múltiples atributos, cómo funcionan los métodos, y cómo crear varios objetos con datos distintos.

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        print("---Datos del libro---")
        print(f"Título: {self.titulo}.")
        print(f"Autor: {self.autor}.")
        print(f"Año: {self.anio} ")

#Instancias

libro_1 = Libro("1984", "George Orwell", 1949)
libro_2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)

libro_1.anio = 1950

libro_1.mostrar_info()
libro_2.mostrar_info()