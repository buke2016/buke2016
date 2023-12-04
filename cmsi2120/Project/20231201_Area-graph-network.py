import networkx as nx

# Assuming you already have the 'area_graph' created
# Function to calculate the shortest network path and distance
def calculate_shortest_path(graph, start, stop):
  try:
    # Check if coordinates are provided
    if isinstance(start, (list, tuple)) and len(start) == 2 and isinstance(stop, (list, tuple)) and len(stop) == 2:
      # Find nearest nodes based on coordinates
      start = nx.get_node_attributes(graph, 'pos')[min(graph.nodes(data='pos'), key=lambda n: euclidean_distance(start, graph.nodes[n]['pos']))]
      stop = nx.get_node_attributes(graph, 'pos')[min(graph.nodes(data='pos'), key=lambda n: euclidean_distance(stop, graph.nodes[n]['pos']))]

    # Calculate shortest path
    path = nx.shortest_path(graph, start, stop, weight="length")
    distance = nx.shortest_path_length(graph, start, stop, weight="length")
    return path, distance
  except nx.NetworkXNoPath:
    print(f"No path found from {start} to {stop}.")
    return None, None

# Define the starting and ending coordinates
start_coord = [33.87882383472052, -118.4042118944318] # actual start coordinates
stop_coord = [33.901248061342244, -118.39275927632005] # actual stop coordinates

# Call the function to retrieve the path and distance
shortest_path, shortest_distance = calculate_shortest_path(area_graph, start_coord, stop_coord)

# Print the results
if shortest_path:
  print(f"Shortest path: {shortest_path}")
  print(f"Shortest distance: {shortest_distance}")
else:
  print("No path found.")