import copy

import run_genetic
import utils
from graph_generator import generate_graph
from ant_colony import AntColony
import numpy as np

def test_coefficients_aco(number_of_ants, number_of_generations, nodes_count,
                      pe_range, pe_step,
                      le_range, le_step,
                      ec_range, ec_step,
                      plc_range, plc_step):
    graph = generate_graph(1000, 1000, nodes_count)

    with open("wyniki_aoc.csv", mode='w') as results:
        results.write("iteration;pheromone_exponent;length_exponent;evaporation_coefficient"
                      ";pheromone_leaving_coefficient;total_distance;path;\n")
        iters = 0
        for pe in np.linspace(pe_range[0], pe_range[1], int((pe_range[1]-pe_range[0]) / pe_step)):
            for le in np.linspace(le_range[0], le_range[1], int((le_range[1]-le_range[0]) / le_step)):
                for ec in np.linspace(ec_range[0], ec_range[1], int((ec_range[1]-ec_range[0]) / ec_step)):
                    for plc in np.linspace(plc_range[0], plc_range[1], int((plc_range[1]-plc_range[0]) / plc_step)):
                        iters += 1
                        g = copy.deepcopy(graph)
                        colony = AntColony(g, number_of_ants, number_of_generations)
                        path, dist, steps = colony.simulate(pe, le, ec, plc)

                        results.write(f"{iters};{pe:02};{le:02};{ec:02};{plc:02};{dist};{path};\n")

def test_coefficients_genetic(nodes_count,
                      nog_range, nog_step,
                      ps_range, ps_step,
                      es_range, es_step,
                      mr_range, mr_step):
    graph = generate_graph(1000, 1000, nodes_count)

    with open("wyniki_genetics.csv", mode='w') as results:
        results.write("iteration;pheromone_exponent;length_exponent;evaporation_coefficient"
                      ";pheromone_leaving_coefficient;total_distance;path;\n")
        iters = 0
        for nog in np.linspace(nog_range[0], nog_range[1], int((nog_range[1]-nog_range[0]) / nog_step)):
            for ps in np.linspace(ps_range[0], ps_range[1], int((ps_range[1]-ps_range[0]) / ps_step)):
                for es in np.linspace(es_range[0], es_range[1], int((es_range[1]-es_range[0]) / es_step)):
                    for mr in np.linspace(mr_range[0], mr_range[1], int((mr_range[1]-mr_range[0]) / mr_step)):
                        iters += 1
                        g = copy.deepcopy(graph)
                        #colony = AntColony(g, number_of_ants, number_of_generations)
                        path, steps = run_genetic.genetic(g, generations=int(nog), population_size=int(ps), elite_size=int(es), mutation_rate=mr)
                        dist = utils.calculate_total_distance(g, path)
                        results.write(f"{iters};{nog:02};{ps:02};{es:02};{mr:02};{dist:02};{path};\n")
