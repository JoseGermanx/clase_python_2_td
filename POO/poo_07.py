# ¿En qué consistirá la Demo?
# Vas a diseñar una clase que modele un empleado, incorporando tanto un método de clase como uno estático para aplicar distintos tipos de comportamiento.


# 🔹 Lo que deberá tener la clase:
# Atributos públicos como nombre y salario
# Un atributo de clase llamado aumento_general con un valor inicial (ej. 1.05)
# Un método de clase que permita modificar el porcentaje de aumento general para todos los empleados
# Un método estático que reciba un salario y verifique si supera un cierto umbral (ej. sueldo mínimo)
# 🔹 Qué se debe probar:
# Crear varios empleados con salarios distintos
# Modificar el aumento general desde la clase
# Usar el método estático para evaluar si un salario es alto o bajo
# Ver cómo el método de clase afecta a todos los objetos

class Empleado:
    aumento_general = 1.05
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def get_datos(self):
        print(f"Trabajador: {self.nombre}, sueldo: {self.salario} ")

    def aplicar_aumento(self):
        self.salario = self.salario * Empleado.aumento_general
    
    @classmethod
    def cambiar_aumento(cls, nuevo_factor):
        cls.aumento_general = nuevo_factor

    @staticmethod
    def salario_alto(salario):
        return salario >= 1000
    
#instancia
emplea_1 = Empleado("Ana", 900)

#Método de instancia
emplea_1.get_datos()

#Método de clase
Empleado.cambiar_aumento(5)

print(f" Salario alto ?: {Empleado.salario_alto(emplea_1.salario)}")


emplea_1.aplicar_aumento()
emplea_1.get_datos()

print(f" Salario alto ?: {Empleado.salario_alto(emplea_1.salario)}")
