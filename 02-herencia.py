class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')


class Pajaro(Animal):
    pass

# Imprimir clase de la que hereda
print(Pajaro.__base__)

# Imprimir subclases
print(Animal.__subclasses__())

piolin = Pajaro(2, 'amarillo')
piolin.nacer()
print(piolin.color)