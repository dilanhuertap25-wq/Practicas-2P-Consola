class Mensaje:
  
    def __init__(self, texto):
        self.texto = texto
    
    def imprimir(self):
        print(self.texto)

if __name__ == "__main__":
    mensaje = Mensaje("Hola Mundo programacion en clases")
    mensaje.imprimir() 
