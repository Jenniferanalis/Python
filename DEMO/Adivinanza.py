import random 
numero_random = random.randint(0, 10) #print(numero_random)
print("""Bienvenido al juego de adivinanzas,deberas adivinar un numero de 0 a 10 """) 
adivinanza = 11
contador = 0
while adivinanza != numero_random: 
    adivinanza = int(input("Ingresa un numero del 0 al 10: ")) 
    contador += 1 
    if adivinanza > numero_random: 
        print("el numero es mayor al numero a adivinar") 
    elif adivinanza < numero_random: print("el numero es menor al numero a adivinar") 
    else: print( f"Adivinaste! el numero era {numero_random} en , {contador} intentos")