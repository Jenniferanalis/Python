"""Simulación de una bomba de tiempo. 
Irá el tiempo desde el 5 al 1 en decremento. 
Al ejecutar el programa, se imprimirá el mensaje "Booom"
"""
import time
num=6
for i in range(1,num+1):
    print(num-i)
    time.sleep(1)
print("BOOM!")

