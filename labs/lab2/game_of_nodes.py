# Kevin Wilson syx009

import csv
import matplotlib.pyplot as plt
import networkx as nx

from jon_snow_search import JonSnow
from white_walker_search import WhiteWalker

def show_graph(graph, pos, edges, title, accent_edges=None, accent_name=None, accent_color=None):
    fig = plt.figure(figsize=(20, 16))
    fig.add_subplot()
    # draw graph using pos dict to designate city positions
    nx.draw_networkx(graph, pos=pos, node_size=100, font_size=13, label=['City'])
    # add edge labels drawing to see distances
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edges,
                                 font_size=13, label_pos=0.5)
    
    if accent_edges != None:
        # accentuate path traveled with thick colored edges
        nx.draw_networkx_edges(graph, pos=pos, edgelist=accent_edges,
                           edge_color=accent_color, label=accent_name, width=2.0)
    
    plt.title(title)
    if accent_name == None:
        plt.legend(['City', 'Road'])
    else:
        plt.legend(['City', 'Road', accent_name])
    plt.show()

def main():
    pos_dict = {} # stores cities and their coords
    edge_dict = {} # stores edges and their distances
    list_edge = [] # used to create initial networkx graph
    with open('data.csv', newline='') as f:
        reader = csv.reader(f, dialect='unix')
        # if second value in csv is int, add pos dict, else add edge dict
        for row in reader:
            if str.isdigit(row[1]):
                pos_dict[row[0]] = (int(row[1]), int(row[2]))
            else:
                edge_dict[(row[0], row[1])] = float(row[2])
                list_edge.append(','.join(row))

    # create nx graph using edgelist from csv file
    G = nx.parse_edgelist(list_edge, delimiter=',', data=(('weight', float),))
    
    # show original map
    show_graph(G, pos_dict, edge_dict, 'Game of Nodes Map')
    
    js = JonSnow(G, 'Trader Town', 'The Wall', pos_dict).search()
    js_edgelist = []
    for i in range(len(js) - 1):
        js_edgelist.append((js[i], js[i + 1]))

    print(js_edgelist)
    # show path Jon Snow took
    show_graph(G, pos_dict, edge_dict, 'Jon Snow A* Search', js_edgelist,
               'Jon Snow', 'b')
    
    ww = WhiteWalker(G, pos_dict).search()     
        
    print(ww)
    # show path white walkers took
    show_graph(G, pos_dict, edge_dict, 'White Walker DFS on All Nodes', ww, 'White Walkers', 'r')

if __name__ == "__main__":
    main()
