import config
from Data_Structures import bst_tree as bst
from Data_Structures import rbt_tree as rbt

class ordered_map():
    def __init__(self, datastructure='RBT', cmpfunction=None):
        self.size = 0
        if datastructure == 'BST':
            self.tree = bst.bst_tree(cmpfunction)
            self.type = datastructure
        elif datastructure == 'RBT':
            self.tree = rbt.rbt_tree(cmpfunction)
            self.type = datastructure
        self.cmpfunction = cmpfunction

    def __str__(self):
        return self.tree.__str__()

    def __iter__(self):
        return self.tree.__iter__()

    def __next__(self):
        return self.tree.__next__()

    def __getitem__(self, key):
        return self.tree.__getitem__(key)
    
    def __contains__(self, key):
        return self.tree.contains(key)
    
    def put(self, key, value):
        self.tree.put(key, value)
        self.size += 1
    
    def get(self, key):
        return self.tree.get(key)
    
    def remove(self, key):
        self.size -= 1
        return self.tree.remove(key)
    
    def contains(self, key):
        return self.tree.contains(key)
    
    def is_empty(self):
        return self.tree.is_empty()
    
    def key_set(self):
        return self.tree.key_set()
    
    def value_set(self):
        return self.tree.value_set()
    
    def min_key(self):
        return self.tree.min_key()
    
    def max_key(self):
        return self.max_key()
    
    def delete_min(self):
        return self.delete_min()
    
    def delete_max(self):
        return self.delete_max()
    
    def keys_range(self, low_key, high_key):
        return self.keys_range(low_key, high_key)

def my_cmpfunction(el1, el2):
    if el1 > el2:
        return 1
    elif el1 < el2:
        return -1
    else:
        return 0

if __name__ == '__main__':
    ordered_map('BST', my_cmpfunction)
