radio = float(input("Ingrese el valor del Radio: "))
altura = float (input("Ingrese el valor de la Altura: "))
pi = 3.14

volumen = pi * radio**2 * altura
Superficie = -2 * pi * radio * altura + 2 * pi * radio**2

print("El volumen del cilindro es: ", volumen)
print("La superficie del cilindro es: ", Superficie)
print("El resultado de la suma es : ", volumen - Superficie)