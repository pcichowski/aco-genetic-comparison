import math
import time
from concurrent.futures import ThreadPoolExecutor

from graph_generator import generate_graph
from networkx.algorithms.approximation import traveling_salesman_problem
from matplotlib import pyplot as plt
from run_genetic import genetic
from ant_colony import AntColony
from ant import Ant
from test_coeficients import *

from statistics import mean, variance

from utils import calculate_total_distance
from utils_genetic import plot_route, plot_improvement

NUMBER_OF_NODES = 10
NUMBER_OF_TESTS = 10


def perform_test(show_graphs=True):
    graph = generate_graph(1000, 1000, NUMBER_OF_NODES)

    results = {'time': {}, 'distance': {}, 'path': {}, 'steps': {}}

    # optimal approximation algorithm
    time_start = time.time()
    results['path']['christofides'] = traveling_salesman_problem(graph, weight='distance')
    time_end = time.time()
    results['time']['christofides'] = time_end - time_start  # in seconds
    results['distance']['christofides'] = calculate_total_distance(graph, results['path']['christofides'])

    # genetic algorithm
    time_start = time.time()
    results['path']['genetic'], results['steps']['genetic'] = genetic(graph, generations=100, population_size=97,
                                                                      elite_size=18, mutation_rate=0.01)
    time_end = time.time()
    results['time']['genetic'] = time_end - time_start  # in seconds
    results['distance']['genetic'] = calculate_total_distance(graph, results['path']['genetic'])

    # ant colony optimization algorithm
    colony = AntColony(graph, 20, 30)
    time_start = time.time()
    results['path']['ants'], results['distance']['ants'], results['steps']['ants'] = colony.simulate(1.2, 1.2, 0.4, 1.5)
    time_end = time.time()
    results['time']['ants'] = time_end - time_start  # in seconds

    if show_graphs:
        create_plots(graph, results)

    return results


def create_plots(graph, results):
    fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(10, 5))
    plot_improvement(ax[0][0], graph, results['steps']['ants'])
    plot_route(ax[0][1], graph, results['path']['ants'])
    ax[0][0].set_title('Ant colony optimization algorithm')

    plot_improvement(ax[1][0], graph, results['steps']['genetic'])
    plot_route(ax[1][1], graph, results['path']['genetic'])
    ax[1][0].set_title('Genetic algorithm')

    fig.tight_layout()
    plt.show()


def run():
    # test_coefficients_genetic(25, (100, 400), 50, (40, 120), 10, (8, 20), 2, (0, 0.04), 0.002)

    results = {'times': {'ants': [], 'genetic': []}, 'distances': {'ants': [], 'genetic': []}}

    for _ in range(NUMBER_OF_TESTS):
        test_results = perform_test(show_graphs=False)

        results['times']['ants'].append(test_results['time']['ants'])
        results['times']['genetic'].append(test_results['time']['genetic'])

        results['distances']['ants'].append(test_results['distance']['ants'])
        results['distances']['genetic'].append(test_results['distance']['genetic'])

    mean_time_ants = mean(results['times']['ants'])
    mean_time_genetic = mean(results['times']['genetic'])
    mean_distance_ants = mean(results['distances']['ants'])
    mean_distance_genetic = mean(results['distances']['genetic'])

    std_time_ants = math.sqrt(variance(results['times']['ants']))
    std_time_genetic = math.sqrt(variance(results['times']['genetic']))
    std_distance_ants = math.sqrt(variance(results['distances']['ants']))
    std_distance_genetic = math.sqrt(variance(results['distances']['genetic']))

    fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(10, 5))
    ax[0][0].plot(range(1, NUMBER_OF_TESTS + 1), results['times']['ants'])
    ax[0][1].plot(range(1, NUMBER_OF_TESTS + 1), results['times']['genetic'])

    ax[1][0].plot(range(1, NUMBER_OF_TESTS + 1), results['distances']['ants'])
    ax[1][1].plot(range(1, NUMBER_OF_TESTS + 1), results['distances']['genetic'])

    ax[0][0].plot(range(1, NUMBER_OF_TESTS + 1), [mean_time_ants for _ in range(1, NUMBER_OF_TESTS + 1)])
    ax[0][1].plot(range(1, NUMBER_OF_TESTS + 1), [mean_time_genetic for _ in range(1, NUMBER_OF_TESTS + 1)])
    ax[1][0].plot(range(1, NUMBER_OF_TESTS + 1), [mean_distance_ants for _ in range(1, NUMBER_OF_TESTS + 1)])
    ax[1][1].plot(range(1, NUMBER_OF_TESTS + 1), [mean_distance_genetic for _ in range(1, NUMBER_OF_TESTS + 1)])

    ax[0][0].set_xlabel('Test number')
    ax[0][1].set_xlabel('Test number')
    ax[1][0].set_xlabel('Test number')
    ax[1][1].set_xlabel('Test number')
    ax[0][0].set_ylabel('Time [s]')
    ax[0][1].set_ylabel('Time [s]')
    ax[1][0].set_ylabel('Distance')
    ax[1][1].set_ylabel('Distance')

    ax[0][0].set_title('ACO algorithm')
    ax[0][1].set_title('Genetic algorithm')
    fig.tight_layout()
    fig.show()

    print(f"Average distance for ACO: {mean_distance_ants:.2f}")
    print(f"Average time for ACO: {mean_time_ants:.2f}")
    print(f"Average distance for genetic: {mean_distance_genetic:.2f}")
    print(f"Average time for genetic: {mean_time_genetic:.2f}")

    print(f"Standard deviation distance for ACO: {std_distance_ants:.2f}")
    print(f"Standard deviation time for ACO: {std_time_ants:.2f}")
    print(f"Standard deviation distance for genetic: {std_distance_genetic:.2f}")
    print(f"Standard deviation time for genetic: {std_time_genetic:.2f}")


run()