# Kevin Wilson syx009

import networkx as nx

class JonSnow:
    def __init__(self, graph, source, dest, pos):
        self.graph = graph
        self.source = source
        self.dest = dest
        self.pos = pos
        
    def search(self):
        # heuristic straight line distance func used for A*
        def sl_dist(n1, n2):
            (x1, y1) = self.pos[n1]
            (x2, y2) = self.pos[n2]
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        
        return nx.algorithms.astar_path(self.graph, self.source, self.dest,
                                        heuristic=sl_dist)