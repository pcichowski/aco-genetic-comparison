import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

subax2 = plt.subplot(111)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

plt.show()