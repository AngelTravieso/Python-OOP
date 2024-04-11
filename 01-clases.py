class Pajaro:

    # Atributo de clase
    alas = True

    # Init = constructor, self = instancia del objeto que será creado, self es una convención
    # Atributo de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Métodos de instancia
    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es color {self.color}')

    # Método de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} de huevos')
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print('El pajaro mira')


mi_pajaro = Pajaro('negro', 'Tucan')
# otro_pajaro = Pajaro('amarillo', 'Turpial')

print(mi_pajaro)

# Conocer el tipo de la variable
print(type(mi_pajaro))

print(mi_pajaro.color)
print(mi_pajaro.especie)
print(Pajaro.alas)

print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')

print(mi_pajaro.piar())
print(mi_pajaro.volar(50))

# Modificar atributo de clase
mi_pajaro.alas = False
print(mi_pajaro.alas)

Pajaro.poner_huevos(3)
# Pajar.piar() # Da error porque piar() no es un método de clase

Pajaro.mirar()