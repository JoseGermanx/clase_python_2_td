# class Animal: pass

# class Perro(Animal): pass

# fido = Perro()

# print(isinstance(fido, Perro))
# print(isinstance(fido, Animal))
# print(type(fido) == Perro)
# print(type(fido) == Animal)

# ¿En qué consistirá la Demo?
# Vas a crear una jerarquía de clases (Usuario, Administrador, Cliente) y usar isinstance() para aplicar acciones según el tipo de objeto

# 🔹 Clases involucradas:

# Clase base Usuario:

# Método saludar() común a todos

# Subclases:

# Administrador: método acceder_panel()

# Cliente: método realizar_compra()

# 🔹 Qué se debe probar:

# Crear una lista de objetos mezclados (Cliente, Administrador, Usuario)
# Iterar sobre la lista
# Usar isinstance() para ejecutar acciones según el tipo:
# Si es Administrador → llamar acceder_panel()
# Si es Cliente → llamar realizar_compra()
# Si es Usuario → llamar solo saludar()

class Usuario:
    def __init__(self, nombre, correo):
       self.nombre = nombre
       self.correo = correo
    def saludar(self):
        print(f"El usuario {self.nombre} ingresó al sistema con el correo {self.correo}")

class Administrador(Usuario):
    def __init__(self, nombre, correo, id):
        super().__init__(nombre, correo)
        self.id = id
    def acceder_panel(self):
        print(f"El usuario {self.id} ingresó al panel de administración, con su correo {self.correo}")

class Cliente(Usuario):
    def __init__(self, nombre, correo, cupon):
        super().__init__(nombre, correo)
        self.cupon = cupon
    def realizar_compra(self):
        print(f"El cliente {self.nombre}. Ha reealizando una compra, utilizando el cupon {self.cupon}.")


cliente_1 = Cliente("Ana Luisa", "ana@gmail.com", "DESCUENTOPREMIUM")

administrador_1 = Administrador("Alberto", "admin@correo.com", "admin01")

usuario_1 = Usuario("Juan", "juan@gmail.com")

lista_usuarios = [cliente_1, administrador_1, usuario_1]


for usuario in lista_usuarios:
    if isinstance(usuario, Administrador):
        usuario.saludar()
        usuario.acceder_panel()
    elif isinstance(usuario, Cliente):
        usuario.saludar()
        usuario.realizar_compra()
    else:
        usuario.saludar()