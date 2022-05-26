import math
import threading

from ant import Ant
import networkx as nx


class AntColony:

    def __init__(self, graph, number_of_ants, number_of_generations):
        self.number_of_ants = number_of_ants
        self.graph = graph
        self.number_of_generations = number_of_generations
        self.best_path = []
        self.best_cost = math.inf
        self.results_lock = threading.Lock()
        self.steps = [] # best paths in each generation

    def run_ant(self, ant, pheromone_exponent, length_exponent):
        cost = ant.go(pheromone_exponent, length_exponent)
        self.add_result(ant.path, cost)

    def add_result(self, path, cost):
        with self.results_lock:
            if cost < self.best_cost:
                self.best_path = path
                self.best_cost = cost

    def evaporate_pheromones(self, evaporation_coefficient):
        edges = self.graph.edges(data=True)
        for edge in edges:
            node1, node2, data = edge
            old_pheromone = data['pheromone']
            self.graph[node1][node2]['pheromone'] = (1 - evaporation_coefficient) * old_pheromone

    def simulate(self, pheromone_exponent, length_exponent, evaporation_coefficient, pheromone_leaving_coefficient,
                 starting_node=0):
        for generation_number in range(self.number_of_generations):
            ants = []
            threads = list()
            for i in range(self.number_of_ants):
                ants.append(Ant(i, self.graph, starting_node))
                x = threading.Thread(target=self.run_ant, args=[ants[i], pheromone_exponent, length_exponent])
                threads.append(x)
                x.start()

            for thread in threads:
                thread.join()

            self.evaporate_pheromones(evaporation_coefficient)

            for ant in ants:
                ant.leave_pheromones(pheromone_leaving_coefficient)

            self.steps.append(self.best_path)

        return self.best_path, self.best_cost, self.steps
