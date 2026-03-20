class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = self.calcular_area()
        self.perimetro: int = self.calcular_perimetro()

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        lado = self.base
        return 3 * lado

if __name__ == "__main__":
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    
    triangulo = Triangulo(base, altura)
    area = triangulo.area
    perimetro = triangulo.perimetro 
    print(f"El area del triangulo es: {area}")
    print(f"El perimetro del triangulo es: {perimetro}")