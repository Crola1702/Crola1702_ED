import config
from ADT import lista as lt

class queue():
    def __init__(self):
        self.queue = lt.lista('SL')
        self.size = 0
    
    def enqueue(self, element):
        self.queue.add_first(element)
        self.size += 1
    
    def dequeue(self):
        self.size -= 1
        return self.queue.remove_first().info
    
    def peek(self):
        return self.queue.first_element()
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def size(self):
        return size
    

