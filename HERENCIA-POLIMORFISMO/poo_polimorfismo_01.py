# ¿En qué consistirá la Demo?
# Vas a crear una clase base Figura y subclases como Rectangulo y Circulo, cada una con su propia implementación del método dibujar().

# 🔹 Qué debe tener cada clase:

# Clase base Figura:
# Método dibujar() (vacío o con pass)
# Subclases:
# Rectangulo: sobrescribe dibujar() con "Dibujo un rectángulo"
# Circulo: sobrescribe dibujar() con "Dibujo un círculo"
# Triangulo: sobrescribe dibujar() con "Dibujo un triángulo"

# 🔹 Qué se debe probar:

# Crear una lista con objetos de distintas figuras

# Iterar con un for y llamar a dibujar()

# Verificar que cada objeto ejecuta su propia versión del método



class Figura:
    def dibujar(self):
        pass

# Polimorfismo por sobreescritura
class Rectangulo(Figura):
    def dibujar(self):
        print("Dibujo un rectángulo.")

# Polimorfismo por sobreescritura
class Circulo(Figura):
    def dibujar(self):
        print("Dibujo un círculo.")

# Polimorfismo por sobreescritura
class Triangulo(Figura):
    def dibujar(self):
        print("Dibujo un triangulo.")


#lista

rectangulo_1 = Rectangulo()
circulo_1 = Circulo()
triangulo_1 = Triangulo()

lista_de_figuras = [rectangulo_1, circulo_1, triangulo_1]

for figura in lista_de_figuras:
    figura.dibujar()