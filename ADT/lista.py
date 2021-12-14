from typing import Callable
import config
from Data_Structures import single_linked_list as sl
from Data_Structures import array_list as al

class lista():
    def __init__(self, datastructure: str = 'SL', cmpfunction: Callable[[any, any], int] = None, base_index: int = 1):
        self.base_index = base_index
        self.size = 0
        self.cmpfunction = cmpfunction
        if cmpfunction is None:
            self.cmpfunction = self.__default_cmp_function
        if datastructure == 'AL':
            self.lista = al.array_list(cmpfunction=self.cmpfunction, base_index=base_index)
            self.type = datastructure
        elif datastructure == 'SL':
            self.lista = sl.sl_list(cmpfunction=self.cmpfunction, base_index=base_index)
            self.type = datastructure
        else:
            raise TypeError("No such datastructure")

    def __str__(self) -> str:
        return self.lista.__str__()

    def __repr__(self) -> str:
        return self.lista.__repr__()
    
    def __iter__(self):
        return self.lista.__iter__()
    
    def __next__(self):
        return self.lista.__next__()
    
    def __len__(self):
        return self.lista.__len__()
    
    def __getitem__(self, index):
        if type(index) == slice:
            raise TypeError("__getitem__ does not support slices")
        return self.lista.__getitem__(index)
    
    def add_first(self, element: any) -> None:
        """
        Adds an element to de first position of the array
        """
        self.lista.add_first(element)
        self.size += 1
    
    def add_last(self, element: any) -> None:
        """
        Adds an element to de last position of the array
        """
        self.lista.add_last(element)
        self.size += 1
    
    def insert_element(self, pos: int, element: any) -> None:
        """
        Inserts an element before the index \'pos\'
        """
        self.lista.insert_element(pos, element)
        self.size += 1
    
    def is_empty(self) -> bool:
        """
        Return \'True\' if the list has no elements
        \'False\' in other case
        """
        return self.lista.is_empty()
    
    def first_element(self) -> any:
        """
        Returns the first element of the list
        """
        return self.lista.first_element()
    
    def last_element(self) -> any:
        """
        Returns the las element of the list
        """
        return self.lista.last_element()
    
    def get_element(self, pos: int) -> any:
        """
        Returns the element at index \'pos\' of the list
        """
        return self.lista.get_element(pos)
    
    def remove_first(self) -> any:
        """
        Removes the firs element of the list and returns it
        """
        self.size -= 1
        return self.lista.remove_first()
    
    def remove_last(self) -> any:
        """
        Removes the last element of the list and returns it
        """
        self.size -= 1
        return self.lista.remove_last()
    
    def remove_pos(self, pos: int) -> any:
        """
        Removes the element at index \'pos\' and returns it
        """
        self.size -= 1
        return self.lista.remove_pos(pos)
    
    def replace(self, pos: int, element: any) -> any:
        """
        Replaces the element at index \'pos\' with the given element
        """
        return self.lista.replace(pos, element)
    
    def exchange(self, pos1: int, pos2: int) -> None: 
        """
        Exchanges the position of elements at indices \'pos1\' and \'pos2\'
        """
        return self.lista.exchange(pos1, pos2)
    
    def has(self, element: any) -> bool:
        """
        Returns \'True\' if the list has the given element
        It compares it by the given cmpfunction
        """
        return self.lista.has(element)

    def index(self, element: any) -> int:
        """
        Returns the index of the given element or \'-1\' if it's not found
        """
        return self.lista.index(element)
    
    def sublist(self, start: int, num_elements: int):
        """
        Creates a sublist from the \'start\' index and the given number of elements
        The return type of the function is a Single Linked list
        """
        ret_list = lista(datastructure='SL', cmpfunction=self.cmpfunction, base_index=self.base_index)
        iter = lt_iterator(self.lista)
        i = 0
        while iter.has_next() and i<=num_elements:
            element = iter.next_element()
            if (self.base_index >= start):
                ret_list.add_last(element)
                i += 1
        return ret_list
    
    def sort(self, sort: str = 'selection'):
        """
        Sorts the list with the given sort method
        """
        return self.lista.sort(sort)

    def __default_cmp_function(self, el1, el2):
        if (el1 > el2):
            return 1
        elif (el1 < el2):
            return -1
        return 0

class lt_iterator():
    def __init__(self, lst: lista):
        if lst.type == 'AL':
            self.iterator = al.al_iterator(lst)
        elif lst.type == 'SL':
            self.iterator = sl.sl_iterator(lst)
    
    def has_next(self) -> bool:
        return self.iterator.has_next()
    
    def next_element(self) -> any:
        return self.iterator.next_element()

if __name__ == '__main__':
    nueva_lista = lista(base_index=0)
    nueva_lista.add_first(1)
    nueva_lista.add_last(3)
    nueva_lista.insert_element(2,2)
    nueva_lista.add_last(5)
    nueva_lista.insert_element(4,4)
    print(nueva_lista, nueva_lista.size)

    nueva_lista.remove_first()
    print(nueva_lista, nueva_lista.size)
    nueva_lista.remove_last()
    nueva_lista.remove_pos(2)
    print(nueva_lista, nueva_lista.size)

    