lista = [45, 23, 67, 99, 12, 356, 78, 90] 
mayor = lista[-1] 
menor = lista[0] 
repetido = 0
for elemento in lista: 
    if elemento > mayor: 
        mayor = elemento 
        if elemento < menor: 
            menor = elemento

print(mayor) 
print(menor)