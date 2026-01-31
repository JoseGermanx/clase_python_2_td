# Contexto: 🙌
# Una empresa quiere un sistema que gestione diferentes tipos de personal, permitiendo operaciones polimórficas y validación dinámica de acciones según el rol.

# Consigna: ✍️
# Diseñá e implementá las siguientes clases:
# 🔹 Empleado (clase base)
# Atributos: nombre, dni
# Método: trabajar() imprime "Empleado general trabajando"
# 🔹 Subclases:
# Desarrollador: sobrescribe trabajar() con "Codificando...", método propio escribir_codigo()
# Diseñador: sobrescribe trabajar() con "Diseñando interfaces...", método propio crear_mockup()
# Gerente: sobrescribe trabajar() con "Planificando estrategias...", método propio supervisar_equipo()

# Paso a paso: ⚙️
# Crear una lista con objetos de distintas subclases

# Iterar e invocar trabajar() para demostrar polimorfismo

# Usar isinstance() para aplicar funciones específicas según el tipo:

# Si es Gerente → mostrar que supervisa
# Si es Desarrollador → mostrar que escribe código


class Empleado:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
    
    def trabajar(self):
        print("Empleado general trabajando...")


class Deesarrollador(Empleado):
    def trabajar(self):
        print("Codificando....")
    
    def escribir_codigo(self):
        print(f"{self.nombre} esta creado una aplicación para la gestión de clientes con Python.")

class Disenador(Empleado):
    def trabajar(self):
        print("Diseñando interfaces...")

    def crear_mockup(self):
        print(f"{self.nombre} trabaja en el diseño la apariencia de la aplicación de gestión de clientes")

class Gerente(Empleado):
    def trabajar(self):
        print(" Planificando estrategias....")
    
    def supervisar_equipo(self):
        print(f" El líder del equipo {self.nombre}, esta supervisando las tareas de los desarrolladores y diseñadores para cumplir con el tiempo de entrega")

lista_empleados = [
    Deesarrollador("Ana", "12234234"),
    Disenador("Juan", "12342345"),
    Gerente("Luis", "12342344ef")
]

for empleado in lista_empleados:
    empleado.trabajar()
    if isinstance(empleado, Deesarrollador):
        empleado.escribir_codigo()
    elif isinstance(empleado, Disenador):
        empleado.crear_mockup()
    elif isinstance(empleado, Gerente):
        empleado.supervisar_equipo()
