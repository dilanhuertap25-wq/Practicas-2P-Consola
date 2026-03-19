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
    op = OperacionesMatematicas(10, 5)
    print("Suma:", op.sumar())
    print("Resta:", op.restar())
    print("Multiplicación:", op.multiplicar())
    print("División:", op.dividir())