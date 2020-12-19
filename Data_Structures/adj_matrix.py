import config
import math
from ADT import lista as lt
from ADT import mapa as mp

class adj_matrix():
    def __init__(self, initial_elements=17, cmpfunction=None, directed=True):
        self.edges = lt.lista('AL',cmpfunction)
        self.vertexes = mp.mapa('CHT', initial_elements, 1, cmpfunction)
        self.num_vertexes = 0
        self.num_edges = 0
        self.cmpfunction = cmpfunction
        self.directed = directed
    
    def __str__(self):
        adm_str = f'ADM: ({str(self.vertexes)}\n'
        for vertex_edges in self.edges:
            adm_str += str(vertex_edges) + '\n'
        return adm_str.strip('\n') + ' )'

    #_______________________________
    #              API
    #_______________________________

    def insert_vertex(self, vertex):
        self.num_vertexes += 1
        self.vertexes.put(vertex, self.num_vertexes)
        edges_lst = lt.lista('AL', self.cmpfunction)
        for i in range(self.num_vertexes):
            edges_lst.add_last(math.inf)
        for vertex_edges in self.edges:
            vertex_edges.add_last(math.inf)
        self.edges.add_last(edges_lst)
    
    def insert_edge(self, vertex_A, vertex_B, weight):
        vertex_A_index = self.vertexes.get(vertex_A).value
        vertex_B_index = self.vertexes.get(vertex_B).value
        self.edges.get_element(vertex_A_index).replace(vertex_B_index, weight)
        self.num_edges += 1
        if not self.directed:
            self.edges.get_element(vertex_B_index).replace(vertex_A_index, weight)
    
    def get_edge(self, vertex_A, vertex_B):
        vertex_A_index = self.vertexes.get(vertex_A).value
        vertex_B_index = self.vertexes.get(vertex_B).value
        weight = self.edges.get_element(vertex_A_index).get_element(vertex_B_index)
        return {'vertex_A': vertex_A, 'vertex_B': vertex_B, 'weight': weight}

    def remove_vertex(self, vertex):
        vertex_index = self.vertexes.get(vertex).value
        self.vertexes.remove(vertex)
        for vertex in self.vertexes:
            entry = self.vertexes.get(vertex)
            if entry.value > vertex_index:
                entry.value -= 1
        
        for vertex_edges in self.edges:
            if vertex_edges.remove_pos(vertex_index) != math.inf:
                self.num_edges -= 1
        
        vertex_edge = self.edges.remove_pos(vertex_index)
        for edge in vertex_edge:
            if edge != math.inf:
                self.num_edges -= 1

        self.num_vertexes -= 1
        return vertex_edge
    
    def outdegree(self, vertex):
        vertex_index = self.vertexes.get(vertex).value
        outdegree = 0
        for edge in self.edges.get_element(vertex_index):
            if edge != math.inf:
                outdegree += 1
        return outdegree

    def indegree(self, vertex):
        vertex_index = self.vertexes.index(vertex)
        indegree = 0
        for vertex_edges in self.edges:
            if vertex_edges.get_element(vertex_index) != math.inf:
                indegree += 1
        return indegree

    def out_adjacents(self, vertex):
        vertex_index = self.vertexes.get(vertex).value
        out_adjacents_list = lt.lista('SL',self.cmpfunction)
        current_index = 1
        for edge in self.edges.get_element(vertex_index):
            if edge != math.inf:
                out_adjacents_list.add_last(self.__find_vertex(current_index))
            current_index += 1
        return out_adjacents_list
    
    def in_adjacents(self, vertex):
        vertex_index = self.vertexes.get(vertex).value
        in_adjacents_list = lt.lista('SL',self.cmpfunction)
        current_index = 1
        for vertex_edges in self.edges:
            if vertex_edges.get_element(vertex_index) != math.inf:
                in_adjacents_list.add_last(self.__find_vertex(current_index))
            current_index += 1
        return in_adjacents_list

    def vertex_list(self):
        return self.vertexes.key_set()
        # return self.vertexes.entry_set()
    
    def edges_list (self):
        edges_list = lt.lista('SL', self.cmpfunction)
        edges_iterator_1 = lt.lt_iterator(self.edges)
        vertex_A_index = 1                   
        for vertex_edges in self.edges:
            vertex_B_index = 1
            for edge in vertex_edges:
                if edge != math.inf:
                    edges_list.add_last({'vertex_A': self.__find_vertex(vertex_A_index),
                                         'vertex_B': self.__find_vertex(vertex_B_index),
                                         'weight': edge})       
                vertex_B_index += 1
            vertex_A_index += 1
        return edges_list    

    def is_empty(self):
        return self.num_vertexes == 0

    #_______________________________
    #       Funciones de apoyo
    #_______________________________

    def __find_vertex(self, vertex_index):
        for entry in self.vertexes:
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
    print(a)


    
