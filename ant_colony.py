import networkx as nx
from loader import load_graph
from operator import itemgetter
from Ant import Ant


NUMBER_OF_ITERATIONS = 200
NUMBER_OF_ANTS = 10

PHEROMONE_COEFFICIENT = 3
EVAPORATION_COEFFICIENT = 0.2


def simulate_colony():

    graph = load_graph()

    begin = min(graph.nodes())
    end = max(graph.nodes())

    for _ in range(NUMBER_OF_ITERATIONS):

        ants = []

        # add N ants
        for ant_id in range(NUMBER_OF_ANTS):
            ant = Ant(ant_id, graph, begin, end)
            ants.append(ant)

        # let the ants start their journey
        for ant in ants:
            ant.walk_to_goal()

        for ant in ants:
            delta_pheromone = PHEROMONE_COEFFICIENT / ant.distance_walked

            for i in range(len(ant.path_walked) - 1):  # for each segment
                node = ant.path_walked[i]
                next_node = ant.path_walked[i + 1]

                graph[node][next_node]['pheromone'] += delta_pheromone

        for edge in graph.edges:

            graph[edge[0]][edge[1]]['pheromone'] *= (1 - PHEROMONE_COEFFICIENT)

            # edge['pheromone'] *= (1 - PHEROMONE_COEFFICIENT)

            if graph[edge[0]][edge[1]]['pheromone'] < 0:
                graph[edge[0]][edge[1]]['pheromone'] = 0

    determinant_ant = Ant(-1, graph, begin, end)

    determinant_ant.walk_to_goal()

    final_path = determinant_ant.path_walked

    print(final_path)


def ant_colony_algorithm(graph, begin, end):  # for each ant
    graph = load_graph()

    nx.set_edge_attributes(graph, 0, 'pheromone')
    nx.set_edge_attributes(graph, 0, 'probability')

    ants = []

    current_node = begin

    while running:
        solutions = generate_solutions(graph, current_node)

        best_solution = max(solutions, lambda i: i[1])[0]


simulate_colony()