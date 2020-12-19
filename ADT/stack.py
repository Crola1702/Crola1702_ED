import config
from ADT import lista as lt

class stack():
    def __init__(self):
        self.stack = lt.lista('SL')
        self.size = 0
    
    def push(self, element):
        self.stack.add_first(element)
        self.size += 1
    
    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.stack.remove_first().info
        return None
    
    def top(self):
        return self.stack.last_element()
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def size(self):
        return size
    

