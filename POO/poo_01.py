# Definir una clase Persona con el método especial __init__()
# Asignar atributos: nombre, edad
# Crear el método presentarse() que imprima una presentación
# Instanciar dos objetos diferentes con datos propios
# Ejecutar el método presentarse() desde cada objeto
# Ver cómo cada objeto mantiene su propio estado
# Bonus: Agregar otro método, como cumplir_anios() que sume 1 a la edad

# 📌 Objetivo: visualizar cómo una clase puede generar múltiples objetos, cada uno con su identidad y comportamiento.

#declaración de la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1


#instancias
persona_1 = Persona("Ana", 30)
persona_2 = Persona("Alberto", 40)

persona_1.presentarse()
persona_2.presentarse()

persona_1.cumplir_anios()
persona_1.presentarse()