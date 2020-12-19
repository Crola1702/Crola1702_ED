import config
from Data_Structures import map_entry as me
from Data_Structures import binary_heap as bh

class priority_queue():
    def __init__(self, pq_type='min',cmpfunction=None):
        self.type = pq_type
        self.cmpfunction = cmpfunction
        if self.type == 'min':
            self.pq = bh.b_min_heap(self.cmpfunction)
        else:
            self.pq = bh.b_max_heap(self.cmpfunction)
        self.size = 0
    
    #_______________________________
    #             API
    #_______________________________

    def insert(self, key, value):
        self.pq.insert(me.map_entry(key, value))
        self.size += 1
    
    def priority_element(self):
        if self.type == 'min':
            return self.pq.min_element()
        else:
            return self.pq.max_element()
    
    def delete_priority(self):
        self.size -= 1
        if self.type == 'min':
            return self.pq.delete_min()
        else:
            return self.pq.delete_min()
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False

#EJEMPLO CMPFUNCTION
"""
def my_cmpfunction(el1, el2):
    if el1.key > el2.key:
        return 1
    elif el1.key < el2.key:
        return -1
    return 0
"""
