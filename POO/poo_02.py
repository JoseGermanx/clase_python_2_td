
# Reutilizar la clase Persona con atributos nombre y edad
# Crear dos objetos distintos: persona1 y persona2
# Ver cómo cada objeto tiene su estado individual
# Modificar el atributo edad de uno de los objetos
# Verificar que los cambios en un objeto no afectan al otro
# Agregar un nuevo atributo "profesión" directamente a uno de los objetos
# Mostrar que no todos los objetos tienen por qué tener los mismos atributos si se agregan dinámicamente


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
persona_1 = Persona("Lucia", 30)
persona_2 = Persona("Luis", 25)

# Verificar que cada estado es independiente
persona_1.presentarse()
persona_2.presentarse()

# Agregar un nuevo atributo "profesión" directamente a uno de los objetos

persona_1.profesion = "Doctor"

# Mostrar que no todos los objetos tienen por qué tener los mismos atributos si se agregan dinámicamente

print("persona 1: ", persona_1.__dict__)
print("persona 2: ", persona_2.__dict__)