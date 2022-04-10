import numpy as np
from numpy.random import choice
import networkx as nx

alpha = 1.3
beta = 1.4


class Ant:
    def __init__(self, id, graph, begin, end):
        self.distance_walked = 0
        self.path_walked = []

        self.id = id
        self.graph = graph
        self.begin = begin
        self.end = end
        self.alive = True
        self.current_node = begin

    def walk_to_goal_basic(self):

        path_walked = [self.current_node]

        while self.current_node != self.end:
            solutions, probabilities = generate_solutions_basic(self.graph, self.current_node)

            solution = choice(solutions, p=probabilities)

            path_walked.append(solution)
            self.current_node = solution

        path_walked = remove_loops(path_walked)
        self.path_walked = path_walked

        # calculating total distance walked by the ant (without loops)
        for i in range(len(path_walked) - 1):
            node = self.path_walked[i]
            next_node = self.path_walked[i + 1]

            segment_length = self.graph[node][next_node]['distance']
            self.distance_walked += segment_length

    def walk_to_goal_extended(self):
        path_walked = [self.current_node]

        while self.current_node != self.end:
            solutions, probabilities = generate_solutions_extended(self.graph, self.current_node, path_walked)

            if not solutions:
                # ant has nowhere to go and has to die
                self.alive = False
                return

            solution = choice(solutions, p=probabilities)

            path_walked.append(solution)
            self.current_node = solution

        self.path_walked = path_walked

        # calculating total distance walked by the ant (without loops)
        for i in range(len(path_walked) - 1):
            node = self.path_walked[i]
            next_node = self.path_walked[i + 1]

            segment_length = self.graph[node][next_node]['distance']
            self.distance_walked += segment_length
        # mrowka konczy bieg
        # na przebytej drodze zostawiamy troszkę feromonu
        # informacja o przebytej drodze i jej odleglosci w polach klasy Ant


# TODO refactor function to be more optimised
def remove_loops(path):
    j = 1
    while True:
        if j >= len(path):
            break
        el = path[-1 * j]
        itr = len(path) - j
        for i in range(0, itr):
            if path[i] == el:
                path = path[:i] + path[itr:]
                break
        j += 1
    return path


def generate_solutions_basic(graph, node):
    sum = 0
    for neighbor in graph.neighbors(node):
        pheromone = graph[node][neighbor]['pheromone']
        sum += pheromone ** alpha

    possible_solutions = []
    probabilities = []

    for neighbor in graph.neighbors(node):
        pheromone = graph[node][neighbor]['pheromone']
        if sum != 0:
            probability = (pheromone ** alpha) / sum
        else:
            probability = 1 / len(list(nx.neighbors(graph, node)))

        possible_solutions.append(neighbor)
        probabilities.append(probability)

    return possible_solutions, probabilities


def generate_solutions_extended(graph, node, visited_nodes):
    sum = 0
    allowed_neighbors = []

    for neighbor in graph.neighbors(node):
        if neighbor not in visited_nodes:
            allowed_neighbors.append(neighbor)

    for neighbor in allowed_neighbors:
        pheromone = graph[node][neighbor]['pheromone']
        distance = graph[node][neighbor]['distance']
        sum += (pheromone ** alpha) * (1 / distance) ** beta

    possible_solutions = []
    probabilities = []

    for neighbor in allowed_neighbors:
        pheromone = graph[node][neighbor]['pheromone']
        distance = graph[node][neighbor]['distance']
        if sum != 0:
            probability = pheromone ** alpha * (1 / distance ** beta) / sum
        else:
            probability = 1 / len(allowed_neighbors)

        possible_solutions.append(neighbor)
        probabilities.append(probability)

    return possible_solutions, probabilities
