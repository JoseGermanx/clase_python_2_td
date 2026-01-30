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
class VehiculoMotor(Vehiculo):
    def __init__(self, marca, modelo, anio, ruedas, color, numero_serie, asientos, kilometros, motor):
        super().__init__(marca, modelo, anio, ruedas, color, numero_serie, asientos)
        self.kilometros = kilometros
        self.motor = motor
        
class Auto(VehiculoMotor):
    def moverse(self):
        print(f"El auto {self.marca} va andando por la carretera.")

class Camion(VehiculoMotor):
    def moverse(self):
        print(f"El camión {self.marca} va full con la carga.")

class SUV(VehiculoMotor):
    def moverse(self):
        print(f"La SUV {self.marca} va vía la playa con toda la familia.")


class Motocicleta(VehiculoMotor):
    def __init__(self, marca, modelo, anio, ruedas, color, numero_serie, asientos, kilometros, motor, cilindrada):
        super().__init__(marca, modelo, anio, ruedas, color, numero_serie, asientos, kilometros, motor)
        self.cilindrada = cilindrada

    def moverse(self):
        print(f"La motocicleta {self.marca}-{self.cilindrada}cc, va a toda velocidad por la pista.")

# A pedal
class Bicicleta(Vehiculo):
    def moverse(self):
        print(f"El ciclista va pedaleando en su bici {self.marca}.")


vehiculos = [
    Auto("Toyota", "Corolla", 2000, 4, "Rojo", "sdgoñihdfg789723453", 5, 20000, "4L"),
    Bicicleta("Trek", "Marlin 4", 2000, 2, "Azul", "3245983rghjedg", 2),
    Motocicleta("Yamaha", "MT-07", 2000, 2, "Negro", "234'902734'892jk3hjksdfg", 2, 5000, "1L", 500),
    Camion("Mercedes-Benz", "Actros 1845", 2021, 3, "Blanco", "2342342342344", 5, 100000, "12.8 L"),
]

for vehiculo in vehiculos:
    vehiculo.moverse()