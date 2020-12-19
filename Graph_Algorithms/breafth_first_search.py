import config
from TAD import graph as gr
from TAD import queue as que
from TAD import stack as stk
from TAD import mapa as mp
from TAD import lista as lt

class bfs_structure():
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.cmpfunction = graph.cmpfunction

    def bfs(self, destination=None):
        self.queue = que.queue()
        self.visited = mp.mapa(cmpfunction=self.graph.cmpfunction)
        self.destination = destination
        self.visited.put(self.source, {'edge_to': None, 'weight':0})
        self.queue.enqueue(self.source)
        while not self.queue.is_empty():
            vertex = self.queue.dequeue()
            vertex_adjacents = lt.lt_iterator(self.graph.out_adjacents(vertex))
            while vertex_adjacents.has_next():
                new_vertex = vertex_adjacents.next_element()
                if not self.visited.contains(new_vertex):
                    self.visited.put(new_vertex, {'edge_to': vertex, 'weight': self.graph.get_edge(vertex, new_vertex)['weight']})
                    if self.destination is not None:
                        if self.cmpfunction(new_vertex, self.destination) == 0:
                            return self.path_to(self.destination)
                    self.queue.enqueue(new_vertex)
    
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
