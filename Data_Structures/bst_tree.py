import config
from Data_Structures import tree_node as tn
from ADT import lista as lt

class bst_tree():
    def __init__(self, cmpfunction=None):
        self.root = None
        self.size = 0
        self.cmpfunction = cmpfunction
    
    def __str__(self):
        bst_str = "BST:{"
        for i in self.__entry_set():
            bst_str += str(i) + ','
        return bst_str.strip(',') + '}'

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
        return self.__remove(key)
    
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
        elif self.size == 1:
            copy_node = tn.tree_node(self.root.key, self.root.value)
            self.root = None
            self.size -= 1
            return copy_node
        else:
            self.size -=1
            return self.__delete_min_tree_key(self.root)
    
    def delete_max(self):
        if self.root is None:
            return None
        elif self.size == 1:
            copy_node = tn.tree_node(self.root.key, self.root.value)
            self.root = None
            self.size -= 1
            return copy_node
        else:
            self.size -= 1
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
    
    def __insert_node(self, key, value, tree):
        node = tn.tree_node(key, value)
        cmp = self.cmpfunction(key, tree.key)
        if cmp > 0:
            if tree.right is None:
                tree.right = node
                node.parent = tree
            else:
                self.__insert_node(key, value, tree.right)            
        elif cmp < 0:
            if tree.left is None:
                tree.left = node
                node.parent = tree
            else:
                self.__insert_node(key, value, tree.left)
        else:
            tree.value = value

    def __remove(self, key):
        if self.cmpfunction(key, self.root.key) == 0:
            copy_node = tn.tree_node(self.root.key, self.root.value)
            if self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None:
                self.root = self.root.right
            else:
                aux_node = self.__delete_max_tree_key(self.root.left)
                self.root.value = aux_node.value
                self.root.key = aux_node.key
            self.size -= 1
            return copy_node

        rem_node = self.__find_node(key, self.root)
        if rem_node is not None:
            rem_node_copy = tn.tree_node(rem_node.key, rem_node.value)
            parent_cmp = self.cmpfunction(rem_node.key, rem_node.parent.key)
            if parent_cmp > 0:
                if rem_node.right is None and rem_node.left is None:
                    del rem_node.parent.right
                elif rem_node.right is None and rem_node.left is not None:
                    rem_node.left.parent = rem_node.parent
                    rem_node.parent.right = rem_node.left
                elif rem_node.left is None and rem_node.right is not None:
                    rem_node.right.parent = rem_node.parent
                    rem_node.parent.right = rem_node.right
                else:
                    aux_left = rem_node.left
                    aux_node = self.__delete_min_tree_key(rem_node.left)
                    rem_node.value = aux_node.value
                    rem_node.key = aux_node.key
                    if aux_node == aux_left:
                        del rem_node.left
                    else:
                        rem_node.left = aux_left
            elif parent_cmp < 0:
                if rem_node.right is None and rem_node.left is None:
                    del rem_node.parent.left
                elif rem_node.right is None and rem_node.left is not None:
                    rem_node.left.parent = rem_node.parent
                    rem_node.parent.left = rem_node.left
                elif rem_node.left is None and rem_node.right is not None:
                    rem_node.right.parent = rem_node.parent
                    rem_node.parent.left = rem_node.right
                else:
                    aux_right = rem_node.right
                    aux_node = self.__delete_max_tree_key(rem_node.left)
                    rem_node.value = aux_node.value
                    rem_node.key = aux_node.key
                    if aux_node == aux_right:
                        del rem_node.right
                    else:
                        rem_node.right = aux_right
            self.size -= 1
            return rem_node_copy

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
        if tree.right is None:
            return tree
        return self.__max_tree_entry(tree.right)
    
    def __delete_min_tree_key(self, tree):
        if tree is None:
            return None

        if tree.left is None:
            copy_node = tn.tree_node(tree.key, tree.value)
            aux_node = tree.right
            if tree.parent is not None:
                if tree.right is None:
                    del tree.parent.left
                else:
                    new_node = self.__delete_min_tree_key(tree.right)
                    tree.key = new_node.key
                    tree.value = new_node.value
                    if new_node == aux_node:
                        del tree.right
                    else:
                        tree.right = aux_node
            else:
                self.root = self.__delete_min_tree_key(self.root.right)
                self.root.parent = None
            return copy_node
            
        return self.__delete_min_tree_key(tree.left)
    
    def __delete_max_tree_key(self, tree):
        if tree is None:
            return None

        # print(f"Tree: {tree}\n Parent: {tree.parent}")

        if tree.right is None:
            copy_node = tn.tree_node(tree.key, tree.value)
            aux_node = tree.left
            if tree.parent is not None:
                if tree.left is None:
                    del tree.parent.right
                else:
                    new_node = self.__delete_max_tree_key(tree.left)
                    tree.key = new_node.key
                    tree.value = new_node.value
                    if new_node == aux_node:
                        del tree.left
                    else:
                        tree.left = aux_node
            else:
                new_node = self.__delete_max_tree_key(self.root.left)
                new_node.parent = None
                self.root.key = new_node.key
                self.root.value = new_node.value
                if new_node == aux_node:
                    tree.left = tree.left.left
                else:
                    tree.left = aux_node
                
            return copy_node

        return self.__delete_max_tree_key(tree.right)

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
    tree = bst_tree(my_cmpfunction)
    print(tree, len(tree))
    tree.put(10,10)
    tree.put(5,5)
    tree.put(7,7)
    tree.put(3,3)
    tree.put(4,4)
    tree.put(1,1)
    tree.put(2,2)
    tree.put(8,8)
    tree.put(6,6)
    tree.put(9,9)
    tree.put(15,15)
    tree.put(13,13)
    tree.put(14,14)
    tree.put(12,12)
    tree.put(11,11)
    tree.put(17,17)
    tree.put(16,16)
    tree.put(18,18)
    print(tree, len(tree))    
