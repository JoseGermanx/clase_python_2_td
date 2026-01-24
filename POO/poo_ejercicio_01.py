# Consigna: ✍️
# Creá una clase Celular que tenga los siguientes elementos:
# Atributos: marca, modelo, almacenamiento
# Método encender() que imprima "Encendiendo {marca} {modelo}..."
# Método mostrar_info() que muestre todos los atributos

class Celular:
    def __init__(self, marca, modelo, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento

    def encender(self):
        print(f"Encendiendo {self.marca} {self.modelo}...")

    def mostrar_info(self):
        print("Datos del teléfono: ")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento} gb")

celular_1 = Celular("Iphone", "17 Pro", 128)
celular_2 = Celular("Xiaomi", "XpUltra", 64)

celular_1.encender()
celular_1.mostrar_info()

celular_2.encender()
celular_2.mostrar_info()