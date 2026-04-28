print("--Calculadora Simple--")

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

operacion = input("Elige una operación (+, -, *, /): ")

resultado = 0
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 == 0:
        print("No se puede dividir entre 0")
    else:
        resultado = numero1 / numero2
else:
    print("Operación no válida")

if operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/":
    if not (operacion == "/" and numero2 == 0):
        print(f"El resultado es: {resultado}")
