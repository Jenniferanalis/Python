""" 
Encontrar el número más grande en la lista utilizando el ciclo For
"""

list = [45, 23, 150, 89, 12, 356, 78, 90, 120]
num = list[0]

for i in list:
    if i > num:
        num = i
print(num)