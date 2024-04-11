class Pajaro:

    # Atributo de clase
    alas = True

    # Init = constructor, self = instancia del objeto que será creado, self es una convención
    # Atributo de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')


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