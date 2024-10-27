import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(arr, index=0):
    if index >= len(arr):
        return None

    node = Node(arr[index])
    node.left = build_heap_tree(arr, 2 * index + 1)
    node.right = build_heap_tree(arr, 2 * index + 2)
    return node

def heap_sort(arr):
    h = []
    for value in arr:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]

def generate_color_gradient(step, total_steps, color="blue"):
    intensity = int((step / total_steps) * 255)
    if color == "blue":
        return f'#{intensity:02x}{intensity:02x}ff'
    elif color == "green":
        return f'#{intensity:02x}ff{intensity:02x}'
    elif color == "red":
        return f'#ff{intensity:02x}{intensity:02x}'
    return f'#{intensity:02x}{intensity:02x}{intensity:02x}'

def bfs(root, color="blue"):
    if not root:
        return

    queue = deque([root])
    step = 0
    total_steps = count_nodes(root)

    while queue:
        node = queue.popleft()
        node.color = generate_color_gradient(step, total_steps, color)
        step += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs(root, color="red"):
    if not root:
        return

    stack = [root]
    step = 0
    total_steps = count_nodes(root)

    while stack:
        node = stack.pop()
        node.color = generate_color_gradient(step, total_steps, color)
        step += 1

        # Спочатку додаємо правого, щоб лівий обробився першим
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# Масив, який потрібно перетворити на мін-купу
heap_array = [0, 4, 5, 10, 1, 3]

# Сортуємо масив за допомогою heap_sort
sorted_arr = heap_sort(heap_array)

# Будуємо бінарне дерево з відсортованого масиву
root_bfs = build_heap_tree(sorted_arr)
root_dfs = build_heap_tree(sorted_arr)
# Виконуємо обхід у ширину або глибину та призначаємо кольори
bfs(root_bfs, color="blue")
dfs(root_dfs, color="red")

# Відображаємо дерево після завершення обходу
draw_tree(root_dfs)
draw_tree(root_bfs)
