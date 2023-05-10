"""
Dada la siguiente lista de nombres: •Harry Houdini, •Newton, •David Blaine,•Hawking, •Messi, •Teller, •Einstein, •Pele,•Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y Einstein son científicos.
Debemos separar los nombres en tres grupos: magos, científicos y otros; y escribir  una  función
llamada hacer_grandioso(), que  modifique  la  lista  de  magos  añadiendo  la frase "El gran" antes del nombre de cada mago.
Crear  una  función  llamada imprimir_nombres(),  que  imprime  el  nombre  de  cada personade de la lista.
Finalmente, imprimir en  pantalla  la  lista completa  de  nombres antes  de  ser  modificados;
luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.
"""


# Crear funcion hacer_grandioso() para modificar la lista de magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

# funcion imprimr_nombres()

def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# funcion para crear lista nueva

def crear_listas(magos, cientificos, otros, lista_nombres):
    for nombre in lista_nombres:
        if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
            magos.append(nombre)
        elif nombre in ['Newton', 'Hawking', 'Einstein']:
            cientificos.append(nombre)
        else:
            otros.append(nombre)



# lista de nombres
lista_nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

# grupos diferentes para cada nombre
magos = []
cientificos = []
otros = []

crear_listas(magos, cientificos, otros, lista_nombres)

diccionario = {'magos': magos,'cientificos': cientificos,'otros': otros,
'nombres': lista_nombres}

# # imprimimos la lista completa de personajes
print('La lista completa de personajes es: ')
imprimir_nombres(lista_nombres)

# Magos
print('--------------Los magos grandiosos son: -----------------')
hacer_grandioso(magos)
imprimir_nombres(magos)

# cientificos
print('------------Los nombres de los científicos son: --------------')
imprimir_nombres(cientificos)

# otros
print('--------Los restantes son: --------------')
imprimir_nombres(otros)