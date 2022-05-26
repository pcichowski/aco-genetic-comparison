from loader import load_graph
from dijkstry import execute_dijkstra
from ant_colony import simulate_colony
import networkx as nx
from random import randint
from statistics import mean, stdev
from matplotlib import pyplot as plt
import time

NUMBER_OF_NODES = 1000
NUMBER_OF_TESTS = 1

results = {"shortest": [], "dijkstra": [], "ants": []}


def calculate(print_console=False):
    # graph = load_graph()
    graph = nx.gnp_random_graph(NUMBER_OF_NODES, 0.05)

    nx.set_node_attributes(graph, None, 'parent')
    nx.set_node_attributes(graph, False, 'visited')
    nx.set_edge_attributes(graph, 0, 'pheromone')
    for edge in graph.edges:
        graph[edge[0]][edge[1]]['distance'] = randint(1, 100)

    begin = randint(0, NUMBER_OF_NODES - 1)
    end = randint(0, NUMBER_OF_NODES - 1)

    if not nx.has_path(graph, begin, end):
        return

    shortest_path = nx.shortest_path(graph, source=begin, target=end, weight='distance')
    shortest_distance = 0
    for i in range(len(shortest_path) - 1):  # for each segment
        node = shortest_path[i]
        next_node = shortest_path[i + 1]

        distance = graph[node][next_node]['distance']
        shortest_distance += distance

    if print_console: print(f"shortest: {shortest_path}\n{shortest_distance}")

    time_start = time.time()
    dijkstra_path, dijkstra_dist = execute_dijkstra(graph, begin, end)
    time_end = time.time()
    results['dijkstra_time'] = time_end - time_start

    if print_console: print(f"Dijkstra: {dijkstra_path}\n{dijkstra_dist}")

    time_start = time.time()
    ant_path, ant_dist = simulate_colony(graph, begin, end)
    time_end = time.time()
    results['ants_time'] = time_end - time_start

    if print_console: print(f"Ants: {ant_path}\n{ant_dist}")

    results['shortest'].append(shortest_distance)
    results['dijkstra'].append(dijkstra_dist)
    results['ants'].append(ant_dist)


def main():
    for _ in range(NUMBER_OF_TESTS):
        calculate()

    deviation_ants = []
    deviation_dijkstra = []
    for result_opt, result_dijkstra in zip(results['shortest'], results['dijkstra']):
        deviation_dijkstra.append(round((result_dijkstra - result_opt) / result_dijkstra * 100, 2))

    for result_opt, result_ants in zip(results['shortest'], results['ants']):
        deviation_ants.append(round((result_ants - result_opt) / result_ants * 100, 2))

    print(f"mean deviation of ants: {mean(deviation_ants)}%   time: {results['ants_time']}")
    print(f"mean deviation of dijkstra: {mean(deviation_dijkstra)}%   time: {results['dijkstra_time']}")

    fig, axs = plt.subplots(2, 1, figsize=(8, 10))
    ax = axs[0]
    ax.plot([i for i in range(1, len(results['shortest']) + 1)], results['shortest'], label='optimal')
    ax.plot([i for i in range(1, len(results['shortest']) + 1)], results['ants'], label='ants')
    ax.plot([i for i in range(1, len(results['shortest']) + 1)], results['dijkstra'], label='dijkstra')
    ax.set_title('Comparison of algorithms')
    ax.set_xlabel('Test number')
    ax.set_ylabel('Found path length')
    ax.legend()
    ax.grid(True)
    plt.savefig('./comparison.png')

main()
