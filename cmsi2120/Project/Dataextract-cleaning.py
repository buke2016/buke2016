# Data extraction and cleaning
road_data = [
    {"road_name": "A", "start_node": 1, "end_node": 2, "road_type": "highway", "length": 10},
    {"road_name": "B", "start_node": 2, "end_node": 3, "road_type": "secondary", "length": 5},
    {"road_name": "C", "start_node": 3, "end_node": 4, "road_type": "primary", "length": 8},
]

# Data transformation and standardization
standardized_road_data = []
for road in road_data:
    road_segment = {
        "id": road["road_name"],
        "start": road["start_node"],
        "end": road["end_node"],
        "type": road["road_type"],
        "length": road["length"],
    }
    standardized_road_data.append(road_segment)

# Data loading into graph data structure
road_network = {}
for road_segment in standardized_road_data:
    if road_segment["start"] not in road_network:
        road_network[road_segment["start"]] = []
    road_network[road_segment["start"]].append((road_segment["end"], road_segment["type"], road_segment["length"]))

# Print the road network
print(road_network)
