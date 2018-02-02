# Kevin Wilson syx009

import csv
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

def main():
    dic_pos = {}
    dic_edge = {}
    list_edge = []
    with open('data.csv', newline='') as f:
        reader = csv.reader(f, dialect='unix')
        lnum = 1
        for row in reader:
            if lnum <= 56:
                dic_pos[row[0]] = (int(row[1]), int(row[2]))
            else:
                dic_edge[(row[0], row[1])] = float(row[2])
                list_edge.append(','.join(row))
            lnum += 1

    G = nx.parse_edgelist(list_edge, delimiter=',', data=(('weight', float),))
    fig = plt.figure(figsize=(12, 10))
    fig.add_subplot()
    nx.draw_networkx(G, pos=dic_pos, node_size=100, font_size=10)
    nx.draw_networkx_edge_labels(G, pos=dic_pos, edge_labels=dic_edge, font_size=10, label_pos=0.5)
    plt.show()

if __name__ == "__main__":
    main()
