def validate_input_float(texto): 
    
    while True: 
        try: 
            r = float(input(texto)) #float(), str(), int() casteo o transformacion, conversion del tipo de dato 
            if r > 0: 
                abs(r)
                return r 
    
            else: 
                print("El valor es menor a 0") 
                
        except Exception as e: 
            print("Ha ocurrido un error en el ingreso de la resistencia ",e) 
            print("Ha ocurrido un error, ingrese de nuevo el valor de la resistencia")
        
r_1 = validate_input_float("Ingrese la resistencia 1: ") ##lamada a funcion o invocando
r_2 = validate_input_float("Ingrese la resistencia 2: ")
r_3 = validate_input_float("Ingrese la resistencia 3: ")

# calcular la resistencia total
resistencia_total = 1/((1/r_1) + (1/r_2) + (1/r_3))

# imprimir la resistencia total en consola
print("La resistencia total es de", resistencia_total)