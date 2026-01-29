# ¿En qué consistirá la Demo?
# Vas a implementar una clase base con un método común, y dos subclases que sobrescriben ese método de forma distinta.

# 🔹 Clase base Animal:
# Atributo: nombre
# Método: emitir_sonido() que imprima "Sonido genérico"

# 🔹 Subclases Perro y Gato:
# Sobrescriben emitir_sonido() para imprimir:
# "Guau!" en Perro
# "Miau!" en Gato

#  Qué se debe probar:
# Crear un objeto de cada subclase
# Llamar a emitir_sonido() desde cada uno
# Verificar que el comportamiento es distinto, aunque el método se llama igual

class Animal:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

    def emitir_sonido(self):
        print("Sonido Genérico")


class Perro(Animal):
    def emitir_sonido(self):
        print("Guauuu!")

class Gato(Animal):
    def emitir_sonido(self):
        print("Miaau")


perro = Perro("Firulai", "patio")
gato = Gato("Michi", "techo")

perro.emitir_sonido()
gato.emitir_sonido()

print(perro.__dict__)