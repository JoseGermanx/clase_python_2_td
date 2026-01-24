# Paso a paso: ⚙️
# Definí la clase y sus métodos

# Creá una lista de 3 o más mascotas

# Recorrelas con un for y:

# Mostrá su presentación

# Indicá si es joven o no

# Bonus: Filtrá solo las mascotas jóvenes en una nueva lista

class Mascota:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo} y tengo {self.edad} años.")


    def es_joven(self):
        return self.edad < 5
    

mascotas = [
    Mascota("Luna", 2, "perra"),
    Mascota("Rocky", 7, "perro"),
    Mascota("Milo", 4, "gato"),
    Mascota("Mia", 6, "gata")
]

mascotas_jovenes= []


for mascota in mascotas:
    mascota.presentarse()
    if mascota.es_joven():
        print("Es joven!!")
        mascotas_jovenes.append(mascota) #bonus track
    else:
        print("No es joven.")


#bonus track
print("Estas son las mascotas jóvenes")
for mascota in mascotas_jovenes:
    print(mascota.nombre)