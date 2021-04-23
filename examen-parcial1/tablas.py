# 4.- programa tablas.py, que permita capturar un numero positivo
# e imprima su tabla de multiplicar.
# Ejemplo:

# n = 5
# 5
# 10
# 15
# ..
# 50

# n=-1

# ERROR

# NOTA: Validar que solo permita valores positivos

while True:
    number = input("Ingrese un numero: ")
    try:
        val = int(number)
        if val < 0:  
            print("Debe ser un valor positivo, intenta de nuevo. ")
            continue
        break
    except ValueError:
        print("Tiene que se un entero")     

for i in range(1, 11):
   print(val, 'x', i, '=', val*i)




