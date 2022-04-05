import csv

import networkx as nx
from matplotlib import pyplot as plt

def load_graph():
    graph = nx.Graph()
    with open('./graph_input.csv', encoding='utf-8') as file_graph_input:
        csv_reader = csv.reader(file_graph_input, delimiter=' ')

        for row in csv_reader:
            initial_node = row[0]

            for node in row[1:]:
                graph.add_edge(initial_node, node)

    return graph

G = load_graph()
for node in nx.nodes(G):
    ns = G.neighbors(node)
    print(f"{node}: ", end='')
    for n in ns:
        print(n, end=' ')

    print("")