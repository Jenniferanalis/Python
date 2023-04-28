password = "password"
intentos = 1

while intentos <= 3: clave = input("Ingrese la clave: ") 
if clave == password: 
    print("Clave correcta") 
    intentos = 4
elif intentos == 3: 
    print("Cantidad de intentos completada") 
    intentos = 4 
else: print(f"Intento {intentos} Contraseña incorrecta") 
intentos += 1