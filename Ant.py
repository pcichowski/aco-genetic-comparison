import numpy as np
from numpy.random import choice
import networkx as nx

alpha = 0.5
beta = 1.2


class Ant:
    def __init__(self, id, graph, begin, end):
        self.distance_walked = 0
        self.path_walked = []

        self.id = id
        self.graph = graph
        self.begin = begin
        self.end = end
        self.current_node = begin

    def walk_to_goal(self):

        path_walked = [self.current_node]

        while self.current_node != self.end:
            solutions, probabilities = generate_solutions(self.graph, self.current_node)

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

        # mrowka konczy bieg
        # na przebytej drodze zostawiamy troszkę feromonu
        # informacja o przebytej drodze i jej odleglosci w polach klasy Ant


# TODO refactor function to be more optimised
def remove_loops(path):
    visited = []

    running = True
    while running:
        for itr, el in enumerate(path):
            breaking = False
            if el in visited:
                for i in range(itr - 1, 0, -1):
                    if path[i] == el:
                        new_path = path[:i] + path[itr:]

                        path = new_path
                        breaking = True
                        break
            else:
                visited.append(el)

            if breaking:
                breaking = False
                break
            if itr == len(path) - 1:
                running = False

    return path


def generate_solutions(graph, node):
    sum = 0
    for neighbor in graph.neighbors(node):
        pheromone = graph[node][neighbor]['pheromone']
        distance = graph[node][neighbor]['distance']
        sum += pheromone ** alpha * (1 / distance) ** beta

    possible_solutions = []
    probabilities = []

    for neighbor in graph.neighbors(node):
        pheromone = graph[node][neighbor]['pheromone']
        distance = graph[node][neighbor]['distance']
        if sum != 0:
            probability = pheromone ** alpha * (1 / distance ** beta) / sum
        else:
            probability = 1 / len(list(nx.neighbors(graph, node)))

        possible_solutions.append(neighbor)
        probabilities.append(probability)

    return possible_solutions, probabilities
