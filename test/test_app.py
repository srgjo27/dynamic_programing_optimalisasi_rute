import heapq

def dijkstra(graph, start, end):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0

    paths = {node: [] for node in graph}
    paths[start] = [start]

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))
    return paths[end]

graph = {
    'GD 8': {'GD 9': 30, 'KB': 60},
    'GD 9': {'GD 8': 30, 'KB': 60, 'Simpang Pohon Bau': 40},
    'KB': {'GD 8': 60, 'GD 9': 60, 'Simpang Pohon Bau': 10, 'Kantor Vokasi': 80},
    'Simpang Pohon Bau': {'Simpang Gerbang': 325, 'KB': 10, 'GD 9': 40},
    'Kantor Vokasi': {'OT': 110, 'Perpustakaan': 70, 'KB': 80},
    'Simpang Gerbang': {'Simpang Bundaran': 45, 'KL': 230},
    'Perpustakaan': {'Auditorium': 40, 'GD 5': 160, 'Kantor Vokasi': 70},
    'OT': {'GD 5': 90, 'GD 7': 120, 'Kantor Vokasi': 110},
    'Auditorium': {'GD 5': 130, 'Simpang Bundaran': 25, 'KL': 110, 'Perpustakaan': 40},
    'Simpang Bundaran': {'KL': 30, 'Auditorium': 25},
    'KL': {'GD 7': 230, 'Simpang Bundaran': 30},
    'GD 5': {'GD 7': 70, 'Auditorium': 130, 'OT': 90},
    'GD 7': {'GD 5': 70, 'OT': 120, 'KL': 230}
}

start_node = 'GD 8'
end_node = 'GD 5'
shortest_route = dijkstra(graph, start_node, end_node)
print(f'Rute terpendek dari {start_node} ke {end_node}: {shortest_route}')