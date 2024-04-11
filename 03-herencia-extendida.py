class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        # self.edad = edad
        # self.color = color
        super().__init__(edad, color) # Hereda el constructor de la clase padre
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro vuelta {metros} metros')




piolin = Pajaro(3, 'amarillo', 60)
mi_animal = Animal(5, 'negro')

piolin.volar(100)
piolin.nacer()
piolin.hablar()


################################
class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('ja ja')

    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar() # imprime 'Hola' porque primero hereda de Padre
mi_nieto.reir()

print(Nieto.__mro__) ## Imprimir orden de resolución de clase