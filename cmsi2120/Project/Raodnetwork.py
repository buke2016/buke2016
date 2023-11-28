import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

class StreetNetworkModule:
    def __init__(self, city):
        self.city = city
        self.G = ox.graph_from_place(self.city, network_type='drive')

    def visualize_network(self):
        fig, ax = ox.plot_graph(self.G, figsize=(10, 10), node_size=0.2, edge_linewidth=0.5, edge_color='#999999')
        plt.show()

    def calculate_network_statistics(self):
        G_proj = ox.project_graph(self.G)
        nodes_proj = ox.graph_to_gdfs(G_proj, edges=False)
        graph_area_m = nodes_proj.unary_union.convex_hull.area
        print("Area of the network:", graph_area_m / 1000000, "square kilometers")

    def shortest_path(self, origin, destination):
        origin_node = ox.get_nearest_node(self.G, origin)
        destination_node = ox.get_nearest_node(self.G, destination)
        route = nx.shortest_path(self.G, origin_node, destination_node, weight='length')
        return route

# Example usage
city_module = StreetNetworkModule('Los Angeles, California')
city_module.visualize_network()
city_module.calculate_network_statistics()
route = city_module.shortest_path((34.0522, -118.2437), (34.0522, -118.2437))
print("Shortest path route:", route)