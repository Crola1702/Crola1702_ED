import config
from Data_Structures import single_linked_list as sl
from Data_Structures import array_list as al

class lista():
    def __init__(self, datastructure='SL', cmpfunction=None, base_index=1):
        self.base_index = base_index
        self.size = 0
        self.cmpfunction = cmpfunction
        if datastructure == 'AL':
            self.lista = al.array_list(cmpfunction=cmpfunction, base_index=base_index)
            self.type = datastructure
        elif datastructure == 'SL':
            self.lista = sl.sl_list(cmpfunction=cmpfunction, base_index=base_index)
            self.type = datastructure

    def __str__(self):
        return self.lista.__str__()
    
    def __iter__(self):
        return self.lista.__iter__()
    
    def __next__(self):
        return self.lista.__next__()
    
    def __len__(self):
        return self.lista.__len__()
    
    def __getitem__(self, index):
        if type(index) == slice:
            raise TypeError("´__getitem__ does not support slices")
        return self.lista.__getitem__(index)
    
    def add_first(self, element):
        self.lista.add_first(element)
        self.size += 1
    
    def add_last(self, element):
        self.lista.add_last(element)
        self.size += 1
    
    def insert_element(self, pos, element):
        self.lista.insert_element(pos, element)
        self.size += 1
    
    def is_empty(self):
        return self.lista.is_empty()
    
    def first_element(self):
        return self.lista.first_element()
    
    def last_element(self):
        return self.lista.last_element()
    
    def get_element(self, pos):
        return self.lista.get_element(pos)
    
    def remove_first(self):
        self.size -= 1
        return self.lista.remove_first()
    
    def remove_last(self):
        self.size -= 1
        return self.lista.remove_last()
    
    def remove_pos(self, pos):
        self.size -= 1
        return self.lista.remove_pos(pos)
    
    def replace(self,pos,element):
        return self.lista.replace(pos, element)
    
    def exchange(self,pos1,pos2):
        return self.lista.exchange(pos1, pos2)
    
    def has(self, element):
        return self.lista.has(element)
    
    def sort(self,sort):
        return self.lista.sort(sort)

class lt_iterator():
    def __init__(self, lst):
        if lst.type == 'AL':
            self.iterator = al.al_iterator(lst)
        elif lst.type == 'SL':
            self.iterator = sl.sl_iterator(lst)
    
    def has_next(self):
        return self.iterator.has_next()
    
    def next_element(self):
        return self.iterator.next_element()

if __name__ == '__main__':
    nueva_lista = lista(base_index=0)
    nueva_lista.add_first(1)
    nueva_lista.add_last(3)
    nueva_lista.insert_element(2,2)
    nueva_lista.add_last(5)
    nueva_lista.insert_element(4,4)
    print(nueva_lista, len(nueva_lista))

    nueva_lista.remove_first()
    nueva_lista.remove_last()
    nueva_lista.remove_pos(2)
    print(nueva_lista, len(nueva_lista))

    