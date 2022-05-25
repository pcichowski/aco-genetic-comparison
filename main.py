from graph_generator import generate_graph
import networkx as nx
from matplotlib import pyplot as plt

g = generate_graph(100, 100, 10)

poss = nx.get_node_attributes(g, 'pos')
print(poss)

nx.draw(g, poss)

plt.show()
