import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# Клас вузла дерева
class Node:
    def __init__(self, key, color="black"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


# Функція для додавання ребер у граф
def add_edges(graph, node, pos, x=0, y=0, layer=1, horizontal_spacing=2):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - horizontal_spacing / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1, horizontal_spacing=horizontal_spacing)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + horizontal_spacing / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1, horizontal_spacing=horizontal_spacing)


# Функція для візуалізації дерева з відповідною назвою
def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos, horizontal_spacing=2.5)  # Збільшено горизонтальний відступ

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(title)  # Додавання назви графіка
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Генерація градієнту кольорів
def rgb_gradient(start_color, end_color, steps):
    start_color = [int(start_color[i:i + 2], 16) for i in (1, 3, 5)]
    end_color = [int(end_color[i:i + 2], 16) for i in (1, 3, 5)]
    gradient = []
    for step in range(steps):
        interpolated = [
            int(start_color[i] + (float(step) / (steps - 1)) * (end_color[i] - start_color[i]))
            for i in range(3)
        ]
        gradient.append(f"#{interpolated[0]:02x}{interpolated[1]:02x}{interpolated[2]:02x}")
    return gradient


# Функція обходу в ширину
def bfs(tree_root):
    queue = deque([tree_root])
    colors = rgb_gradient("#8B0000", "#FF4500", len(queue) + 10)  # Від темно-червоного до оранжево-червоного
    idx = 0
    while queue:
        node = queue.popleft()
        node.color = colors[idx]
        idx += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Функція обходу в глибину
def dfs(tree_root):
    stack = [tree_root]
    colors = rgb_gradient("#8B0000", "#FF4500", len(stack) + 10)  # Від темно-червоного до оранжево-червоного
    idx = 0
    while stack:
        node = stack.pop()
        node.color = colors[idx]
        idx += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs(root)
draw_tree(root, "Обхід в глибину (DFS)")

root.color = "black"
root.left.color = "black"
root.left.left.color = "black"
root.left.right.color = "black"
root.right.color = "black"
root.right.left.color = "black"

bfs(root)
draw_tree(root, "Обхід в ширину (BFS)")
