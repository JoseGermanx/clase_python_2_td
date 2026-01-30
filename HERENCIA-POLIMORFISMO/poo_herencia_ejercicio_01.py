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


# Base de datos en memoria
class BaseDatos:
    def __init__(self):
        self.vehiculos = []
    
    def agregar(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"✓ {vehiculo.__class__.__name__} agregado correctamente.\n")
    
    def listar(self):
        if not self.vehiculos:
            print("\n⚠️  No hay vehículos en la base de datos.\n")
            return
        
        print("\n" + "="*60)
        print(f"{'VEHÍCULOS ALMACENADOS'}".center(60))
        print("="*60)
        
        for i, vehiculo in enumerate(self.vehiculos, 1):
            print(f"\n{i}. {vehiculo.__class__.__name__}")
            print(f"   Marca: {vehiculo.marca}")
            print(f"   Modelo: {vehiculo.modelo}")
            print(f"   Año: {vehiculo.anio}")
            print(f"   Color: {vehiculo.color}")
            if hasattr(vehiculo, 'cilindrada'):
                print(f"   Cilindrada: {vehiculo.cilindrada}cc")
        
        print("\n" + "="*60 + "\n")
    
    def demostrar(self):
        if not self.vehiculos:
            print("\n⚠️  No hay vehículos para demostrar.\n")
            return
        
        print("\n" + "="*60)
        print("DEMOSTRACIONES DE MOVIMIENTO".center(60))
        print("="*60 + "\n")
        
        for vehiculo in self.vehiculos:
            vehiculo.moverse()
        
        print("\n" + "="*60 + "\n")


def menu_interactivo():
    bd = BaseDatos()
    
    while True:
        print("\n" + "="*60)
        print("MENÚ PRINCIPAL - GESTOR DE VEHÍCULOS".center(60))
        print("="*60)
        print("\n1. Crear Auto")
        print("2. Crear Bicicleta")
        print("3. Crear Motocicleta")
        print("4. Crear Camión")
        print("5. Crear SUV")
        print("6. Listar vehículos")
        print("7. Demostrar movimiento de vehículos")
        print("8. Salir")
        print("\n" + "="*60)
        
        opcion = input("Selecciona una opción (1-8): ").strip()
        
        if opcion == "1":
            print("\n--- CREAR AUTO ---")
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            anio = int(input("Año: ").strip())
            color = input("Color: ").strip()
            numero_serie = input("Número de serie: ").strip()
            kilometros = int(input("Kilómetros: ").strip())
            motor = input("Motor (ej: 4L): ").strip()
            
            auto = Auto(marca, modelo, anio, 4, color, numero_serie, 5, kilometros, motor)
            bd.agregar(auto)
        
        elif opcion == "2":
            print("\n--- CREAR BICICLETA ---")
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            anio = int(input("Año: ").strip())
            color = input("Color: ").strip()
            numero_serie = input("Número de serie: ").strip()
            
            bicicleta = Bicicleta(marca, modelo, anio, 2, color, numero_serie, 2)
            bd.agregar(bicicleta)
        
        elif opcion == "3":
            print("\n--- CREAR MOTOCICLETA ---")
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            anio = int(input("Año: ").strip())
            color = input("Color: ").strip()
            numero_serie = input("Número de serie: ").strip()
            kilometros = int(input("Kilómetros: ").strip())
            motor = input("Motor (ej: 1L): ").strip()
            cilindrada = int(input("Cilindrada (cc): ").strip())
            
            motocicleta = Motocicleta(marca, modelo, anio, 2, color, numero_serie, 2, kilometros, motor, cilindrada)
            bd.agregar(motocicleta)
        
        elif opcion == "4":
            print("\n--- CREAR CAMIÓN ---")
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            anio = int(input("Año: ").strip())
            color = input("Color: ").strip()
            numero_serie = input("Número de serie: ").strip()
            kilometros = int(input("Kilómetros: ").strip())
            motor = input("Motor (ej: 12.8L): ").strip()
            
            camion = Camion(marca, modelo, anio, 3, color, numero_serie, 3, kilometros, motor)
            bd.agregar(camion)
        
        elif opcion == "5":
            print("\n--- CREAR SUV ---")
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            anio = int(input("Año: ").strip())
            color = input("Color: ").strip()
            numero_serie = input("Número de serie: ").strip()
            kilometros = int(input("Kilómetros: ").strip())
            motor = input("Motor (ej: 5L): ").strip()
            
            suv = SUV(marca, modelo, anio, 4, color, numero_serie, 7, kilometros, motor)
            bd.agregar(suv)
        
        elif opcion == "6":
            bd.listar()
        
        elif opcion == "7":
            bd.demostrar()
        
        elif opcion == "8":
            print("\n¡Hasta luego! 👋\n")
            break
        
        else:
            print("\n❌ Opción inválida. Intenta de nuevo.\n")


# Ejecutar menú interactivo
if __name__ == "__main__":
    menu_interactivo()