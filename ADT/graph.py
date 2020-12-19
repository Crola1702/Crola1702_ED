from Data_Structures import adj_list as adl
from Data_Structures import adj_matrix as adm

class graph():
    def __init__(self, datastructure='ADL', initial_elements=17, cmpfunction=None):
        self.num_vertex = 0
        self.num_edges = 0
        self.cmpfunction = cmpfunction
        if datastructure == 'ADM':
            self.graph = adm.adj_matrix(initial_elements, cmpfunction)
            self.type = datastructure
        elif datastructure == 'ADL':
            self.graph = adl.adj_list(initial_elements, cmpfunction)
            self.type = datastructure

    def insert_vertex(self, vertex):
        self.graph.insert_vertex(vertex)
        self.num_vertex += 1
    
    def insert_edge(self, vertex_A, vertex_B, weight):
        self.graph.insert_edge(vertex_A, vertex_B, weight)
        self.num_edges += 1
    
    def remove_vertex(self, vertex):
        pass

    def vertex_list(self):
        return self.graph.vertex_list()
    
    def edges_list(self):
        return self.graph.edges_list()
    
    def indegree(self, vertex):
        return self.graph.indegree(vertex)
    
    def outdegree(self, vertex):
        return self.graph.outdegree(vertex)
    
    def in_adjacents(self, vertex):
        return self.graph.in_adjacents(vertex)
    
    def out_adjacents(self, vertex):
        return self.graph.out_adjacents(vertex)
    
    def get_edge(self, vertex_A, vertex_B):
        return self.graph.get_edge(vertex_A, vertex_B)
    