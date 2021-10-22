import random
class Producto:
    def __init__(self, cod, peso, tipo, lugar, imp):
        self.codigo = cod
        self.peso = peso
        self.tipo = tipo
        self.lugar = lugar
        self.importe = imp


def crear_aleatorio():

    cod = random.randint(1000, 9999)
    peso = round(random.uniform(1, 100), 2)
    tipo = random.randint(0, 19)
    lugar = random.randint(0, 20)
    imp = round(random.uniform(10, 500), 2)

    return Producto(cod, peso, tipo, lugar, imp)

