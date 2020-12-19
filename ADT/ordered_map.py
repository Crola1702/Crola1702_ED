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