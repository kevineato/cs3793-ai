# Kevin Wilson syx009

import networkx as nx

class WhiteWalker:
    def __init__(self, graph, pos):
        self.graph = graph
        self.pos = pos
        
    # depth first search on all cities such that every city is visited
    def search(self):
        path = list(nx.algorithms.traversal.dfs_edges(self.graph, 'The Wall'))
        return path     