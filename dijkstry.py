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

    reach_cost = {snode: 0}

    while len(options) > 0:

        tuple = heappop(options)
        node = tuple[2]
        G.nodes[node]['visited'] = True

        children = G.neighbors(node)
        for child in children:

            cost = reach_cost[node] + G[node][child]['distance']

            if child == enode:
                G.nodes[child]['parent'] = node
                return path_from(G, child)

            if child not in reach_cost or cost < reach_cost[child]:
                reach_cost[child] = cost
            # if not G.nodes[child]['visited']:
                G.nodes[child]['parent'] = node
                new_tuple = (tuple[0] + 1, i, child)
                i += 1
                heappush(options, new_tuple)


# Wykonanie
def execute_dijkstra(graph, begin, end):
    # nx.draw(graph)
    # plt.show()
    nx.set_node_attributes(graph, None, 'parent')
    nx.set_node_attributes(graph, False, 'visited')
    new_graph = dijkstry(graph, begin, end)

    dijkstra_path = []
    for node in new_graph.nodes:
        # print(node, end=' ')
        dijkstra_path.append(node)
    total_distance = 0
    for i in range(len(dijkstra_path) - 1):  # for each segment
        node = dijkstra_path[i]
        next_node = dijkstra_path[i + 1]

        distance = graph[node][next_node]['distance']
        total_distance += distance


    return dijkstra_path[::-1], total_distance
