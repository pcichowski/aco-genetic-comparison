from genetic import Genetic


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
