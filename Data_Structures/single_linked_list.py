#lista_encadenada.py
import config
from Data_Structures.sorts import *
class sl_node():

    def __init__(self, info: any = None, next = None):
        self.info = info
        self.next = next
    
    def __str__(self):
        node_str = ""
        if self.next is not None:
            return f"(info: {str(self.info)}, next: {str(self.next.info)})"
        else:
            return f"(info: {str(self.info)}, next: None)"

class sl_list():

    def __init__(self, cmpfunction = None, base_index=1):
        self.size = 0
        self.first = None
        self.last = None
        self.cmpfunction = cmpfunction
        self.base_index = base_index
    
    def __str__(self):
        sl_string = ''
        for i in self:
            sl_string += str(i) + ','
        return 'SL:[' + sl_string[:len(sl_string)-1] +']'


    def __iter__(self):
        self.current_node = self.first
        return self
    
    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        else:
            ret_info = self.current_node.info
            self.current_node = self.current_node.next
            return ret_info
    
    def __len__(self):
        return self.size
    
    def __contains__(self, element):
        return self.__has(element)

    def __getitem__(self, index):
        """
        No soporta slices
        """
        return self.get_element(index)

    def add_first(self,elemento):
        nodo = sl_node(elemento,self.first)
        if self.last is None:
            self.last = nodo
        self.first = nodo
        self.size += 1

    def add_last(self,elemento):
        nodo = sl_node(elemento)
        prev_last = self.last
        if prev_last is not None:
            prev_last.next = nodo
        elif self.first is None:
            self.first = nodo
        self.last = nodo
        self.size += 1
    
    def first_element(self):
        if self.first is None:
            return None
        return self.first.info
    
    def last_element(self):
        if self.last is None:
            return None
        return self.last.info

    def insert_element(self, pos, elemento):
        if pos == self.base_index:
            self.add_first(elemento)
        elif pos == self.size + self.base_index:
            self.add_last(elemento)
        else:
            nodo = sl_node(info=elemento)
            prev_node = self.__get(pos - 1)
            next_node = self.__get(pos)
            prev_node.next = nodo
            nodo.next = next_node
            self.size += 1
    
    def is_empty(self):
        return self.size == 0
    
    def get_element(self, pos):
        if pos < self.base_index or pos > self.size-1 + self.base_index:
            raise IndexError(f"\nMin Index: {self.base_index}\nMax Index: {self.size-1 + self.base_index}")
        return self.__get(pos).info

    def remove_first(self):
        removed_node = self.first
        new_node = self.first.next
        self.first = new_node
        self.size -= 1
        return removed_node.info

    def remove_last(self):
        removed_node = self.last
        if self.size > 1:
            new_last = self.__get((self.size-2) + self.base_index)
            new_last.next = None
            self.last = new_last
            self.size -= 1
        elif self.size == 1:
            self.first = None
            self.last = None
            self.size = 0
        return removed_node.info
    
    def remove_pos(self, pos):
        if pos == self.base_index:
            return self.remove_first()
        elif pos == self.size-1 + self.base_index:
            return self.remove_last()
        else:
            removed_node = self.__get(pos)
            new_pos = self.__get(pos-1)
            new_pos.next = removed_node.next    
            self.size -= 1
            return removed_node.info
    
    def replace(self, pos, element):
        node = self.__get(pos)
        node.info = element
    
    def exchange(self, pos1, pos2):
        node1_info = self.__get(pos1).info
        node2_info = self.__get(pos2).info
        self.replace(pos1,node2_info)
        self.replace(pos2,node1_info)

    def has(self, element):
        if self.__find(element) is not None:
            return True
        return False
    
    def index(self, element) -> int:
        local_pos = self.base_index
        local_node = self.first
        while local_node is not None:
            if (self.cmpfunction(element, local_node.info) == 0):
                return local_pos
            local_pos += 1
            local_node = local_node.next
        return -1
                

    def sort(self, sort='selection'):
        if sort == 'selection':
            selection_sort(self)
        elif sort == 'insertion':
            insertion_sort(self)

    # HELPER FUNCTIONS

    def __get(self, pos):
        local_pos = self.base_index
        local_node = self.first
        while local_node is not None:
            if local_pos == pos:
                return local_node
            local_node = local_node.next
            local_pos += 1
        return None
    
    def __find(self, element):
        local_pos = self.base_index
        for local_node in self:
            if self.cmpfunction(local_node, element) == 0:
                return local_pos
            local_pos += 1
        return None

if __name__ == '__main__':
    nueva_lista = sl_list()
    print(nueva_lista, len(nueva_lista))
    nueva_lista.add_last(1)
    nueva_lista.add_last(2)
    nueva_lista.add_last(3)
    nueva_lista.add_last(4)
    print(nueva_lista[1])
    print(nueva_lista, len(nueva_lista))
        