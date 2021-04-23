# 2.- programa numeros.py, que permita al usuario ingresar un numero
#     imprimir CERO si ingreso 0,
#              POSITIVO si es mayor a 0,
#              NEGATIVO si menor a 0,
             
#     ERROR en cualquier otro caso.

while True:
    number = input("Ingrese un numero: ")
    try:
        val = int(number)
        if val == 0:
            print('CERO')
            break
        elif val > 0:
            print('POSITIVO')
            break
        elif val < 0:
            print('NEGATIVO')
            break


    except ValueError:
        print("ERROR")
        break    
