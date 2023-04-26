"""
Realizar el calculo de la hipotenusa requiriendo el ingreso del cateto a y cateto b por parte del usuario en consola
"""

import math

cateto_a = float(input("Ingrese el cateto a : "))

cateto_b = float(input("Ingrese el cateto b : "))

hipotenusa = math.sqrt(cateto_a**2 +cateto_b**2)

print (f"la hipotenusa es {hipotenusa}")