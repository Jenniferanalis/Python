# Definir variables y listas

lista_pers = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking','Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

magos = [lista_pers[0], lista_pers[2], lista_pers[5]]

cientificos = [lista_pers[1], lista_pers[3], lista_pers[6]]

otros = [lista_pers[4], lista_pers[7], lista_pers[8]]

# Definir funcion grandes magos


def hacer_grandioso(mago):
    i=0
    for mago in magos:
        mago = "El gran " + mago
        magos[i] = mago
        i += 1
        return magos




# Definir función que imprime nombres

def imprimir_nombres(lista):
    for persona in lista:
        print(f"{persona}")


# Definir función que imprime lo solicitado

def imprimir_listas(lista1, lista2, lista3, lista4):
    print(f"\nLa lista dada es: {lista1}")
    print("\n** LOS GRANDIOSOS MAGOS SON: **")
    imprimir_nombres(hacer_grandioso(lista2))
    print("\n** LOS CIENTÍFICOS SON: **")
    imprimir_nombres(lista3)
    print("\n** LAS OTRAS PERSONAS SON: **")
    imprimir_nombres(lista4)

imprimir_listas(lista_pers, magos, cientificos, otros)