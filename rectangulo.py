class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = self.calcular_area()
        self.perimetro: int = self.calcular_perimetro()

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
if __name__ == "__main__":
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))
    rectangulo = Rectangulo(base, altura)
    area = rectangulo.area
    perimetro = rectangulo.perimetro 
    print(f"El area del rectangulo es: {area}")
    print(f"El perimetro del rectangulo es: {perimetro}")