graph = {
    'A' : ['G', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'D'],
    'D' : ['A', 'E', 'F'],
    'E' : ['F', 'G'],
    'F' : ['C', 'B'],
    'G' : ['A', 'D']
}

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end = " ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')