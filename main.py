from graph_generator import generate_graph
import networkx as nx
from matplotlib import pyplot as plt
from ant_colony import AntColony

from ant import Ant

g = generate_graph(100, 100, 10)

poss = nx.get_node_attributes(g, 'pos')
print(poss)

#nx.draw(g, poss)

plt.show()

colony = AntColony(g, 20, 30)
path, cost = colony.simulate(2, 1, 0, 1)
print(path)
print(cost)
