import config
from ADT import lista as lt

class stack():
    def __init__(self):
        self.stack = lt.lista('SL')
        self.size = 0
    
    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return self.size
    
    def push(self, element):
        self.stack.add_first(element)
        self.size += 1
    
    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.stack.remove_first().info
        return None
    
    def top(self):
        return self.stack.first_element()
    
    def is_empty(self):
        return self.size == 0

if __name__ == '__main__':
    my_stack = stack()
    print(my_stack, len(my_stack))
    my_stack.push(1)
    my_stack.push(5)
    my_stack.push(3)
    my_stack.push(4)
    print(my_stack, len(my_stack))
    print(my_stack.pop(), end=',')
    print(my_stack.pop(), end=',')
    print(my_stack.pop(), end=',')
    print(my_stack.pop())
    print(my_stack, len(my_stack))
