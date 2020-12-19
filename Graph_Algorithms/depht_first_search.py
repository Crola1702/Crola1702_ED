import config
from TAD import graph as gr
from TAD import mapa as mp
from TAD import stack as stk
from TAD import lista as lt

class dfs_structure():
    def __init__(self, graph, source):
        self.graph = graph
        self.cmpfunction = graph.cmpfunction
        self.source = source
    
    def dfs(self, destination=None):
        self.visited = mp.mapa(cmpfunction=self.graph.cmpfunction)
        self.destination = destination
        self.dfs_vertex(self.source, None)
        

    def dfs_vertex(self, vertex, edge_to):
        if not self.visited.contains(vertex):
            if edge_to is None:
                self.visited.put(vertex, {'edge_to': edge_to, 'weight': None})
            else:
                self.visited.put(vertex, {'edge_to': edge_to, 'weight': self.graph.get_edge(edge_to, vertex)['weight']})
            if self.destination is not None:
                if self.cmpfunction(vertex, self.destination) == 0:
                    return None
            adj_iterator = lt.lt_iterator(self.graph.out_adjacents(vertex))
            while adj_iterator.has_next():
                next_vertex = adj_iterator.next_element()
                self.dfs_vertex(next_vertex, vertex)
            return None
    
    def path_to(self, vertex):
        vertex_entry = self.visited.get(vertex)
        vertex_order = stk.stack()
        if vertex_entry is not None:
            while vertex_entry.value['edge_to'] is not None:
                vertex_order.push({'vertex': vertex_entry.key, 'weight': vertex_entry.value['weight']})
                vertex_entry = self.visited.get(vertex_entry.value['edge_to'])
        return vertex_order
    
    def has_path_to(self, vertex):
        if self.visited.get(vertex) is not None:
            return True
        return False

            

