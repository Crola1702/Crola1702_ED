import config
from ADT import lista as lt
from ADT import mapa as mp
from ADT import ordered_map as om

class adj_list():
    def __init__(self, initial_elements=17, cmpfunction=None):
        self.vertexes = mp.mapa('CHT', initial_elements, 1, cmpfunction)
        self.num_vertexes = 0
        self.num_edges = 0
        self.cmpfunction = cmpfunction
    
    #_______________________________
    #              API
    #_______________________________

    def insert_vertex(self, vertex):
        self.vertexes.put(vertex, om.ordered_map(cmpfunction=self.cmpfunction))
        self.num_vertexes += 1

    def insert_edge(self, vertex_A, vertex_B, weight):
        entry = self.vertexes.get(vertex_A)
        entry.value.put(vertex_B, weight)
        self.num_edges += 1
    
    def get_edge(self, vertex_A, vertex_B):
        if self.vertexes.get(vertex_A) is not None:
            if self.vertexes.get(vertex_A).value.get(vertex_B) is not None:
                weight = self.vertexes.get(vertex_A).value.get(vertex_B).value
                return {'vertex_A': vertex_A, 'vertex_B': vertex_B, 'weight': weight}
        return None

    def remove_vertex(self, vertex):
        pass

    def vertex_list(self):
        return self.vertexes.key_set()
    
    def edges_list(self):
        edges_list = lt.lista(cmpfunction=self.cmpfunction)
        vertex_iterator = lt.lt_iterator(self.vertexes.key_set())
        while vertex_iterator.has_next():
            vertex_entry = self.vertexes.get(vertex_iterator.next_element())
            edges_iterator = lt.lt_iterator(vertex_entry.value.key_set())
            while edges_iterator.has_next():
                adjacent_entry = vertex_entry.value.get(edges_iterator.next_element())
                edges_list.add_last({'vertex_A': vertex_entry.key, 'vertex_B': adjacent_entry.key, 'weight': adjacent_entry.value})
        return edges_list
    
    def outdegree(self, vertex):
        vertex_adjacents = self.vertexes.get(vertex)
        if vertex_adjacents is not None:
            return vertex_adjacents.value.size
        return 0
    
    def indegree(self, vertex):
        indegree = 0
        vertex_iterator = lt.lt_iterator(self.vertexes.key_set())
        while vertex_iterator.has_next():
            edges_iterator = lt.lt_iterator(self.vertexes.get(vertex_iterator.next_element()).value.key_set())
            while edges_iterator.has_next():
                if self.cmpfunction(edges_iterator.next_element(), vertex) == 0:
                    indegree += 1
        return indegree

    def out_adjacents(self, vertex):
        vertex_adjacents = self.vertexes.get(vertex)
        if vertex_adjacents is not None:
            return vertex_adjacents.value.key_set()
        
    def in_adjacents(self, vertex):
        in_adjacents_list = lt.lista(cmpfunction=self.cmpfunction)
        vertex_iterator = lt.lt_iterator(self.vertexes.key_set())
        while vertex_iterator.has_next():
            edges_iterator = lt.lt_iterator(self.vertexes.get(vertex_iterator.next_element()).value.key_set())
            while edges_iterator.has_next():
                edge = edges_iterator.next_element()
                if self.cmpfunction(edge, vertex) == 0:
                    in_adjacents_list.add_last(edge)
        return in_adjacents_list
    
    def is_empty(self):
        if self.num_vertexes == 0:
            return True
        return False


def my_cmpfunction(el1, el2):
    if el1 > el2:
        return 1
    elif el1 < el2:
        return -1
    return 0

if __name__ == '__main__':
    a = adj_list(cmpfunction=my_cmpfunction)
    a.insert_vertex('A')
    a.insert_vertex('B')
    a.insert_vertex('C')
    a.insert_vertex('D')
    a.insert_edge('A','B',1)
    a.insert_edge('A','C',1)
    a.insert_edge('B','C',1)

    v_it = lt.lt_iterator(a.vertex_list())
    while v_it.has_next():
        entry = v_it.next_element()
        print(entry)

    it = lt.lt_iterator(a.edges_list())
    while it.has_next():
        print(it.next_element())
