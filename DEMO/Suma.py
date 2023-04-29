"""
Calcular la suma de todos los números usando ciclo while
"""

numeros = [3, 5, 2, 8, 1, 10]
i=0
suma=0
while i < len(numeros):
    suma = suma + numeros[i] #suma += numeros[i]
    i= i+1
    
print(f"La suma es {suma}")