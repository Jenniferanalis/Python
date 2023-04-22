#variable que acumula el valor ingresado por el usuario
num = 0
#ciclo par pedir el ingreso del número y que sea positivo
while True: 
    num = int(input("ingrese un numero entero positivo: "))
    if num > 0: # si el numero es mayor a 0
        break
    
factorial = 1
i = 1
while True:
    factorial *=i
    i += 1
    if i> num:
        break
        
print (f"El factorial de {num} es {factorial}")
    
    