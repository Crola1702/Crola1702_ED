class map_entry():

    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
    
    def __str__(self):
        return f"({self.key}: {self.value})"