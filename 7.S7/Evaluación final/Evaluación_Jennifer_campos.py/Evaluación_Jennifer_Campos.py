list_of_list = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

list_without_zeros = list(filter(lambda x: x[0] != 0, list_of_list)) 
final_lista = list(filter(lambda x: x != 0, [item for sublist in list_without_zeros for item in sublist])) 
print(final_lista)