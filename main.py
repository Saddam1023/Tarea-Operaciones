import Operaciones

print("=== CALCULADORA BASICA ===")

try:
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))
except ValueError:
    print("Error: debe ingresar numeros validos.")
else:
    print("\nSeleccione una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    opcion = input("Ingrese una opcion (1-4): ").strip()

    if opcion == "1":
        resultado = Operaciones.sumar(numero1, numero2)
    elif opcion == "2":
        resultado = Operaciones.restar(numero1, numero2)
    elif opcion == "3":
        resultado = Operaciones.multiplicar(numero1, numero2)
    elif opcion == "4":
        resultado = Operaciones.dividir(numero1, numero2)
    else:
        resultado = "Error: opcion no valida."

    print("Resultado:", resultado)
