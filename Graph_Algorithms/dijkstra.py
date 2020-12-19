import config 
from TAD import graph as gr
from TAD import mapa as mp
from TAD import lista as lt
from TAD import stack as stk
from TAD import queue as que

class dijkstra_structure():
    def __init__(self, graph, source):
        self.graph = graph
        self.cmpfunction = cmpfunction
        self.vertex_lst = graph.vertex_list()
        self.marked = mp.mapa('PHT', self.vertex_lst.size, 0.5, graph.cmpfunction)
        self.source = source
    
    def dijkstra(self):
        adjacents = que.queue()
        self.marked.put(self.source, 0)
        adjacents_list = self.graph.out_adjacents(self.source)
        adj_iterator = lt.lt_iterator(adjacents_list)
        while adj_iterator.has_next():
            adjacents.enqueue(adj_iterator.next_element())
        adjacents.enqueue()
