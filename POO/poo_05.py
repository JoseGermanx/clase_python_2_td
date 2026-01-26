# ¿En qué consistirá la Demo?
# Vamos a crear una clase que representa una cuenta de correo electrónico, con atributos públicos, protegidos y privados para simular distintos niveles de acceso.

# Definir la clase CuentaCorreo
# Crear una instancia
# Acceder a los atributos
# Reflexión final:
# ¿Qué pasaría si esta clase se usara en un sistema real sin protección?

# 📌 Objetivo: reforzar la utilidad del encapsulamiento en contextos sensibles, mostrando cómo Python permite proteger atributos para evitar mal uso o manipulación directa.

#   usuario-> correo @  dominio-> correo.com  password->123456

class CuentaCorreo:
    def __init__(self, usuario, dominio, password):
        self.usuario = usuario # público
        self._dominio = dominio # protegido
        self.__password = password
    
    def crear_cuenta(self):
        print(f"Usuario: {self.usuario}@{self._dominio} ")
    

cuenta_1 = CuentaCorreo("correo", "gmail.com", "123456")

print(cuenta_1._dominio) # Accesible pero no recomendado

# print(cuenta_1.__password) # Error: no es accesible --> Privado

cuenta_1.crear_cuenta()

print(cuenta_1._CuentaCorreo__password)

