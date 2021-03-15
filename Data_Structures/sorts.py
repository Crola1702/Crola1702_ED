import config
from ADT import lista as lt

def selection_sort(lista):
    pos_1 = lista.base_index
    for el1 in lista:
        min_el = el1
        pos_2 = lista.base_index
        for el2 in lista:
            if lista.cmpfunction(min_el, el2) > 0 and pos_2 > pos_1:
                min_el = el2
            pos_2 += 1
        lista.exchange(pos_1, pos_2)
        pos_1 += 1

def insertion_sort(lista):
    pos_1 = lista.base_index
    while pos_1 < lista.size:
        pos_2 = pos_1
        while (pos_2 > 1) and lista.cmpfunction(lista[pos_2], lista[pos_1]) >= 0:
            lista.exchange(pos_2, pos_2-1)
            pos_2 -= 1
        pos_1 += 1
    return lista

def greater_function(el1, el2):
    if el1 > el2:
        return 1
    elif el1 < el2:
        return -1
    return 0    

if __name__ == '__main__':
    nueva_lista = lista.lista('AL',greater_function)
    nueva_lista.add_first(5)
    nueva_lista.add_first(4)
    nueva_lista.add_first(3)
    nueva_lista.add_first(2)
    nueva_lista.add_first(1)
    selection_sort(nueva_lista)
        
            

            

        

