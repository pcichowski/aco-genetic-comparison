import networkx as nx
from loader import load_graph
from operator import itemgetter
from Ant import Ant
from dijkstry import dijkstry
from matplotlib import pyplot as plt

NUMBER_OF_ITERATIONS = 50
NUMBER_OF_ANTS = 200

PHEROMONE_COEFFICIENT = 2
EVAPORATION_COEFFICIENT = 0.4


def simulate_colony(graph, begin, end):

    most_common_paths = [[], [], [], []]
    most_common_paths_counts = [[], [], []]
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

        all_paths_counts_sorted = sorted(all_paths_counts, reverse=True)

        min_path = sorted(all_paths, key=lambda k: k[1])[0]

        for i, top_path_count in enumerate(all_paths_counts_sorted[:3]):
            most_common_paths[i].append(all_paths[all_paths_counts.index(top_path_count)])
            most_common_paths_counts[i].append(all_paths_counts[all_paths_counts.index(top_path_count)])

        if len(all_paths_counts_sorted) == 1:
            most_common_paths[1].append(([], 0))
            most_common_paths_counts[1].append(0)
            most_common_paths[2].append(([], 0))
            most_common_paths_counts[2].append(0)

        if len(all_paths_counts_sorted) == 2:
            most_common_paths[2].append(([], 0))
            most_common_paths_counts[2].append(0)

        most_common_paths[3].append(min_path)

        iterations.append(iteration)
    determinant_ant = Ant(-1, graph, begin, end)

    determinant_ant.walk_to_goal_extended()

    final_path = determinant_ant.path_walked

    # print(final_path)
    # print(determinant_ant.distance_walked)

    # create_statistics(iterations, most_common_paths, most_common_paths_counts)

    return final_path, determinant_ant.distance_walked


def create_statistics(iterations, most_common_paths, most_common_paths_counts):
    distances0 = [dist for _, dist in most_common_paths[0]]
    distances1 = [dist for _, dist in most_common_paths[1]]
    distances2 = [dist for _, dist in most_common_paths[2]]
    distances_min = [dist for _, dist in most_common_paths[3]]

    counts0 = most_common_paths_counts[0]
    counts1 = most_common_paths_counts[1]
    counts2 = most_common_paths_counts[2]

    fig, axs = plt.subplots(2, 1, figsize=(6, 7))

    ax = axs[0]
    ax.plot(iterations, distances0, 'r-', label='Most popular path')
    ax.plot(iterations, distances_min, 'c-', label='Shortest path found')
    ax.grid(True)
    ax.set_title('Most popular and shortest path lengths')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Path length')

    ax = axs[1]
    ax.plot(iterations, counts0, 'r-', iterations, counts1, 'g-', iterations, counts2, 'b-')
    ax.grid(True)
    ax.set_title('Top three popular paths')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Number of ants that chose this path')

    plt.tight_layout()
    plt.savefig('./figure.png')
