# ¿En qué consistirá la Demo?
# Vas a implementar una clase base Persona y una subclase Empleado que herede de ella y agregue comportamiento específico.

# 🔹 Qué debe tener la clase Persona:

# Atributos: nombre, edad
# Método: presentarse() que imprima una presentación básica

# 🔹 Qué debe tener la subclase Empleado:
# Atributo adicional: cargo
# Método sobrescrito presentarse() que además incluya el cargo
# Método adicional: trabajar() que imprima lo que hace

#  Qué se debe probar:

# Crear una instancia de Empleado

# Verificar que puede usar métodos heredados y propios

# Llamar a presentarse() y observar cómo cambia el comportamiento

#superclase
class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


# herencia
class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad) # se incluyen los atributos del constructor de la superclase
        self.cargo = cargo # atributo adicional

    #método heredado y sobreescrito
    def presentarse(self):
        #return super().presentarse()
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y trabajo como {self.cargo}")

    # método propio
    def trabajar(self):
        print(f"{self.nombre} trabaja como {self.cargo}")

trabajador_1 = Empleado("Ana", 30, "Desarrolladora")

trabajador_1.presentarse()
trabajador_1.trabajar()