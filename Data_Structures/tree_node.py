class tree_node():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'R'
    
    def __str__(self):
        return f"({self.key}: {self.value})"

    def __delattr__(self, name):
        if name == 'left':
            self.left = None
        elif name == 'right':
            self.right = None
        elif name == 'parent':
            self.parent = None
    
    def __eq__(self, other):
        return self.key == other.key
    
    def switch_color(self):
        if self.color == 'B':
            self.color = 'R'
        elif self.color == 'R':
            self.color = 'B'        

if __name__ == '__main__':
    a = tree_node('A','A')
    a.left = tree_node('B','B')
    del a.left
    print(a, a.left)
    
