import tkinter as tk
from tkinter import messagebox
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import ipywidgets as widgets
from IPython.display import display

class CityStreetNetwork:
    def __init__(self):
        self.city_name_widget = widgets.Text(
            value='',
            placeholder='Enter City Name, Country',
            description='City:',
            disabled=False
        )

        self.visualize_button = widgets.Button(description='Visualize')
        self.visualize_button.on_click(self.visualize_callback)

        self.output = widgets.Output()

        self.city_network = None
        self.graph = None

        self.create_gui()

    def _get_city_network(self):
        try:
            return ox.graph_from_place(self.city_name_widget.value, network_type='all')
        except Exception as e:
            print(f"Error: {e}")
            return None

    def visualize_callback(self, button):
        with self.output:
            self.graph = self._get_city_network()
            self.visualize()

    def visualize(self):
        if self.graph:
            ox.plot_graph(self.graph, fig_height=10, node_color='skyblue', node_size=30, edge_color='gray', linewidth=0.5)
            plt.show()
        else:
            print("Unable to visualize. No graph data available.")

    def create_gui(self):
        display(self.city_name_widget)
        display(self.visualize_button)
        display(self.output)


class StreetNetworkGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        master.title("Street Network Analysis")

        self.city_network = CityStreetNetwork()

        self.visualize_button = tk.Button(self, text="Visualize Network", command=self.city_network.create_gui)
        self.visualize_button.pack()

        self.stats_button = tk.Button(self, text="Calculate Network Statistics", command=self.calculate_network_statistics)
        self.stats_button.pack()

        self.shortest_path_button = tk.Button(self, text="Find Shortest Path", command=self.find_shortest_path)
        self.shortest_path_button.pack()

    def calculate_network_statistics(self):
        # Add code to calculate network statistics using OSMnx
        if self.city_network.graph:
            statistics = {
                "Number of Nodes": len(self.city_network.graph.nodes),
                "Number of Edges": len(self.city_network.graph.edges),
            }
            messagebox.showinfo("Network Statistics", "\n".join(f"{key}: {value}" for key, value in statistics.items()))
        else:
            messagebox.showwarning("No Data", "Please visualize the network first.")

    def find_shortest_path(self):
        # Add code to find the shortest path using NetworkX
        if self.city_network.graph:
            try:
                source = int(tk.simpledialog.askstring("Source Node", "Enter source node:"))
                target = int(tk.simpledialog.askstring("Target Node", "Enter target node:"))
                shortest_path = nx.shortest_path(self.city_network.graph, source=source, target=target)
                messagebox.showinfo("Shortest Path", f"Shortest Path: {shortest_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
        else:
            messagebox.showwarning("No Data", "Please visualize the network first.")


root = tk.Tk()
my_gui = StreetNetworkGUI(root)
my_gui.pack()
root.mainloop()
