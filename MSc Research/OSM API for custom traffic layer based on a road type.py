import folium
import requests

# Set the location and zoom level for the map
location = [39.8283, -98.5795]
zoom_level = 4

# Create the map
map = folium.Map(location=location, zoom_start=zoom_level, tiles="OpenStreetMap")

# Retrieve the road data from the OpenStreetMap API
bbox = map.get_bounds()
bbox_str = f"{bbox[1][1]},{bbox[0][1]},{bbox[1][0]},{bbox[0][0]}"
response = requests.get(f"https://www.openstreetmap.org/api/0.6/map?bbox={bbox_str}")

# Parse the XML data and extract the road information
import xml.etree.ElementTree as ET
root = ET.fromstring(response.text)

# Create a custom style function based on the road type
def style_function(feature):
    road_type = feature["properties"]["highway"]
    if road_type == "motorway":
        color = "red"
    elif road_type in ["trunk", "primary"]:
        color = "orange"
    elif road_type in ["secondary", "tertiary"]:
        color = "yellow"
    else:
        color = "gray"
    return {"color": color}

# Add a GeoJSON layer for the road data
folium.GeoJson(
    root,
    style_function=style_function,
).add_to(map)

# Display the map
map