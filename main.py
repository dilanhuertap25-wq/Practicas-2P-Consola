if __name__ == "__main__":
    
    from holaMundo import Mensaje
    from operacionesMatematicas import OperacionesMatematicas
    from persona import Persona  
    from cuadrado import Cuadrado
    from rectangulo import Rectangulo
    from triangulo import Triangulo

    print("este es el programa principal")
    print("elige la opcion que deseas hacer")
    print("1. hola mundo programacion en clases")
    print("2. Realizar operaciones matematicas")
    print("3. Persona")
    print("4. Figuras geometricas")
    opcion = int(input("Ingrese el numero de la opcion que desea realizar: "))

    if opcion == 1:
        mensaje = Mensaje("Hola Mundo programacion en clases")
        mensaje.imprimir()
    elif opcion == 2:
        print("Ingrese los numeros para realizar las operaciones matematicas")
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        operaciones = OperacionesMatematicas(a, b)
        print("la suma es: ", operaciones.suma())
        print("la resta es: ", operaciones.resta())
        print("la multiplicacion es: ", operaciones.multiplicacion())
        print("la division es: ", operaciones.division())
    elif opcion == 3:
        print("Ingrese su nombre")
        nombre = input()
        print("Ingrese su año de nacimiento")
        año_nacimiento = int(input())
        edad = 2026 - año_nacimiento
        persona = Persona(nombre, edad, año_nacimiento)
        print(f"{persona.nombre} tiene {persona.calcular_edad(2026)} años.")

    elif opcion == 4:   
        print("elige la figura geometrica que deseas calcular")
        print("1. Cuadrado")
        print("2. Rectangulo")
        print("3. Triangulo")
        figura = int(input("Ingrese el numero de la figura geometrica que desea calcular: "))
        if figura == 1:
           lado = float(input("Ingrese el lado del cuadrado: "))
           cuadrado = Cuadrado(lado)
           area = cuadrado.calcular_area()
           perimetro = cuadrado.calcular_perimetro()
           print(f"El area del cuadrado es: {area}")
           print(f"El perimetro del cuadrado es: {perimetro}")
        elif figura == 2:
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            rectangulo = Rectangulo(base, altura)
            area = rectangulo.calcular_area()
            perimetro = rectangulo.calcular_perimetro()
            print(f"El area del rectangulo es: {area}")
            print(f"El perimetro del rectangulo es: {perimetro}")
        elif figura == 3:
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            triangulo = Triangulo(base, altura)
            area = triangulo.calcular_area()
            perimetro = triangulo.calcular_perimetro()
            print(f"El area del triangulo es: {area}")
            print(f"El perimetro del triangulo es: {perimetro}")