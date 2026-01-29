# ¿En qué consistirá la Demo?
# Vas a crear una clase Pato que herede métodos de dos clases distintas, y observarás cómo Python decide cuál método usar si hay conflicto.

# 🔹 Clase Volador:
# Método: moverse() imprime "El pato vuela"

# 🔹 Clase Nadador:
# Método: moverse() imprime "El pato nada"

# 🔹 Clase Pato:
# Hereda de ambas: class Pato(Volador, Nadador)
# No implementa moverse()

# 🔹 Qué se debe probar:
# Crear un objeto Pato
# Llamar a moverse()
# Usar Pato.__mro__ o help(Pato) para inspeccionar el orden de búsqueda
# Cambiar el orden de herencia (class Pato(Nadador, Volador)) y repetir


class Volador:
    def moverse(self):
        print("El pato vuela")

class Nadador:
    def moverse(self):
        print("El pato nada")

class Pato(Nadador, Volador):
    pass

pato_1 = Pato()

pato_1.moverse()

print(Pato.__mro__)