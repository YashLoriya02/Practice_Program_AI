def depth_limited_search(graph, start, goal, depth_limit):
    stack = [(start, 0, [])]

    while stack:
        node, depth, path = stack.pop()

        if node == goal:
            return path + [node]

        if depth < depth_limit:
            for neighbor in reversed(graph[node]):
                stack.append((neighbor, depth + 1, path + [node]))

    return None

def depth_first_iterative_deepening(graph, start, goal):
    depth_limit = 0

    while True:
        result = depth_limited_search(graph, start, goal, depth_limit)
        if result is not None:
            return result
        depth_limit += 1

graph = {
    'A' : ['G', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'D'],
    'D' : ['A', 'E', 'F'],
    'E' : ['F', 'G'],
    'F' : ['C', 'B'],
    'G' : ['A', 'D']
}

start_node = 'A'
goal_node = 'F'

result_path = depth_first_iterative_deepening(graph, start_node, goal_node)

if result_path:
    print(f"Path from {start_node} to {goal_node}: {result_path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
