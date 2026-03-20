if __name__ == "__main__":
    
    from holaMundo import Mensaje
    from operacionesMatematicas import OperacionesMatematicas
    from persona import Persona
    from triangulo import Triangulo
    from rectangulo import Rectangulo
    from cuadrado import Cuadrado
    
    print("este es el programa principal")
    print("elige la opcion que deseas hacer")
    print("1. Mensaje")
    print("2. Realizar operaciones matematicas")
    print("3. Persona")
    print("4. Figuras geometricas")
    opcion = int(input("Ingrese el numero de la opcion que desea realizar: "))

    if opcion == 1:
        mensaje = Mensaje("Hola mundo programacion en clases")
        mensaje.imprimir()

    elif opcion == 2:
        print("Ingrese los numeros para realizar las operaciones matematicas")
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        operaciones = OperacionesMatematicas(a, b)
        print("la suma es: ", operaciones.sumar())
        print("la resta es: ", operaciones.restar())
        print("la multiplicacion es: ", operaciones.multiplicar())
        print("la division es: ", operaciones.dividir())

    elif opcion == 3:
        año_actual = 2026
        print("Ingrese su nombre")
        nombre = input()
        print("Ingrese su año de nacimiento")
        año_nacimiento = int(input())
        persona = Persona(nombre, año_nacimiento)
        edad = persona.calcular_edad(año_actual)
        print(f"{persona.nombre} tiene {edad} años")

    elif opcion == 4:
        print("elige la figura geometrica que deseas calcular")
        print("1. Triangulo")
        print("2. Rectangulo")
        print("3. Cuadrado")
        opcion_figura = int(input("Ingrese el numero de la figura geometrica que desea calcular: "))
        if opcion_figura == 1:
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            triangulo = Triangulo(base, altura)
            area = triangulo.area
            perimetro = triangulo.perimetro 
            print(f"El area del triangulo es: {area}")
            print(f"El perimetro del triangulo es: {perimetro}")
        elif opcion_figura == 2:
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            rectangulo = Rectangulo(base, altura)
            area = rectangulo.area
            perimetro = rectangulo.perimetro 
            print(f"El area del rectangulo es: {area}")
            print(f"El perimetro del rectangulo es: {perimetro}")
        elif opcion_figura == 3:
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            area = cuadrado.area
            perimetro = cuadrado.perimetro 
            print(f"El area del cuadrado es: {area}")
            print(f"El perimetro del cuadrado es: {perimetro}")