import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Specify the location (Los Angeles, California, USA)
place_name = "Los Angeles, California, USA"

# Function to download and plot the street network
def plot_street_network(network_type):
    # Download the street network
    G = ox.graph_from_place(place_name, network_type=network_type)

    # Plot the network
    ox.plot_graph(G, bgcolor='w', node_size=30, node_color='#999999', edge_linewidth=0.2, edge_color='#999999')

    # Display the plot
    plt.show()

# Specify different network types and plot them
network_types = ['drive', 'drive_service', 'walk', 'bike', 'all', 'all_private']

for network_type in network_types:
    print(f"Plotting {network_type} network...")
    plot_street_network(network_type)
