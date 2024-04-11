class Pajaro:

    # Atributo de clase
    alas = True

    # Init = constructor, self = instancia del objeto que será creado, self es una convención
    # Atributo de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro('negro', 'Tucan')
otro_pajaro = Pajaro('amarillo', 'Turpial')

print(mi_pajaro)

# Conocer el tipo de la variable
print(type(mi_pajaro))

print(mi_pajaro.color)
print(mi_pajaro.especie)
print(Pajaro.alas)

print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')