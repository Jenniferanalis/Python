"""Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla.
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay
entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1."""

#variable que acumula el valor ingresado por el usuario
num = 0
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
    
    