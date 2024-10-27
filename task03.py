import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней та попередників
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}

    # Використовуємо чергу з пріоритетами (heap) для вибору вершини з мінімальною відстанню
    priority_queue = [(0, start)]  # Кожен елемент: (відстань, вершина)

    while priority_queue:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдена відстань вже більша за збережену, продовжуємо (оптимізація)
        if current_distance > distances[current_vertex]:
            continue

        # Оновлюємо відстані для сусідів
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex 
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад графа у вигляді словника
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

# Виклик функції для вершини A
distances = dijkstra(graph, 'A')
print("Найкоротші відстані від A:", distances)

