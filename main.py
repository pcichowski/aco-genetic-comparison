from graph_generator import generate_graph
import networkx as nx
from matplotlib import pyplot as plt
from ant_colony import AntColony

from ant import Ant

g = generate_graph(100, 100, 10)

poss = nx.get_node_attributes(g, 'pos')
print(poss)

nx.draw(g, poss)

plt.show()

colony = AntColony(g, 200, 50)
colony.evaporate_pheromones(0.5)
