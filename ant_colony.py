import networkx as nx
from loader import load_graph
from operator import itemgetter
from Ant import Ant
from dijkstry import dijkstry
from matplotlib import pyplot as plt

NUMBER_OF_ITERATIONS = 200
NUMBER_OF_ANTS = 100

PHEROMONE_COEFFICIENT = 5
EVAPORATION_COEFFICIENT = 0.25


def simulate_colony():

    graph = load_graph()

    begin = min(graph.nodes())
    end = max(graph.nodes())

    most_common_paths = []
    most_common_paths_counts = []
    iterations = []

    for iteration in range(NUMBER_OF_ITERATIONS):

        ants = []

        all_paths = []
        all_paths_counts = []

        # add N ants
        for ant_id in range(NUMBER_OF_ANTS):
            ant = Ant(ant_id, graph, begin, end)
            ants.append(ant)

        # let the ants start their journey
        for ant in ants:
            ant.walk_to_goal_extended()

        for ant in ants:
            if ant.alive:
                delta_pheromone = PHEROMONE_COEFFICIENT / ant.distance_walked

                if (ant.path_walked, ant.distance_walked) in all_paths:
                    all_paths_counts[all_paths.index((ant.path_walked, ant.distance_walked))] += 1
                else:
                    all_paths.append((ant.path_walked, ant.distance_walked))
                    all_paths_counts.append(1)

                for i in range(len(ant.path_walked) - 1):  # for each segment
                    node = ant.path_walked[i]
                    next_node = ant.path_walked[i + 1]

                    graph[node][next_node]['pheromone'] += delta_pheromone

        for edge in graph.edges:

            graph[edge[0]][edge[1]]['pheromone'] *= (1 - EVAPORATION_COEFFICIENT)

            # edge['pheromone'] *= (1 - PHEROMONE_COEFFICIENT)

            if graph[edge[0]][edge[1]]['pheromone'] < 0:
                graph[edge[0]][edge[1]]['pheromone'] = 0

        max_index = all_paths_counts.index(max(all_paths_counts))

        # all_paths = sorted(zip(all_paths, all_paths_counts), key=lambda k: k[1], reverse=True)

        most_common_paths.append(all_paths[max_index])
        most_common_paths_counts.append(all_paths_counts[max_index])
        iterations.append(iteration)

    determinant_ant = Ant(-1, graph, begin, end)

    determinant_ant.walk_to_goal_extended()

    final_path = determinant_ant.path_walked

    print(final_path)
    print(determinant_ant.distance_walked)

    distances = [dist for _, dist in most_common_paths]

    plt.plot(iterations, distances)
    plt.plot(iterations, most_common_paths_counts)
    plt.savefig('./figure.png')

    nx.set_node_attributes(graph, None, 'parent')
    nx.set_node_attributes(graph, False, 'visited')
    new_graph = dijkstry(graph, 0, 19)
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
    print(dijkstra_path[::-1])
    print(total_distance)


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