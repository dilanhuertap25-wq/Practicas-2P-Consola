class Persona:
    def __init__(self, nombre, edad, año_nacimiento):
        self.nombre = nombre
        self.edad = edad
        self.año_nacimiento = año_nacimiento

    def calcular_edad(self, año_actual):
        self.edad = año_actual - self.año_nacimiento
        return self.edad
        