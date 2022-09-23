import pandas as pd
import networkx as nx
import json

hierarchy_df = pd.read_csv('hierarchy_table.csv', index_col=0, dtype=str)

graph_network = nx.from_pandas_edgelist(
    hierarchy_df,
    source='Parent',
    target='Child',
)

json_graph = json.dumps(graph_network, default=nx.node_link_data)

# Using a JSON string
with open('json_graph.json', 'w') as outfile:
    outfile.write(json_graph)
