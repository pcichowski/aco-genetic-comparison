import copy

import numpy as np
from utils_genetic import fitness, get_coords
from random import random, randint, choice


class Genetic:
    def __init__(self, graph, population_size=100, elite_size=10, mutation_rate=0.01):
        self.graph = graph
        self.population_size = population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate

    def population_fitness(self, population):
        population_fitness = {}
        for i, individual in enumerate(population):
            population_fitness[i] = 1/fitness(self.graph, individual)

        return {k: v for k, v in sorted(population_fitness.items(), key=lambda item: item[1], reverse=True)}

    def best_solution(self, population):
        population_fitness = list(self.population_fitness(population))
        best_ind = population_fitness[0]
        return population[best_ind]

    def initial_population(self):
        population = []
        # Create initial population
        for i in range(self.population_size):
            solution = np.random.permutation(len(get_coords(self.graph)))
            population.append(solution)

        return population

    def selection(self, population):
        # print(population)
        selection = []
        pop_fitness = self.population_fitness(population)

        # print(elite)
        probability = {}
        sum_fitness = sum(pop_fitness.values())
        prob_prev = 0.0
        for key, value in pop_fitness.items():
            probability[key] = prob_prev + (value / sum_fitness)
            prob_prev = probability[key]

        for i, key in enumerate(pop_fitness.keys()):
            if i >= self.elite_size:
                break
            selection.append(population[key])

        for i in range(len(population) - self.elite_size):
            rand = np.random.random()

            for key, value in probability.items():
                if rand <= value:
                    selection.append(population[key])
                    break

        return selection

    def crossover_population(self, population):
        children = []

        for i in range(self.elite_size):
            children.append(population[i])

        for i in range(len(population) - self.elite_size):
            parent_a = choice(population)
            parent_b = choice(population)

            slice_low = randint(0, len(parent_a))
            slice_high = randint(slice_low, len(parent_a))

            slice_right = len(parent_a) - slice_high

            parent_slice = list(parent_a[slice_low:slice_high])

            offspring = [x for x in parent_b if x not in parent_slice]

            if slice_right == 0:
                offspring = offspring[:len(offspring) - slice_right] + parent_slice
            else:
                offspring = offspring[:len(offspring) - slice_right] + parent_slice + offspring[-slice_right:]

            children.append(np.array(offspring))
        return children

    def mutate_population(self, population):
        elite = population[:self.elite_size]
        newp = []
        for p in population:
            newp.append(self.mutate(p, self.mutation_rate))
        elite_selection = newp[self.elite_size:]
        return elite + elite_selection

    def mutate(self, individual_c, rate):
        individual = copy.deepcopy(individual_c)
        for i in range(len(individual)):
            rand = random()
            if rand <= rate:
                ind = randint(0, len(individual) - 1)
                individual[i], individual[ind] = individual[ind], individual[i]

        return individual

    def next_generation(self, population):
        selection = self.selection(population)
        children = self.crossover_population(selection)
        next_generation = self.mutate_population(children)
        return next_generation
