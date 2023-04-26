"""
Pedir el ingreso de dos textos al usuario por consola y comparar si son iguales o del mismo tamaño
"""

texto_1 = input("Ingrese el primer texto: ")
texto_2 = input("Ingrese el segudo texto: ")

if texto_1 == texto_2 or len(texto_2) == len(texto_1): 
    print("su texto es igual o tiene el mismo tamaño" ) 
else: print("no tienen el mismo tamaño o no son iguales")
