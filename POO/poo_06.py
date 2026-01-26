# ¿En qué consistirá la Demo?
# Vas a diseñar una clase que represente un producto de tienda, controlando el acceso y modificación del precio a través de métodos específicos.

# 🔹 Qué debe tener la clase:
# Un atributo público para el nombre del producto
# Un atributo privado para el precio (__precio)
# Un método para ver el precio (getter)
# Un método para modificar el precio (setter), que solo permita valores positivos
# En el constructor (__init__), usar el setter para validar el precio desde el inicio
# 🔹 Qué se debe probar con objetos:
# Crear un producto con precio válido
# Mostrar el precio usando el getter
# Intentar cambiar el precio a un valor negativo (debe mostrar un error)
# Modificar correctamente el precio y verificar el nuevo valor

class Producto:
    def __init__(self,nombre, precio):
        self.nombre = nombre
        self.set_precio(precio)

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El valor del precio debe ser positivo.")

    
    
producto_1 = Producto("Zapatilla", 500)

print(f"Precio: {producto_1.get_precio()}")

producto_1.set_precio(-100)

print(f"Precio: {producto_1.get_precio()}")