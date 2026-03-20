class OperacionesMatematicas:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: División por cero no permitida"
        
if __name__ == "__main__":
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    operaciones = OperacionesMatematicas(a, b)
    print("Suma:", operaciones.sumar())
    print("Resta:", operaciones.restar())
    print("Multiplicación:", operaciones.multiplicar())
    print("División:", operaciones.dividir())