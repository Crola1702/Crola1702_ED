#lista.py
import config
from Data_Structures.sorts import *

class array_list():
    """
    Crola1702 Implementation for an array
    """

    def __init__(self, cmpfunction, base_index=1):
        
        r""" Creates a List of Array_List type (AL)
        
        Parameters
        ----------
        cmpfunction: function
                for comparing elements
                inside the list. Uses 0 for equal
                elements and 1 or -1 for greater
                or lesser

        base_index: int
                refers the initial index of 
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
        self.pos = 0
        return self

    def __next__(self):
        if self.pos == self.size:
            raise StopIteration
        else:
            element = self.get_element(self.pos + self.base_index)
            self.pos += 1
            return element
    
    def __len__(self):
        return self.size
    
    def __contains__(self, element):
        return self.__has(element)
    
    def __getitem__(self, index):
        """
        No soporta slices.
        """
        return self.get_element(index)
    
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
        self.elements.insert(pos-self.base_index,element)
        self.size += 1
        
    
    def is_empty(self):
        """
        Retorna True si el lista está vacío, False de lo contrario
        """
        return self.size == 0
    
    def first_element(self):
        """
        Retorna el primer elemento del lista
        """
        return self.elements[0]
    
    def last_element(self):
        """
        Retorna el último elemento del lista
        """
        return self.elements[len(self.elements)-1]
    
    def get_element(self,pos):
        """
        Retorna el elemento en la posición 'pos' del lista
        """
        if pos < self.base_index or pos > self.size-1 + self.base_index:
            raise IndexError(f"\nMin Index: {self.base_index}\nMax Index: {self.size-1 + self.base_index}")
        return self.elements[pos - self.base_index]
    
    def remove_first(self):
        """
        Elimina el primer elemento del lista y lo retorna
        """
        self.size -= 1
        return self.elements.pop(0)
        
    
    def remove_last(self):
        """
        Elimina el primer elemento del lista y lo retorna
        """
        # splitted_string = self.al_string.split(',')
        # self.al_string = ','.join(splitted_string[:self.size-1])
        self.size -= 1
        return self.elements.pop(-1)
    
    def remove_pos(self,pos):
        """
        Elimina el elemento número 'pos' del lista y lo retorna
        """
        if pos == self.base_index:
            return self.remove_first()
        elif pos == (len(self.elements)-1) + self.base_index:
            return self.remove_last()
        else:
            removed_element = self.elements.pop(pos - self.base_index)
            self.size -= 1
            return removed_element
    
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
    
    def index(self, element):
        for index in range(len(self.elements)):
            if self.cmpfunction(self.elements[index], element) == 0:
                return index + self.base_index
        return -1

    def sort(self,sort='selection'):
        """
        Ordena el lista por el método de ordenamiento 'ordenamiento'
        Por defecto se utiliza el ordenamiento por selección (selection_sort)
        """
        if sort == 'selection':
            selection_sort(self)
        
        elif sort == 'insertion':
            insertion_sort(self)

    def has(self, element):
        for index in self:
            if self.cmpfunction(index, element) == 0:
                return True
        return False

if __name__ == '__main__':
    nueva_lista = array_list(base_index=-1)
    print(nueva_lista, len(nueva_lista))
    nueva_lista.add_last(4)
    nueva_lista.add_last(3)
    nueva_lista.add_last(2)
    nueva_lista.add_last(1)
    print(nueva_lista[4])
    print(nueva_lista, len(nueva_lista))
