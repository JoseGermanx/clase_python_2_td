# Definir una clase simple llamada Animal con atributo nombre y método hablar()
# Crear una instancia de Animal llamada mi_gato
# Ejecutar un método desde la instancia
# Comprobar con isinstance() que mi_gato es una instancia de Animal
# Mostrar que una instancia tiene vida propia y puede almacenarse, pasarse como parámetro, o guardarse en listas

# 📌 Objetivo: entender que una instancia es un objeto real creado a partir de una clase, y que puede verificarse con herramientas como isinstance().

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"Soy {self.nombre} y puedo hablar.")

mi_gato = Animal("Lucas")

mi_gato.hablar()

print("¿El objeto es instacnia de la clase?: ", isinstance(mi_gato, Animal))

# Mostrar que una instancia tiene vida propia y puede almacenarse, pasarse como parámetro, o guardarse en listas

animales = []

animales.append(mi_gato)

def presentar_animal(animal):
    animal.hablar()

presentar_animal(mi_gato)