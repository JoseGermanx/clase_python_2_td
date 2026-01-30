

class Calculadora:
    def sumar(self, *args):
        if len(args) == 2:
            print(args[0] + args[1])
        elif len(args) == 3:
            print(args[0] + args[1] + args[2])
        else:
            print("Cantidad de parámetros no soportada.")
        

calc = Calculadora()
    
calc.sumar(1, 4, 7)
