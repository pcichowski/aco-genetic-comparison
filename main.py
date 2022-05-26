import time

from graph_generator import generate_graph
import networkx as nx
from networkx.algorithms.approximation import traveling_salesman_problem
from matplotlib import pyplot as plt
from run_genetic import genetic
from ant_colony import AntColony
from ant import Ant


from utils import calculate_total_distance
from utils_genetic import plot_route, get_coords, plot_improvement

NUMBER_OF_NODES = 25
NUMBER_OF_TESTS = 1


def perform_test():
    graph = generate_graph(1000, 1000, 25)

    results = {'time': {}, 'distance': {}, 'path': {}, 'steps': {}}

    # optimal approximation algorithm
    time_start = time.time()
    results['path']['christofides'] = traveling_salesman_problem(graph, weight='distance')
    time_end = time.time()
    results['time']['christofides'] = time_end - time_start  # in seconds
    results['distance']['christofides'] = calculate_total_distance(graph, results['path']['christofides'])

    # genetic algorithm
    time_start = time.time()
    results['path']['genetic'], results['steps']['genetic'] = genetic(graph)
    time_end = time.time()
    results['time']['genetic'] = time_end - time_start  # in seconds
    results['distance']['genetic'] = calculate_total_distance(graph, results['path']['genetic'])


    # ant colony optimization algorithm
    colony = AntColony(graph, 20, 30)
    time_start = time.time()
    results['path']['ants'], results['distance']['ants'], results['steps']['ants'] = colony.simulate(2, 1, 0, 1)
    time_end = time.time()
    results['time']['ants'] = time_end - time_start  # in seconds

    create_plots(graph, results)

def create_plots(graph, results):
    fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(10, 5))
    plot_improvement(ax[0][0], graph, results['steps']['ants'])
    plot_route(ax[1][0], graph, results['path']['ants'])

    plot_improvement(ax[1][0], graph, results['steps']['genetic'])
    plot_route(ax[1][1], graph, results['path']['genetic'])
    plt.show()



def run():

    for _ in range(NUMBER_OF_TESTS):
        perform_test()

    # poss = nx.get_node_attributes(graph, 'pos')
    # print(poss)
    #
    # fig, ax = plt.subplots(ncols=2, figsize=(10, 5))
    # nodes_positions = get_coords(graph)
    # plot_route(ax[1], graph, list(graph.nodes.keys()))
    #
    # # nx.draw(g, poss)
    #
    # plt.show()

run()

# colony = AntColony(g, 20, 30)
# path, cost = colony.simulate(2, 1, 0, 1)
# print(path)
# print(cost)
