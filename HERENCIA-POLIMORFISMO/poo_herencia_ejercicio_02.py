# Queremos modelar un animal con habilidades combinadas.


# Consigna: ✍️
# Definí las siguientes clases:
# Volador: método moverse() imprime "Estoy volando"
# Nadador: método moverse() imprime "Estoy nadando"
# Pato: hereda de ambas clases, no sobrescribe moverse()

# Paso a paso: ⚙️
# Creá un objeto Pato y llamá a moverse()
# Usá Pato.__mro__ o help(Pato) para mostrar el orden de resolución
# Cambiá el orden de herencia y volvé a probar
# Agregá un método propio en Pato que combine ambos comportamientos


class Volador:
    def moverse(self):
        print("Estoy volando")

class Nadador:
    def moverse(self):
        print("Estoy nadando")


class Pato(Volador, Nadador):
    def moverse_como_pato(self):
        print("Puedo volar y puedo nadar")

pato_1 = Pato()
pato_1.moverse()
print(Pato.__mro__)
pato_1.moverse_como_pato()