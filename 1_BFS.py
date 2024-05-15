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
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, 'A')
