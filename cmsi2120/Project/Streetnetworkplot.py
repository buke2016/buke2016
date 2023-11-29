# Import necessary libraries
import osmnx as ox
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Specify the location (Los Angeles, California, USA)
place_name = "Los Angeles, California, USA"

# Function to download and plot the street network
def plot_street_network(network_type):
    # Download the street network
    G = ox.graph_from_place(place_name, network_type=network_type)

    # Calculate the node degrees
    degrees = dict(G.degree())

    # Convert the degrees to a NumPy array for numerical operations
    degrees_array = np.array(list(degrees.values()))

    # Calculate the average node degree
    average_degree = np.mean(degrees_array)

    # Plot the network
    ox.plot_graph(G, bgcolor='w', node_size=30, node_color='#999999', edge_linewidth=0.2, edge_color='#999999')

    # Display the plot with the average node degree in the title
    plt.title(f"{network_type.capitalize()} Network\nAverage Node Degree: {average_degree:.2f}")
    plt.show()

# Specify different network types and plot them
network_types = ['drive', 'drive_service', 'walk', 'bike', 'all', 'all_private']

# Loop through network types and generate plots
for network_type in network_types:
    print(f"Plotting {network_type} network...")
    plot_street_network(network_type)
