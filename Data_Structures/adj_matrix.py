import config
import math
from ADT import lista as lt
from ADT import mapa as mp

class adj_matrix():
    def __init__(self, initial_elements=17, cmpfunction=None):
        self.edges = lt.lista('AL',cmpfunction)
        self.vertexes = mp.mapa('CHT', initial_elements, 1, cmpfunction)
        self.num_vertexes = 0
        self.num_edges = 0
        self.cmpfunction = cmpfunction
    
    #_______________________________
    #              API
    #_______________________________

    def insert_vertex(self, vertex):
        self.num_vertexes += 1
        self.vertexes.put(vertex, self.num_vertexes)
        edges_lst = lt.lista('AL', self.cmpfunction)
        edges_iterator = lt.lt_iterator(self.edges)
        while edges_iterator.has_next():
            edges_iterator.next_element().add_last(math.inf)

        for i in range(self.num_vertexes):
            edges_lst.add_last(math.inf)

        self.edges.add_last(edges_lst)
    
    def insert_edge(self, vertex_A, vertex_B, weight):
        vertex_A_index = self.vertexes.get(vertex_A).value
        vertex_B_index = self.vertexes.get(vertex_B).value
        self.edges.get_element(vertex_A_index).replace(vertex_B_index, weight)
        self.num_edges += 1
    
    def get_edge(self, vertex_A, vertex_B):
        vertex_A_index = self.vertexes.get(vertex_A).value
        vertex_B_index = self.vertexes.get(vertex_B).value
        weight = self.edges.get_element(vertex_A_index).get_element(vertex_B_index)
        return {'vertex_A': vertex_A, 'vertex_B': vertex_B, 'weight': weight}

    def remove_vertex(self, vertex):
        vertex_index = self.vertexes.get(vertex).value
        self.vertexes.remove(vertex)
        entry_iterator = lt.lt_iterator(self.vertexes.entry_set())
        while entry_iterator.has_next():
            entry = entry_iterator.next_element()
            if entry.value > vertex_index:
                self.vertexes.put(entry.key, entry.value-1)

        edge_iterator = lt.lt_iterator(self.edges)
        while edge_iterator.has_next():
            edge = edge_iterator.next_element()
            if edge.remove_pos(vertex_index) != math.inf:
                self.num_edges -= 1
        
        vertex_edge = self.edges.remove_pos(vertex_index)
        vertex_edge_iterator = lt.lt_iterator(vertex_edge)
        while vertex_edge_iterator.has_next():
            if vertex_edge_iterator.next_element() != math.inf:
                self.num_edges -= 1

        self.num_vertexes -= 1
        return vertex_edge
    
    def outdegree(self, vertex):
        vertex_index = self.vertexes.get(vertex).value
        edge_iterator = lt.lt_iterator(self.edges.get_element(vertex_index))
        outdegree = 0
        while edge_iterator.has_next():
            edge = edge_iterator.next_element()
            if edge != math.inf:
                outdegree += 1
        return outdegree

    def indegree(self, vertex):
        vertex_index = self.vertexes.index(vertex)
        edge_iterator = lt.lt_iterator(self.edges)
        indegree = 0
        while edge_iterator.has_next():
            edge = edge_iterator.next_element()
            if edge.get_element(vertex_index) != math.inf:
                indegree += 1
        return indegree

    def out_adjacents(self, vertex):
        vertex_index = self.vertexes.get(vertex).value
        edge_iterator = lt.lt_iterator(self.edges.get_element(vertex_index))
        out_adjacents_list = lt.lista('AL',self.cmpfunction)
        current_index = 1
        while edge_iterator.has_next():
            out_edge = edge_iterator.next_element()
            if out_edge != math.inf:
                out_adjacents_list.add_last(self.find_vertex(current_index))
            current_index += 1
        return out_adjacents_list
    
    def in_adjacents(self, vertex):
        vertex_index = self.vertexes.get(vertex).value
        edge_iterator = lt.lt_iterator(self.edges)
        in_adjacents_list = lt.lista('AL',self.cmpfunction)
        current_index = 1
        while edge_iterator.has_next():
            in_edge = edge_iterator.next_element().get_element(vertex_index)
            if in_edge != math.inf:
                in_adjacents_list.add_last(self.find_vertex(current_index))
            current_index += 1
        return in_adjacents_list

    def vertex_list(self):
        return self.vertexes.key_set()
        # return self.vertexes.entry_set()
    
    def edges_list (self):
        edges_list = lt.lista('SL', self.cmpfunction)
        edges_iterator_1 = lt.lt_iterator(self.edges)
        vertex_A_index = 1                              
        while edges_iterator_1.has_next():
            vertex_B_index = 1
            edges_iterator_2 = lt.lt_iterator(edges_iterator_1.next_element())
            while edges_iterator_2.has_next():
                edge = edges_iterator_2.next_element()
                if edge != math.inf:
                    edges_list.add_last({'vertex_A': self.find_vertex(vertex_A_index),
                                         'vertex_B': self.find_vertex(vertex_B_index),
                                         'weight': edge})
                vertex_B_index += 1
            vertex_A_index += 1
        return edges_list

    def is_empty(self):
        if self.num_vertexes == 0:
            return True
        return False

    #_______________________________
    #       Funciones de apoyo
    #_______________________________

    def find_vertex(self, vertex_index):
        vertex_iterator = lt.lt_iterator(self.vertexes.entry_set())
        while vertex_iterator.has_next():
            entry = vertex_iterator.next_element()
            if entry.value == vertex_index:
                return entry.key
        return None

def my_cmpfunction(el1, el2):
    if el1 > el2:
        return 1
    elif el1 < el2:
        return -1
    return 0

if __name__ == '__main__':
    a = adj_matrix(cmpfunction=my_cmpfunction)
    a.insert_vertex('A')
    a.insert_vertex('B')
    a.insert_vertex('C')
    a.insert_vertex('D')
    a.insert_edge('A','B',1)
    a.insert_edge('A','C',1)
    a.insert_edge('B','C',1)
    a.remove_vertex('A')


    v_it = lt.lt_iterator(a.vertex_list())
    while v_it.has_next():
        entry = v_it.next_element()
        print(entry)

    it = lt.lt_iterator(a.edges_list())
    while it.has_next():
        print(it.next_element())
    
