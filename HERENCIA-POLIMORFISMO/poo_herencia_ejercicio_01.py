# Vas a diseñar un sistema para representar diferentes tipos de medios de transporte.


# Consigna: ✍️
# Implementá las siguientes clases en Python usando herencia:
# Vehiculo (clase base): marca, modelo, moverse()
# Auto (subclase): sobrescribe moverse() con "Conduciendo por la carretera"
# Bicicleta (subclase): sobrescribe moverse() con "Pedaleando"
# Motocicleta (subclase): agrega atributo cilindrada

# Paso a paso: ⚙️
# Aplicar herencia simple

# Usar sobrescritura de métodos

# Probar comportamiento polimórfico con un bucle que recorra una lista de vehículos y llame a moverse()

class Vehiculo:
    def __init__(self, marca, modelo, anio, ruedas, color, numero_serie, asientos):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.ruedas = ruedas
        self.color = color
        self.numero_serie = numero_serie
        self.asientos = asientos


    def moverse(self):
        print("Este método lo implementará cada subclase.")

#TODO: Implementar para herencia multiple de atributos
class Motor:
    def __init__(self, kilometros, motor):
        self.kilometros = kilometros
        self.motor = motor
        
class Auto(Vehiculo):
    def moverse(self):
        print(f"El auto {self.marca} va andando por la carretera.")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, ruedas, color, numero_serie, asientos, cilindrada):
        super().__init__(marca, modelo, anio, ruedas, color, numero_serie, asientos)
        self.cilindrada = cilindrada

    def moverse(self):
        print(f"La motocicleta {self.marca}-{self.cilindrada}cc, va a toda velocidad por la pista.")

class Camion(Vehiculo):
    pass


# A pedal
class Bicicleta(Vehiculo):
    def moverse(self):
        print(f"El ciclista va pedaleando en su bici {self.marca}.")


vehiculos = [
    Auto("Toyota", "Corolla", 2000, 4, "negra", "werwerwer", 5),
    Bicicleta("Trek", "Marlin 4", 2000, 2, "negra", "werwerwer", 2),
    Motocicleta("Yamaha", "MT-07", 2000, 2, "Negra", "123423rff", 2, 550)
]

for vehiculo in vehiculos:
    vehiculo.moverse()