import config
from Data_Structures import chaining_hash_table as cht
from Data_Structures import probing_hash_table as pht

class mapa():
    def __init__(self, datastructure='CHT', initial_elements=17, load_factor=2, cmpfunction=None):
        self.map = None
        if datastructure == 'CHT':
            self.map = cht.chaining_ht(initial_elements=initial_elements,load_factor=load_factor,cmpfunction=cmpfunction)
            self.type = datastructure
        elif datastructure == 'PHT':
            if load_factor > 1:
                load_factor = load_factor**-1
            self.map = pht.probing_ht(initial_elements=initial_elements,load_factor=load_factor,cmpfunction=cmpfunction)
            self.type = datastructure
    
    def __str__(self):
        return self.map.__str__()
    
    def __iter__(self):
        return self.map.__iter__()
    
    def __next__(self):
        return self.map.__next__()
    
    def __len__(self):
        return self.map.__len__()
    
    def __contains__(self, key):
        return self.map.__contains__(key)
    
    def __getitem__(self, key):
        return self.map.__getitem__(key)

    #_______________________________
    #              API
    #_______________________________ 

    def put(self, key, value):
        self.map.put(key, value)
    
    def get(self, key):
        return self.map.get(key)
    
    def contains(self, key):
        return self.map.contains(key)
    
    def remove(self, key):
        return self.map.remove(key)

    def size(self):
        return self.map.size()
    
    def is_empty(self):
        return self.map.is_empty()
    
    def key_set(self):
        return self.map.key_set()
    
    def value_set(self):
        return self.map.value_set()
    
    def entry_set(self):
        return self.map.entry_set()

if __name__ == '__main__':
    new_ht = mapa('PHT')
    print(new_ht, len(new_ht))
    for i in range(8):
        new_ht.put(f"K{i}",f"V{i}")

    print(new_ht['K4'])
    print(new_ht, len(new_ht))
