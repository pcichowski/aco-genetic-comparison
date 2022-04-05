import networkx as nx
from loader import load_graph
from operator import itemgetter

alpha = 0.5
beta = 1.2

NUMBER_OF_STEPS = 200


# args
# node - node from which the ant want to moves
def generate_solutions(graph, node):
    sum = 0
    for neighbor in graph.neighbors(node):
        pheromone = graph[node][neighbor]['pheromone']
        distance = graph[node][neighbor]['distance']
        sum += pheromone ** alpha * distance ** beta

    possible_solutions = []

    for neighbor in graph.neighbors(node):
        pheromone = graph[node][neighbor]['pheromone']
        distance = graph[node][neighbor]['distance']
        probability = pheromone ** alpha * distance ** beta / sum

        possible_solutions.append((neighbor, probability))

    return possible_solutions


def ant_colony_algorithm(graph, begin, end):  # for each ant
    graph = load_graph()

    nx.set_edge_attributes(graph, 0, 'pheromone')
    nx.set_edge_attributes(graph, 0, 'probability')

    ants = []

    current_node = begin

    while running:
        solutions = generate_solutions(graph, current_node)

        best_solution = max(solutions, lambda i: i[1])[0]

