class Persona:
    def __init__(self, nombre, año_nacimiento):
        self.nombre = nombre
        self.año_nacimiento = año_nacimiento

    def calcular_edad(self, año_actual):
        return año_actual - self.año_nacimiento
    
if __name__ == "__main__":
    print("Ingrese su nombre")
    nombre = input()
    print("Ingrese su año de nacimiento")
    año_nacimiento = int(input())
    persona = Persona(nombre, año_nacimiento)
    año_actual = 2026
    edad = persona.calcular_edad(año_actual)
    print(f"{persona.nombre} tiene {edad} años")