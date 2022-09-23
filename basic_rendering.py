import plotly.graph_objects as go
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import json

# Import graph network from JSON
with open('json_graph.json') as json_file:
    graph = json.load(json_file)
G = nx.node_link_graph(graph)

# Plot graph
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)
plt.show()
