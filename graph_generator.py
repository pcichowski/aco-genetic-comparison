import networkx as nx
from random import randint
import math

def generate_graph(width, height, number_of_nodes):
    graph = nx.Graph()

    for i in range(number_of_nodes):
        x = randint(0, width)
        y = randint(0, height)

        graph.add_node(i, pos=(x, y))

    positions = nx.get_node_attributes(graph, 'pos')
    for i in range(number_of_nodes - 1):
        for j in range(i + 1, number_of_nodes):
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

            graph.add_edge(i, j, distance=dist, pheromone=0)

    return graph
