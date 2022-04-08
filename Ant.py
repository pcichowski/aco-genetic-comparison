import numpy as np


class Ant:
    def __init__(self, id, graph, begin, end):
        self.id = id
        self.graph = graph
        self.begin = begin
        self.end = end
        self.current_node = begin

    def generate_solutions(self, graph, node):
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
            probability = pheromone ** alpha * (1 / distance ** beta) / sum

            possible_solutions.append(neighbor)
            probabilities.append(probability)

        return possible_solutions, probabilities

    def walk_to_goal(self):

        path_walked = []

        while self.current_node != end:
            solutions, probabilities = self.generate_solutions(self.graph, self.current_node)

            solution = np.choice(solutions, probabilities)

            path_walked.append(solution)

            self.current_node = solution


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

