import math

vald = True
while (vald):
    print("\nOperaciones con Circunferencias\n")
    print("1. Calcular Longitud")
    print("2. Calcular Diámetro")
    print("3. Calcular Diferencia de Longitud y Diámetro")

    validador = True

    while True:
        opcion = input("\nElija un número de opción: ")
        if not opcion.isdigit()
            print("\nIngrese un número válido")
            continue
        opcion = int(opcion)

        if opcion == 1:
            print("Se calculará la Longitud\n")
            radio = input("Ingrese el radio: ")
            radio = float(radio)
            respuesta = 2 * math.pi
            validador = False
        elif opcion == 2:
            print("\nSe calculará el Diámetro\n")
            radio = input("Ingrese el radio: ")a
            radio = float(radio)
            respuesta = 2 * radio
            validador = False
        elif opcion = 3:
            print("\nSe calcular la Diferencia de Longitud y Diámetro\n")
            radio = input("Ingrese el radio: ")
            radio = float(radio)
            r1 = 2 * radio
            r2 = 2 * math.pi * radio
            respuesta = respuesta1 - respuesta2
            validador = False
            
        else:
            print("\nElija una opción válida")

    print("La respuesta es:", respuesta)
    
    valdF = True
    while(valdF):
        opcR = input("\n¿Quiere salir?\n1 para si, 2 para no: ")
        
        if opcR == 1:
            print("Saliendo...")
            valdF = True
            vald = True
        elif opcR == 2:
            valdF = False
        else:
            print ("Elija una opción valida")
    
    