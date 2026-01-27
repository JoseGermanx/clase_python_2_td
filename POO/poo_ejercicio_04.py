# Contexto: 🙌
# Queremos representar productos de un sistema de stock, controlando el precio mediante métodos y gestionando un descuento común para todos. Además, el sistema debe validar precios antes de aceptarlos.

# Consigna: ✍️
# Creá una clase Producto con precio encapsulado, un descuento común para todas las instancias, y un validador independiente que confirme si un precio ingresado es correcto.

# Paso a paso: ⚙️
# Atributos: nombre (público), __precio (privado), y descuento (atributo de clase)
# Método aplicar_descuento() para obtener el precio final
# @classmethod set_descuento() para actualizar el valor general
# @staticmethod validar_precio(precio) para verificar si es mayor que cero
# Creá 2 productos distintos y usá todos los métodos creados

class Producto:
    descuento = 0.10 # 10% descuento

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.set_precio(precio)

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El valor del precio debe ser positivo.")

    def aplicar_descuento(self):
        return self.__precio * (1 - Producto.descuento)

    @classmethod
    def set_descuento(cls, nuevo_descuento):
        cls.descuento = nuevo_descuento

    @classmethod
    def get_descuento(cls):
        return cls.descuento

    @staticmethod
    def validar_precio(precio):
        return precio > 0
    

obj_1 = Producto("Zapatilla", 100)

print(f"Producto es mayor a cero?:  {Producto.validar_precio(obj_1.get_precio())}")

print(f"Precio: {obj_1.get_precio()}")

print(f"Descuento aplicado: {obj_1.aplicar_descuento()}")

Producto.set_descuento(0.20)

print(f"Descuento aplicado: {obj_1.aplicar_descuento()}")

print(f"Precio: {obj_1.get_precio()}")