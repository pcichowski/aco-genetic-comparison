from heapq import heapify, heappop, heappush
import networkx as nx
import copy
from loader import load_graph
from matplotlib import pyplot as plt


def path_from(G, node):
    graph = nx.Graph()
    graph.add_node(node)

    while G.nodes[node]['parent'] is not None:
        parent = G.nodes[node]['parent']
        graph.add_node(parent, parent=G.nodes[parent]['parent'], visited=False)
        graph.add_edge(parent, node)
        node = parent

    return graph


def dijkstry(G, snode, enode):
    start_tuple = (0, 0, snode)
    options = [start_tuple]
    heapify(options)
    i = 1

    while len(options) > 0:

        tuple = heappop(options)
        node = tuple[2]
        G.nodes[node]['visited'] = True

        children = G.neighbors(node)
        for child in children:

            if child == enode:
                G.nodes[child]['parent'] = node
                return path_from(G, child)

            if not G.nodes[child]['visited']:
                G.nodes[child]['parent'] = node
                new_tuple = (tuple[0] + 1, i, child)
                i += 1
                heappush(options, new_tuple)


# Wykonanie
graph = load_graph()
nx.set_node_attributes(graph, None, 'parent')
nx.set_node_attributes(graph, False, 'visited')
new_graph = dijkstry(graph, 0, 15)

for node in new_graph.nodes:
    print(node)

nx.draw(new_graph)
plt.show()
