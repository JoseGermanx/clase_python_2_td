# Contexto: 🙌
# Una librería necesita un sistema simple para controlar su inventario. Cada libro posee un título, un autor, un precio y una cantidad de stock. Se desea evitar precios negativos y gestionar correctamente las ventas.

# Consigna: ✍️
# Modelá una clase Libro que contenga atributos públicos y privados. Utilizá getters y setters para proteger el precio, y diseñá un método para realizar ventas que actualicen el stock.
# Paso a paso: ⚙️
# Definí los atributos: titulo, autor, stock (públicos) y __precio (privado)
# Implementá get_precio() y set_precio() validando que sea un valor positivo
# Agregá un método vender(unidades) que descuente del stock si hay suficiente
# Creá el método mostrar_info() para imprimir todos los datos del libro
# Probá con varios objetos

class Libro:
    def __init__(self, titulo, autor, stock, precio):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock
        self.set_precio(precio)
    
    #setter
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El valor del precio debe ser positivo.")

    #getter
    def get_precio(self):
        return self.__precio
    
    def vender_libro(self, unidades):
        if not isinstance(unidades, int):
            print("Error de tipo: Debe ingresar un número válido.")
        elif unidades <= 0:
            print("Error: unidades deben ser mayor a 0.")
        elif unidades > self.stock:
            print(f"Error: Stock insuficiente. Sólo tenemos disponibles {self.stock} unidades de {self.titulo}")
        else:
            self.stock -= unidades
            print(f"Venta realizada: {unidades} unidades del libro {self.titulo}")

    def mostrar_info(self):
        print("---Datos del libro---")
        print(f"Título: {self.titulo}.")
        print(f"Autor: {self.autor}.")
        print(f"Stock: {self.stock} ")
        print(f"Precio: {self.get_precio()} ")

libro_1 = Libro("1984", "George Orwell", 10, 18000)
libro_2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 3, 25000)

print(libro_1.get_precio())

libro_1.vender_libro(5)

libro_1.mostrar_info()