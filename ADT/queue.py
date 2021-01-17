import config
from ADT import lista as lt

class queue():
    def __init__(self):
        self.queue = lt.lista('SL')
        self.size = 0

    def __str__(self):
        return str(self.queue)

    def __len__(self):
        return self.size
    
    def enqueue(self, element):
        self.queue.add_last(element)
        self.size += 1
    
    def dequeue(self):
        self.size -= 1
        return self.queue.remove_first().info
    
    def peek(self):
        return self.queue.first_element()
    
    def is_empty(self):
        return self.size == 0

if __name__ == '__main__':
    my_queue = queue()
    print(my_queue, len(my_queue))
    my_queue.enqueue(1)
    my_queue.enqueue(5)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    print(my_queue, len(my_queue))
    print(my_queue.dequeue(), end=',')
    print(my_queue.dequeue(), end=',')
    print(my_queue.dequeue(), end=',')
    print(my_queue.dequeue())
    print(my_queue, len(my_queue))