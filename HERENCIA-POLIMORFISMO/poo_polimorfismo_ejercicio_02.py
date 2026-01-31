# Contexto: 🙌
# Una plataforma de e-commerce necesita clasificar y operar sobre distintos tipos de productos, aplicando descuentos y condiciones según su categoría.

# Consigna: ✍️
# Definí las siguientes clases:
# 🔹 Producto (clase base)
# Atributos: nombre, precio
# Método: calcular_precio_final() (retorna el mismo precio)
# 🔹 Subclases:
# ProductoFisico: aplica costo de envío
# ProductoDigital: aplica descuento automático
# Suscripcion: agrega porcentaje mensual

# Paso a paso: ⚙️
# Crear una lista con productos de diferentes clases

# Calcular e imprimir el precio final de todos con calcular_precio_final()

# Usar isinstance() para clasificar:

# Si es ProductoDigital, aplicar descuento adicional

# Si es Suscripcion, simular facturación mensual

# Mostrar resultados organizados por tipo de producto

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_final(self):
        return self.precio


class ProductoFisico(Producto):
    def __init__(self, nombre, precio, envio):
        super().__init__(nombre, precio)
        self.envio = envio
    
    def calcular_precio_final(self):
        return self.precio + self.envio
    
class ProductoDigital(Producto):
    def calcular_precio_final(self):
        return self.precio * 0.9 #Se aplica 10% de descuento
    
class Suscripcion(Producto):
    def __init__(self, nombre, precio, porcentaje_mensual):
        super().__init__(nombre, precio)
        self.porcentaje_mensual = porcentaje_mensual
    
    def calcular_precio_final(self):
        return self.precio * (1 + self.porcentaje_mensual)

lista_productos = [
    ProductoFisico("NoteBook", 100000, 5000),
    ProductoDigital("Curso de Python", 10000),
    Suscripcion("Youtube", 4500, 0.05)
]

for producto in lista_productos:
    precio_final = producto.calcular_precio_final()
    if isinstance(producto, ProductoDigital):
        decuento_adicional = 0.05
        precio_final -= precio_final * decuento_adicional
        print(f"El precio de {producto.nombre} es ${precio_final} con descuento adicional")

    elif isinstance(producto, Suscripcion):
        print(f"Suscripción mensual del servicio {producto.nombre} es {precio_final}")

    elif isinstance(producto, ProductoFisico):
        print(f"El precio de {producto.nombre} es ${precio_final}, con envio incluido.")