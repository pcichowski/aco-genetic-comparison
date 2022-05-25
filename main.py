from graph_generator import generate_graph
import networkx as nx

g = generate_graph(1000,1000, 20)
nx.draw(g, nx.get_node_attributes(g, 'pos'))
print("test")