import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def f(self):
        return self.g + self.h

class Graph:
    def __init__(self, graph_dict, heuristic_dict):
        self.graph_dict = graph_dict
        self.heuristic_dict = heuristic_dict

    def get_neighbors(self, node):
        return self.graph_dict.get(node, [])

def a_star(graph, start, goal):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (graph.heuristic_dict[start], 0, start, [start]))
    
    while open_list:
        _, g, current, path = heapq.heappop(open_list)
        
        if current == goal:
            return g, path
        
        if current in closed_set:
            continue
        
        closed_set.add(current)
        
        for neighbor, cost in graph.get_neighbors(current):
            if neighbor not in closed_set:
                neighbor_g = g + cost
                neighbor_h = graph.heuristic_dict[neighbor]
                neighbor_path = path + [neighbor]
                heapq.heappush(open_list, (neighbor_g + neighbor_h, neighbor_g, neighbor, neighbor_path))
    
    return float('inf'), []

graph_dict = {
    'A': [('B', 6), ('F', 3)],
    'B': [('D', 2), ('C', 3)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 8)],
    'E': [('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
    'J': [],
}

heuristic_dict = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

graph = Graph(graph_dict, heuristic_dict)

start = 'A'
goal = 'J'

shortest_length, shortest_path = a_star(graph, start, goal)

if shortest_length != float('inf'):
    print("Shortest path length from", start, "to", goal, "is", shortest_length)
    print("Shortest path:", shortest_path)
else:
    print("No path found from", start, "to", goal)
