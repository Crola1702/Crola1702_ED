#chaining_hash_table.py

import config
from ADT import lista as lt
from Data_Structures.map_entry import *

class chaining_ht():

    def __init__(self, initial_elements=17, load_factor=2, cmpfunction=None):
        self.size = 0
        self.spaces = initial_elements
        self.load_factor = load_factor
        self.cmpfunction = cmpfunction
        self.table = lt.lista('AL', cmpfunction, 0)
        for i in range(self.spaces):
            bucket = lt.lista('SL',cmpfunction)
            for j in range(int(load_factor)):
                bucket.add_last(map_entry())
            self.table.add_last(bucket)
    
    def __str__(self):
        cht_str = ""
        for i in self.__entry_set():
            cht_str += str(i) + ','
        return 'CHT:{' + cht_str[:len(cht_str)-1] + '}'

    def __iter__(self):
        return self.key_set().__iter__()
    
    def __next__(self):
        return next(self)
    
    def __len__(self):
        return self.size
    
    def __contains__(self, key):
        return self.__contains(key)
    
    def __getitem__(self, key):
        return self.get(key)

    #_______________________________
    #              API
    #_______________________________

    def put(self, key, value):
        table_pos = self.__hash_value(key)
        replaced = False
        bucket = self.table.get_element(table_pos)
        for entry in bucket:
            if entry.key is None and not replaced:
                entry.key = key
                entry.value = value
                replaced = True
                self.size += 1

            if entry.key == key:
                entry.value = value
                replaced = True

            

        if not replaced:
            bucket.add_last(map_entry(key, value))
            self.size += 1

    def get(self, key):
        entry = self.__find(key)
        if entry is not None:
            return self.__find(key)
        return None

    def __contains(self, key):
        if self.__find(key) is not None:
                return True
        return False       
        
    def remove(self, key):
        entry = self.__find(key)
        if entry is not None:
            copy_entry = map_entry(entry.key, entry.value)
            entry.key = None
            entry.value = None
            return copy_entry
    
    def is_empty(self):
        if self.size == 0:
            return False
        else:
            return True
    
    def key_set(self):
        key_list = lt.lista('SL', self.cmpfunction)
        for bucket in self.table:
            for entry in bucket:
                if entry.key is not None:
                    key_list.add_last(entry.key)
        return key_list

    def value_set(self):
        value_list = lt.lista('SL', self.cmpfunction)
        for bucket in self.table:
            for entry in bucket:
                if entry.info.key is not None:
                    value_list.add_last(entry.value)
        return value_list

    #_______________________________
    #       HELPER FUNCTIONS
    #_______________________________

    def __entry_set(self):
        entry_list = lt.lista('SL', self.cmpfunction)
        for bucket in self.table:
            for entry in bucket:
                if entry.key is not None:
                    entry_list.add_last(entry)
        return entry_list

    def __find(self, key):
        table_pos = self.__hash_value(key)
        bucket = self.table.get_element(table_pos)
        for entry in bucket:
            if entry.key == key:
                return entry
        return None

    def __hash_value(self,key):
        return abs(hash(key))%self.spaces

if __name__ == '__main__':
    new_ht = chaining_ht(initial_elements=4)
    print(new_ht, len(new_ht))
    for i in range(8):
        new_ht.put(f"K{i}",f"V{i}")

    print(new_ht, len(new_ht))
    