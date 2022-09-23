from custom_hierarchical_layout import hierarchical_layout
import plotly.graph_objects as go
import networkx as nx
import json
import datetime

# Import graph network from JSON
with open('json_graph.json') as json_file:
    graph = json.load(json_file)
G = nx.node_link_graph(graph)

# Create coordinates and assign them as node attributes
loan_canvas, nonloan_canvas, pos = hierarchical_layout(G)
nx.set_node_attributes(G, pos, "pos")

# Set up plotting of edges
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.extend((x0, x1, None))
    edge_y.extend((y0, y1, None))

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.75, color='#888'),
    hoverinfo='none',
    mode='lines')

# Set up plotting of nodes
node_x = []
node_y = []
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=20,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

node_color = []
node_shape = []
node_text = []
for node, adjacencies in G.adjacency():
    if node == 'CA':
        node_color.append('#848686')
        node_shape.append('hexagon')
    elif node in ['01', '02']:
        node_color.append('#E5B50A')
        node_shape.append('pentagon')
    else:
        node_color.append('#00AB95')
        node_shape.append('circle')
    node_text.append(f"{node}, x,y={G.nodes[node]['pos']}")

node_trace.marker.color = node_color
node_trace.marker.symbol = node_shape
node_trace.text = node_text

fig = go.Figure(
    data=[edge_trace, node_trace],
    layout=go.Layout(
        title='<b>Example graph</b>',
        titlefont_size=14,
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20,l=5,r=5,t=40),
        annotations=[
            dict(
                text=f"<b>DP</b>, {datetime.datetime.now().strftime('%Y-%m-%d')}",
                showarrow=False,
                xref="paper", yref="paper",
                x=0.005, y=-0.002
            )
        ],
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        template='plotly_white'
    )
)

# Adjusting x and y axes
fig.update_xaxes(range=[-loan_canvas, nonloan_canvas])
fig.update_yaxes(range=[-1.0, 1.0])
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)

fig.show()
