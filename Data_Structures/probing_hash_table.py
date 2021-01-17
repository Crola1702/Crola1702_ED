import config
from Data_Structures.map_entry import *
from ADT import lista as lt

class probing_ht():

    def __init__(self,initial_elements=17,load_factor=0.5,cmpfunction=None):
        self.size = 0
        self.spaces = initial_elements
        self.load_factor = load_factor
        self.current_factor = load_factor
        self.cmpfunction = cmpfunction
        self.table = lt.lista('AL', cmpfunction, 0)
        for bucket in range(initial_elements * int(load_factor**-1)):
            self.table.add_last(map_entry())
    
    def __str__(self):
        cht_str = ""
        for i in self.__entry_set():
            cht_str += str(i) + ','
        return "PHT:{" + cht_str[:len(cht_str)-1] + '}'

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
        entry = map_entry(key, value)
        iterations = 0
        inserted = False
        while not inserted and iterations < self.table.size:
            bucket = self.table.get_element(table_pos)
            if bucket.key is None or bucket.key == '__EMPTY__':
                bucket.key = key
                bucket.value = value
                self.size += 1
                self.current_factor = float(self.size/self.spaces)
                inserted = True
            else:
                table_pos += 1
                if table_pos >= self.table.size:
                    table_pos = 0
            iterations += 1
    
        if self.current_factor > self.load_factor:
            self.__rehash()
    
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
        entry  = self.__find(key)
        if entry is not None:
            copy_entry = map_entry(entry.key, entry.value)
            entry.key = '__EMPTY__'
            entry.value = '__EMPTY__'
            return copy_entry
    
    def is_empty(self):
        if self.size == 0:
            return False
        else:
            return True
    
    def key_set(self):
        key_list = lt.lista('SL', self.cmpfunction)
        for entry in self.table:
            if entry.key is not None and entry.key != '__EMPTY__':
                key_list.add_last(entry.key)
        return key_list

    def value_set(self):
        value_list = lt.lista('SL', self.cmpfunction)
        for entry in self.table:
            if entry.key is not None and entry.key != '__EMPTY__':
                value_list.add_last(entry.value)
        return value_list
    
    #_______________________________
    #       HELPER FUNCTIONS
    #_______________________________

    def __entry_set(self):
        entry_list = lt.lista('SL', self.cmpfunction)
        for entry in self.table:
            if entry.key is not None and entry.key != '__EMPTY__':
                entry_list.add_last(entry)
        return entry_list

    def __hash_value(self, key):
        return abs(hash(key))%self.spaces

    def __rehash(self):
        self.spaces *= 2
        self.size = 0
        old_table = self.table
        new_table = lt.lista('AL', self.cmpfunction, 0)
        self.table = new_table
        for bucket in range(self.spaces):
            self.table.add_first(map_entry())
        
        for bucket in old_table:
            if bucket.key is not None and bucket.key != '__EMPTY__':
                self.put(bucket.key, bucket.value)

    def __find(self, key):
        table_pos = self.__hash_value(key)
        iterations = 0
        found = False
        while not found or iterations < self.table.size:
            bucket = self.table.get_element(table_pos)
            if bucket.key == key:
                return bucket
            elif bucket.key == None:
                return None
            else:
                table_pos += 1
                if table_pos >= self.table.size:
                    table_pos = 0
            iterations += 1

if __name__ == '__main__':
    new_ht = probing_ht(initial_elements=1)
    print(new_ht, len(new_ht))
    for i in range(8):
        new_ht.put(f"K{i}",f"V{i}")

    print(new_ht, len(new_ht))