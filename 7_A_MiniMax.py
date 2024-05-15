import math

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def minimax(node, depth, maximizing_player):    
    if depth == 0 or len(node.children) == 0:
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)

        return max_eval
    
    else:
        min_eval = math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)

        return min_eval

tree =  Node(value=None, children=[
        Node(value=None, children=[
        Node(value=3),
        Node(value=12),
        Node(value=8)
    ]),

        Node(value=None, children=[
        Node(value=2),
        Node(value=4),
        Node(value=6)
    ]),

        Node(value=None, children=[
        Node(value=14),
        Node(value=5),
        Node(value=7)
    ])
])

result = minimax(tree, 2, True)
print("The Optimal Value is:", result)
