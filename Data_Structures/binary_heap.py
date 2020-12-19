import config
from Data_Structures import array_list as al
from ADT import lista as lt

class b_min_heap():
    def __init__(self, cmpfunction=None):
        self.size = 0
        self.cmpfunction = cmpfunction
        self.heap = lt.lista('AL', self.cmpfunction)
    
    #_______________________________
    #             API
    #_______________________________

    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def min_element(self):
        if self.size == 0:
            return None
        return self.heap.get_element(1)

    def insert(self, element):
        self.heap.add_last(element)
        self.size += 1
        self.sift_up(self.size)

    def delete_min(self):
        if self.size == 0:
            return None
        copy_min = self.min_element()
        self.heap.exchange(1, self.size)
        self.heap.remove_last()
        self.size -= 1
        self.sift_down(1)
        return copy_min

    #_______________________________
    #       Funciones Helper
    #_______________________________

    def sift_up(self, position):
        if position != 1:
            cmp = self.cmpfunction(self.heap.get_element(position), self.heap.get_element(position//2))
            if cmp < 0:
                self.heap.exchange(position, position//2)
                self.sift_up(position//2)

    def sift_down(self, position):
        left_son = self.heap.get_element(position*2)
        right_son = self.heap.get_element(position*2+1)

        if left_son is not None:
            cmp_parent_left = self.cmpfunction(self.heap.get_element(position), left_son)

            if right_son is None:
                if cmp_parent_left > 0:
                    self.heap.exchange(position, position*2)
                
            else:
                cmp_parent_right = self.cmpfunction(self.heap.get_element(position), right_son)
                cmp_sons = self.cmpfunction(left_son, right_son)

                if cmp_sons < 0 and cmp_parent_left > 0:
                    self.heap.exchange(position, position*2)
                    self.sift_down(position*2)

                elif cmp_sons > 0 and cmp_parent_right > 0:
                    self.heap.exchange(position, position*2+1)
                    self.sift_down(position*2+1)

class b_max_heap():
    def __init__(self, cmpfunction=None):
        self.size = 0
        self.cmpfunction = cmpfunction
        self.heap = lt.lista('AL', self.cmpfunction)
    
    #_______________________________
    #             API
    #_______________________________

    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def max_element(self):
        if self.size == 0:
            return None
        return self.heap.get_element(1)

    def insert(self, element):
        self.heap.add_last(element)
        self.size += 1
        self.sift_up(self.size)

    def delete_max(self):
        if self.size == 0:
            return None
        copy_min = self.max_element()
        self.heap.exchange(1, self.size)
        self.heap.remove_last()
        self.size -= 1
        self.sift_down(1)
        return copy_min

    #_______________________________
    #       Funciones Helper
    #_______________________________

    def sift_up(self, position):
        if position != 1:
            cmp = - self.cmpfunction(self.heap.get_element(position), self.heap.get_element(position//2))
            if cmp < 0:
                self.heap.exchange(position, position//2)
                self.sift_up(position//2)

    def sift_down(self, position):
        left_son = self.heap.get_element(position*2)
        right_son = self.heap.get_element(position*2+1)

        if left_son is not None:
            cmp_parent_left = -self.cmpfunction(self.heap.get_element(position), left_son)

            if right_son is None:
                if cmp_parent_left > 0:
                    self.heap.exchange(position, position*2)
                
            else:
                cmp_parent_right = -self.cmpfunction(self.heap.get_element(position), right_son)
                cmp_sons = -self.cmpfunction(left_son, right_son)

                if cmp_sons < 0 and cmp_parent_left > 0:
                    self.heap.exchange(position, position*2)
                    self.sift_down(position*2)

                elif cmp_sons > 0 and cmp_parent_right > 0:
                    self.heap.exchange(position, position*2+1)
                    self.sift_down(position*2+1)

def my_cmpfunction(el1, el2):
    if el1 > el2:
        return 1
    elif el1 < el2:
        return -1
    return 0
