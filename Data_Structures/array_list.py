#lista.py
# from Estructuras.sorts import * 
import config
from Data_Structures.sorts import *

class array_list():
    """
    Crea un lista con indexación base 'base_index'
    """

    def __init__(self,cmpfunction=None,base_index=1):
        
        """
        Inicializa el lista con las variables: Size, Elements y cmpfunction
        """

        self.size = 0
        self.cmpfunction = cmpfunction
        self.base_index = base_index
        self.elements = []

    def __str__(self):
        al_string = ''
        for index in self:
            al_string += str(index) + ','
        return 'AL:[' + al_string[:len(al_string)-1] + ']'
        

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == self.size:
            raise StopIteration
        else:
            element = self.get_element(self.index + self.base_index)
            self.index += 1
            return element
    
    def __len__(self):
        return self.size
    
    #_______________________________
    #             API
    #_______________________________
    
    def add_last(self,element):
        """
        Añade un elemento al final del lista
        """
        self.size += 1
        self.elements.append(element)
        # self.al_string += ',' + str(element)

    def add_first(self,element):
        """
        Añade un elemento al comienzo del lista
        """

        self.size += 1
        self.elements.insert(0,element)
        # self.al_string = str(element) + ',' + self.al_string[1:len(self.al_string)]

    def insert_element(self,pos,element):
        """
        Añade un elemento en la posición 'pos' de la lista
        """
        self.size += 1
        self.elements.insert(pos-self.base_index,element)
            # splitted_string = self.al_string.split(',')
            # splitted_string.insert(pos-self.base_index, str(element))
            # self.al_string = ','.join(splitted_string)
        
    
    def is_empty(self):
        """
        Retorna True si el lista está vacío, False de lo contrario
        """

        if self.size == 0:
            return True
        else:
            return False
    
    def first_element(self):
        """
        Retorna el primer elemento del lista
        """

        return self.elements[0]
    
    def last_element(self):
        """
        Retorna el último elemento del lista
        """

        return self.elements[self.size-1]
    
    def get_element(self,pos):
        """
        Retorna el elemento en la posición 'pos' del lista
        """
        if pos < self.size + self.base_index:
            return self.elements[pos - self.base_index]
        else:
            return None
    
    def remove_first(self):
        """
        Elimina el primer elemento del lista y lo retorna
        """

        self.size -= 1
        # splitted_string = self.al_string.split(',')
        # self.al_string = ','.join(splitted_string[1:])
        return self.elements.pop(0)
        
    
    def remove_last(self):
        """
        Elimina el primer elemento del lista y lo retorna
        """
        # splitted_string = self.al_string.split(',')
        # self.al_string = ','.join(splitted_string[:self.size-1])
        self.size -= 1
        
        return self.elements.pop(self.size-1)
    
    def remove_pos(self,pos):
        """
        Elimina el elemento número 'pos' del lista y lo retorna
        """
        if pos == self.base_index:
            return self.remove_first()
        elif pos == (self.size-1) + self.base_index:
            return self.remove_last()
        else:
            self.size -= 1
            # splitted_string = self.al_string.split(',')
            # self.al_string = ','.join(splitted_string[:pos-self.base_index] + splitted_string[pos-self.base_index+1:])
            return self.elements.pop(pos - self.base_index)
    
    def replace(self,pos,element):
        """
        Reemplaza el valor de un elemento en la posición 'pos'
        """

        self.elements[pos - self.base_index] = element


    def exchange(self,pos1,pos2):
        """
        Intercambia dos elements en pos1 y en pos2
        """
        element1 = self.get_element(pos1)
        element2 = self.get_element(pos2)
        self.replace(pos1,element2)
        self.replace(pos2,element1)
    
    def has(self, element):
        for index in self:
            if self.cmpfunction(index, element) == 0:
                return True
        return False
    
    def index(self, element):
        for index in range(len(self)):
            if self.cmpfunction(self.elements[index], element) == 0:
                return index + self.base_index
        return None
    

    def sort(self,sort='selection'):
        """
        Ordena el lista por el método de ordenamiento 'ordenamiento'
        Por defecto se utiliza el ordenamiento por selección (selection_sort)
        """
        if sort == 'selection':
            selection_sort(self)
        
        elif sort == 'insertion':
            #print('Insertion Sort')
            pass

if __name__ == '__main__':
    nueva_lista = array_list(base_index=0)
    print(nueva_lista, len(nueva_lista))
    nueva_lista.add_first(1)
    nueva_lista.add_last(3)
    nueva_lista.insert_element(1,2)
    nueva_lista.add_last(5)
    nueva_lista.insert_element(3,4)
    print(nueva_lista, len(nueva_lista))
