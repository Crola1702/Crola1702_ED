import config
from Data_Structures import tree_node as tn
from ADT import lista as lt

class rbt_tree():
    def __init__(self, cmpfunction=None):
        self.root = None
        self.cmpfunction = cmpfunction
        self.size = 0
    
    def __str__(self):
        rbt_str = "RBT:{"
        for i in self.__entry_set():
            rbt_str += str(i) + ','
        return rbt_str.strip(',') + '}'

    def __iter__(self):
        return self.key_set().__iter__()
    
    def __next__(self):
        return next(self)

    def __len__(self):
        return self.size
    
    def __getitem__(self, key):
        return self.get(key)

    #_______________________________
    #             API
    #_______________________________

    def put(self, key, value):
        if self.root is None:
            self.root = tn.tree_node(key, value)
            self.root.color = 'ROOT'
        else:
            self.__insert_node(key, value, self.root)
        self.size += 1
    
    def get(self, key):
        if self.root is None:
            return None
        else:
            node = self.__find_node(key, self.root)
            if node is not None:
                return self.__find_node(key, self.root)
            return None
    
    def contains(self, key):
        if self.root is None:
            return None
        else:
            node = self.__find_node(key, self.root)
            if node is not None:
                return True
            return False
    
    def remove(self, key):
        if self.root is None:
            return None
        else:
            node=self.__find_node(key, self.root)
            if node is not None:
                self.size -= 1
                value_copy = node.value
                if node.right is None:
                    node = node.left
                elif node.left is None:
                    node = node.right
                else:
                    node = node.left
                return value_copy
            else:
                return None
    
    def is_empty(self):
        if self.root is None:
            return True
        return False
    
    def key_set(self):
        return self.__tree_key_set(self.root, lt.lista('SL', self.cmpfunction))

    def value_set(self):
        return self.__tree_value_set(self.root, lt.lista('SL', self.cmpfunction))
    
    def min_key(self):
        if self.root is None:
            return None
        else:
            return self.__min_tree_entry(self.root).key
    
    def max_key(self):
        if self.root is None:
            return None
        else:
            return self.__max_tree_entry(self.root).key
    
    def delete_min(self):
        if self.root is None:
            return None
        else:
            return self.__delete_min_tree_key(self.root)
    
    def delete_max(self):
        if self.root is None:
            return None
        else:
            return self.__delete_max_tree_key(self.root)

    def keys_range(self, low_key, high_key):
        return self.__tree_keys_range(low_key, high_key, self.root, lt.lista('SL', self.cmpfunction))

    #_______________________________
    #          Recorridos
    #_______________________________

    def preorder(self):
        if self.root is not None:
            return self.__tree_preorder(self.root, lt.lista('SL', self.cmpfunction))
        return None

    def posorder(self):
        if self.root is not None:
            return self.__tree_posorder(self.root, lt.lista('SL', self.cmpfunction))
        return None

    def inorder(self):
        if self.root is not None:
            return self.__tree_inorder(self.root, lt.lista('SL', self.cmpfunction))
        return None

    #_______________________________
    #       Funciones Helper
    #_______________________________
    
    def __rotate_left(self, tree_parent, tree_son):
        aux_key = tree_parent.key         
        aux_value = tree_parent.value     

        tree_parent.key = tree_son.key    
        tree_parent.value = tree_son.value
        tree_son.key = aux_key            
        tree_son.value = aux_value

        aux_node = tree_parent.left       
        tree_parent.right = tree_son.right
        tree_parent.left = tree_son       
        tree_son.right = tree_son.left    
        tree_son.left = aux_node          

    def __rotate_right(self, tree_parent, tree_son, tree_grandson):
        aux_key = tree_parent.key
        aux_value = tree_parent.value

        tree_parent.key = tree_son.key    
        tree_parent.value = tree_son.value
        tree_son.key = aux_key            
        tree_son.value = aux_value

        aux_node = tree_parent.right
        tree_parent.right = tree_son
        tree_parent.left = tree_grandson
        tree_son.left = tree_son.right
        tree_son.right = aux_node

    def __insert_node(self, key, value, tree):
        node = tn.tree_node(key, value)
        cmp = self.cmpfunction(key, tree.key)
        if cmp > 0:
            if tree.right is None:
                tree.right = node
            else:
                self.__insert_node(key, value, tree.right)
        elif cmp < 0:
            if tree.left is None:
                tree.left = node
            else:
                self.__insert_node(key, value, tree.left)
        else:
            tree.value = value
        
        if tree.left is not None:
            if tree.left.left is not None and tree.left.color == 'R':
                if tree.left.left.color == 'R':
                    self.__rotate_right(tree, tree.left, tree.left.left)

        if tree.right is not None and tree.left is not None:
            if tree.left.color == 'R' and tree.right.color == 'R':
                tree.switch_color()
                tree.left.switch_color()
                tree.right.switch_color()
        
        if tree.right is not None:
            if tree.right.color == 'R':
                self.__rotate_left(tree, tree.right)

    def __find_node(self, key, tree):
        if tree is None:
            return None
        cmp = self.cmpfunction(key, tree.key)
        if cmp == 0:
            return tree
        elif cmp > 0:
            return self.__find_node(key, tree.right)
        elif cmp < 0:
            return self.__find_node(key, tree.left)
        return None

    def __tree_key_set(self, tree, lst):
        if tree is not None:
            self.__tree_key_set(tree.left, lst)
            lst.add_last(tree.key)
            self.__tree_key_set(tree.right, lst)
        return lst
    
    def __tree_value_set(self, tree, lst):
        if tree is not None:
            self.__tree_value_set(tree.left, lst)
            lst.add_last(tree.value)
            self.__tree_value_set(tree.right, lst)
        return lst

    def __entry_set(self):
        return self.__tree_entry_set(self.root, lt.lista('SL',cmpfunction=self.cmpfunction))

    def __tree_entry_set(self, tree, lst):
        if tree is not None:
            self.__tree_entry_set(tree.left, lst)
            lst.add_last(tree)
            self.__tree_entry_set(tree.right, lst)
        return lst
    
    def __min_tree_entry(self, tree):
        if tree.left is None:
            return tree
        return self.__min_tree_entry(tree.left)
    
    def __max_tree_entry(self, tree):
        if tree.left is None:
            return tree
        return self.__max_tree_entry(tree.right)
    
    def __tree_keys_range(self, low_key, high_key, tree, lst):
        if tree is not None:
            cmp_lo = self.cmpfunction(tree.key, low_key)
            cmp_hi = self.cmpfunction(tree.key, high_key)
            if cmp_lo >= 0 and cmp_hi <= 0:
                lst.add_last(tree.key)
            if cmp_lo > 0:
                self.__tree_keys_range(low_key, high_key, tree.left, lst)
            if cmp_hi < 0:
                self.__tree_keys_range(low_key, high_key, tree.right, lst)
            return lst

    def __tree_preorder(self, tree, lst):
        if tree is not None:
            lst.add_last(tree.key)
            self.__tree_preorder(tree.left, lst)
            self.__tree_preorder(tree.right, lst)
        return lst
    
    def __tree_posorder(self, tree, lst):
        if tree is not None:
            self.__tree_posorder(tree.left, lst)
            self.__tree_posorder(tree.right, lst)
            lst.add_last(tree.key)
        return lst

    def __tree_inorder(self, tree, lst):
        if tree is not None:
            self.__tree_inorder(tree.left, lst)
            lst.add_last(tree.key)
            self.__tree_inorder(tree.right, lst)
        return lst
        

def my_cmpfunction(el1, el2):
    if el1 > el2:
        return 1
    elif el1 < el2:
        return -1
    return 0

if __name__ == '__main__':
    tree = rbt_tree(my_cmpfunction)
    tree.put('B','B')
    tree.put('A','A')
    tree.put('C','C')
    # print(tree)
    print(tree.get('B'))
    print(tree.get('C'))
    print(tree.get('A'))
    
