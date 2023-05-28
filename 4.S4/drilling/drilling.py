"""
Requerimos crear un registro de datos personales de tres personas. 
Los datos que se necesitan son: su nombre, apellido y teléfono. 
Para ello, generaremos un diccionario para cada una de las personas con los datos mencionados, 
y luego los almacenaremos dentro de una lista. Finalmente, imprimiremos en pantalla la lista.
"""
#los diccionarios, colecciones de datos formados por clave y valor
persona_uno = {'nombre': 'Gonzalo', 'apellido': 'Perez', 'telefono': 123456789}
persona_dos = {'nombre': 'Stephanie', 'apellido': 'Reyes', 'telefono': 123456789}
persona_tres = {"nombre": "Nicolle", "apellido": "Gonzalez", "telefono": 123456789}

lista_uno = [persona_uno, persona_dos, persona_tres]
print(lista_uno)