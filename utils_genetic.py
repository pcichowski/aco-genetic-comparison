import numpy as np


def plot_route(ax, graph, solution):
    coords = get_coords(graph)
    solution_coords = [coords[i] for i in solution]
    x, y = zip(*solution_coords)

    # Draw the primary path for the TSP problem
    for i in range(-1, len(x) - 1):
        ax.plot((x[i], x[i+1]), (y[i], y[i+1]), marker='o', color='g')

    # Set axis too slightly larger than the set of x and y
    ax.set_xlim(min(x)*1.1, max(x)*1.1)
    ax.set_ylim(min(y)*1.1, max(y)*1.1)


def get_coords(graph):
    coords = []
    for node in graph.nodes:
        coords.append(graph.nodes[node]['pos'])
    return coords


def plot_improvement(ax, graph, steps):
    progress = []
    for solution in steps:
        progress.append(fitness(graph, solution))
    ax.plot(progress)

    ax.set_ylabel('Distance')
    ax.set_xlabel('Iteration step')


def generate_random_coords(nb_coords):
    coords = []
    for i in range(nb_coords):
        x = np.random.random() * 1000
        y = np.random.random() * 1000
        coords.append((x, y))

    return coords


def dist(n0, n1):
    return np.sqrt((n0[0] - n1[0]) ** 2 + (n0[1] - n1[1]) ** 2)


def fitness(graph, solution):
    """

    :param graph: input graph
    :param solution: path, list of vertex indices
    :return: fitness - how good a solution path is
    """
    coords = get_coords(graph)
    nb_coords = len(coords)
    assert sorted(solution) == list(range(nb_coords))

    fit = 0
    for i in range(nb_coords):
        n0 = coords[solution[i % nb_coords]]
        n1 = coords[solution[(i + 1) % nb_coords]]
        fit += dist(n0, n1)
    return fit
