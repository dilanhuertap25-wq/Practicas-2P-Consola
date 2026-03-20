class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
        self.area = self.calcular_area()
        self.perimetro: int = self.calcular_perimetro()

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado
    
if __name__ == "__main__":
    lado = float(input("Ingrese el lado del cuadrado: "))
    cuadrado = Cuadrado(lado)
    area = cuadrado.area
    perimetro = cuadrado.perimetro 
    print(f"El area del cuadrado es: {area}")
    print(f"El perimetro del cuadrado es: {perimetro}")