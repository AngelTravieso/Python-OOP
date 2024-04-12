class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido} {self.numero_cuenta} {self.balance}'
    
    def depositar(self, cantidad_deposito):
        if(cantidad_deposito > 0):
            self.balance = cantidad_deposito
        else:
            print('Deposito no permitido')


    def retirar(self, cantidad_retiro):
        if(cantidad_retiro > 0 and self.balance > cantidad_retiro):
            self.balance =- cantidad_retiro
        else:
            print('Retiro no permitido')

opcion = 0

def imprimirMenu():
    while True:
        print('BANCO ZELDA')
        print('---------------------------')
        print('1. DEPOSITO')
        print('2. RETIRO')
        print('3. SALIR')

        
        opcion = input('¿Que operacion desea hacer? (elegir numero de opcion):')

        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        else:
            pass