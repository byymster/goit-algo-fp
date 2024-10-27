import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = set()

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))
        self.nodes.add(from_node)
        self.nodes.add(to_node)

    def dijkstra(self, start):
        # Ініціалізація відстаней до всіх вершин як нескінченності
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0

        # Створення черги з пріоритетами з початковою вершиною
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Пропускаємо вузли, які вже мають кращу відстань
            if current_distance > distances[current_node]:
                continue

            # Оновлення відстаней до сусідів
            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусіда
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Приклад використання
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)

    start_node = 'A'
    distances = graph.dijkstra(start_node)

    print(f"Відстані від вершини {start_node} до інших вершин:")
    for node, distance in distances.items():
        print(f"{start_node} -> {node}: {distance}")
