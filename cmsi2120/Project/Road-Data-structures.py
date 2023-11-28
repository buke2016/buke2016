# https://www.codeproject.com/Questions/5357597/Using-data-structure-on-Python-with-algorithm-to-c
# https://www.codeproject.com/Questions/5357597/Using-data-structure-on-Python-with-algorithm-to-c#:~:text=Using%20data%20structure%20on%20Python%20with%20algorithm%20to%20create%20road%20maps
# Write a function that takes as arguments:

#A string representing JSON graph of the road system
#The starting intersection (node)
#The ending intersection (node)
#And returns a dictionary containing information about the shortest path.

#The return value should be a dictionary with keys distance and path.

#distance should be the number that is the total sum of the distance metadata on each edge used.

# functions to achieve this
import json
from collections import deque
from typing import Dict, List, Tuple, Union



def parse_roads(roads) -> Dict[int, List[Tuple[int, Dict[str, float]]]]:
    graph = {}
    if isinstance(roads, str):
        roads = json.loads(roads)
    for road in roads:
        if isinstance(road, tuple):
            src, dest, distance = road
        elif isinstance(road, dict):
            src, dest, distance = road["src"], road["dest"], road["distance"]
        else:
            raise ValueError("Invalid input format")
        metadata = {"distance": distance}
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        graph[src].append((dest, metadata))
        graph[dest].append((src, metadata))
				
    return graph

def navigate(roads: str, start: int, end: int) -> Dict[str, Union[int, List[int]]]:
    graph = parse_roads(roads)
		 
    if start not in graph or end not in graph:
        return {"error": "Starting or ending node not found in graph"}

    distances = {node: float("inf") for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0

    unvisited_nodes = set(graph)

    while unvisited_nodes:
        current_node = min(
            unvisited_nodes, key=lambda node: distances[node]
        )
        unvisited_nodes.remove(current_node)

        if distances[current_node] == float("inf"):
            break

        for neighbor, metadata in graph[current_node]:
            alternative_route = distances[current_node] + metadata["distance"]
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_nodes[neighbor] = current_node

    path, current_node = [], end
    while previous_nodes[current_node] is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.append(start)

    return {"distance": distances[end], "path": list(reversed(path))}

# Test cases that checks all test pass when functions are used correctly

roads = """
{
  "directed": false,
  "nodes": [
    { "id": 0 },
    { "id": 1 },
    { "id": 2 },
    { "id": 3 },
    { "id": 4 },
    { "id": 5 },
    { "id": 6 },
    { "id": 7 },
    { "id": 8 },
    { "id": 9 }
  ],
  "edges": [
    {
      "source": 1,
      "target": 6,
      "label": "Oak Street",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 6,
      "target": 8,
      "label": "Oak Street",
      "metadata": {
        "distance": 6
      }
    },
    {
      "source": 8,
      "target": 9,
      "label": "Oak Street",
      "metadata": {
        "distance": 11
      }
    },
    {
      "source": 8,
      "target": 7,
      "label": "Robin Way",
      "metadata": {
        "distance": 3
      }
    },
    {
      "source": 7,
      "target": 4,
      "label": "Robin Way",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 6,
      "target": 7,
      "label": "Mountain Road",
      "metadata": {
        "distance": 8
      }
    },
    {
      "source": 7,
      "target": 9,
      "label": "Mountain Road",
      "metadata": {
        "distance": 9
      }
    },
    {
      "source": 4,
      "target": 3,
      "label": "National Street",
      "metadata": {
        "distance": 6
      }
    },
    {
      "source": 1,
      "target": 0,
      "label": "Sunrise Drive",
      "metadata": {
        "distance": 4
      }
    },
    {
      "source": 0,
      "target": 3,
      "label": "Short Street",
      "metadata": {
        "distance": 3
      }
    },
    {
      "source": 5,
      "target": 4,
      "label": "Rickety Creek",
      "metadata": {
        "distance": 7
      }
    },
    {
      "source": 4,
      "target": 0,
      "label": "Rickety Creek",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 9,
      "target": 5,
      "label": "Uphill Grove",
      "metadata": {
        "distance": 6
      }
    },
    {
      "source": 5,
      "target": 2,
      "label": "Uphill Grove",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 2,
      "target": 3,
      "label": "Uphill Grove",
      "metadata": {
        "distance": 7
      }
    }
  ]
}
"""

Test.assert_equals(navigate(roads, 1, 5), {'distance': 16, 'path': [ 1, 0, 4, 5 ]})
Test.assert_equals(navigate(roads, 6, 2), {'distance': 19, 'path': [ 6, 1, 0, 3, 2 ]})
Test.assert_equals(navigate(roads, 3, 4), {'distance': 6, 'path': [ 3, 4 ]})