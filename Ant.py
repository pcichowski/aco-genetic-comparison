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

