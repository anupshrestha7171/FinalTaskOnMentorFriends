import networkx as nx
import matplotlib.pyplot as plt

# Load the graph from the .graphml file
G = nx.read_graphml('knowledge_graph.graphml')

# Draw the graph using matplotlib
pos = nx.spring_layout(G, k=0.5)
nx.draw(G, pos, with_labels=True, font_size=8, node_size=2000, node_color='lightblue', edge_color='gray', width=1, alpha=0.8)

# Show the plot
plt.show()
plt.savefig('graph.png')