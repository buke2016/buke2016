import osmnx as ox
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import traffic


def plot_traffic_analysis(network_type):
    # Download the street network with additional attributes (e.g., edge lengths, speed limits)
    G = ox.graph_from_place(
        "Los Angeles, California, USA",
        network_type=network_type,
        network_speeds=True,
        simplify=False,
    )

    # Fetch real-time traffic information using the traffic library
    bbox = ox.bbox_from_place(place_name, network_type=network_type)
    traffic_data = traffic.Traffic.from_bbox(bbox=bbox, key="YOUR_TOMTOM_API_KEY")

    # Calculate the node degrees
    degrees = dict(G.degree())

    # Convert the degrees to a NumPy array for numerical operations
    degrees_array = np.array(list(degrees.values()))

    # Calculate the average node degree
    average_degree = np.mean(degrees_array)

    # Plot the network
    ox.plot_graph(
        G,
        bgcolor="w",
        node_size=30,
        node_color="#999999",
        edge_linewidth=0.5,
        edge_color="#999999",
    )

    # Display the plot with the average node degree and traffic analysis details
    plt.title(
        f"{network_type.capitalize()} Network\nAverage Node Degree: {average_degree:.2f}"
    )

    # Display traffic information (if available)
    if traffic_data is not None:
        print("\nReal-time Traffic Information:")
        print(traffic_data.current)

    plt.show()


# Specify different network types and plot them with traffic analysis
network_types = ["drive", "drive_service", "walk", "bike", "all", "all_private"]

# Loop through network types and generate plots with traffic analysis
for network_type in network_types:
    print(f"Plotting {network_type} network with traffic analysis...")
    plot_traffic_analysis(network_type)

