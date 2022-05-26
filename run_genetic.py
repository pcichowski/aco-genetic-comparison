from matplotlib import pyplot as plt

from genetic import Genetic
from utils_genetic import generate_random_coords, plot_improvement, plot_route, get_coords
from graph_generator import generate_graph


def genetic(graph, generations=500, population_size=100, elite_size=10, mutation_rate=0.01):
    genetic = Genetic(graph, population_size=population_size, elite_size=elite_size, mutation_rate=mutation_rate)

    population = genetic.initial_population()
    best_solution = genetic.best_solution(population)
    steps = [best_solution]
    for i in range(generations):
        population = genetic.next_generation(population)
        best_solution = genetic.best_solution(population)
        steps.append(best_solution)

    return best_solution, steps


# nb_coords = 25
#
# graph = generate_graph(1000, 1000, nb_coords)
# best_solution, steps = genetic(graph)
#
# fig, ax = plt.subplots(ncols=2, figsize=(10,5))
# plot_improvement(ax[0], graph, steps)
# plot_route(ax[1], graph, best_solution)
# plt.show()