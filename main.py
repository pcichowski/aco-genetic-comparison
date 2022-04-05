import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

subax2 = plt.subplot(111)
nx.draw_circular(G)

plt.show()