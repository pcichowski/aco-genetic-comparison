import copy
import numpy as np


class Ant:
    NO_NODES_AVAILABLE = -1

    def __init__(self, id, graph, starting_node):
        self.id = id
        self.graph = graph
        self.path = [starting_node]
        self.starting_node = starting_node
        self.current_node = starting_node
        self.cost = 0

    def move_to(self, node):
        self.path.append(node)
        self.cost += self.graph[self.current_node][node]['distance']
        self.current_node = node

    def get_available_nodes(self):
        available_nodes = list(copy.deepcopy(self.graph.nodes))

        for node in self.path:
            available_nodes.remove(node)

        return available_nodes

    # available_nodes jest uzyskiwany z get_available_nodes w funkcji wywołującej
    def count_probability(self, available_nodes, pheromone_exponent, length_exponent):
        probabilities = {}
        probability_nominator = {}
        probability_denominator = 0

        for node in available_nodes:
            pheromone = self.graph[self.current_node][node]['pheromone']
            length_coefficient = 1 / self.graph[self.current_node][node]['distance']

            probability_nominator[node] = (pheromone ** pheromone_exponent) * (length_coefficient ** length_exponent)
            probability_denominator += probability_nominator[node]

        for node in available_nodes:
            probabilities[node] = probability_nominator[node] / probability_denominator

        return probabilities

    # returns node index; if no nodes are available then it returns NO_NODES_AVAILABLE
    def select_move(self, pheromone_exponent, length_exponent):
        available_nodes = self.get_available_nodes()
        if not available_nodes:
            # TODO finish
            return self.NO_NODES_AVAILABLE

        probabilities = self.count_probability(available_nodes, pheromone_exponent, length_exponent)

        return np.random.choice(available_nodes, p=list(probabilities.values()))

    def leave_pheromones(self, pheromone_coefficient):
        pheromone_value = self.calculate_pheromone(pheromone_coefficient)
        for i in range(len(self.path) - 1):
            self.graph[i][i + 1]['pheromone'] += pheromone_value

    def calculate_pheromone(self, pheromone_coefficient):
        return pheromone_coefficient / self.cost

    def go(self, pheromone_exponent, length_exponent):
        selected_node = self.select_move(pheromone_exponent, length_exponent)
        while selected_node != self.NO_NODES_AVAILABLE:
            self.move_to(selected_node)
            selected_node = self.select_move(pheromone_exponent, length_exponent)

        self.move_to(self.starting_node)

        return self.cost
