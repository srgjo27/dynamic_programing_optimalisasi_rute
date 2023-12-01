import torch
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    paths = {node: [] for node in graph}
    paths[start] = [start]

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = priority_queue[0]
        priority_queue = priority_queue[1:]
        current_distance = -current_distance  

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(priority_queue, (-distance, neighbor))

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

# Convert graph weights to PyTorch tensors
for node in graph:
    for neighbor in graph[node]:
        graph[node][neighbor] = torch.tensor(graph[node][neighbor], dtype=torch.float)

# Find the shortest route
start_node = 'GD 8'
end_node = 'GD 7'
shortest_route = dijkstra(graph, start_node, end_node)
print(f'Rute terpendek dari {start_node} ke {end_node}: {shortest_route}')

# Create a directed graph using networkx
G = nx.DiGraph(graph)

# Draw the graph with black arrows and red nodes
pos = nx.spring_layout(G, k=0.3)  # Adjust the value of k for optimal node spacing
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='black', width=2, arrows=True, connectionstyle='arc3,rad=0.1', edgecolors='black')
nx.draw_networkx_nodes(G, pos, nodelist=shortest_route, node_color='red', node_size=1000, edgecolors='black')

# Add labels to the nodes
node_labels = {node: node if node in shortest_route else '' for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels)

# Show the plot
plt.show()
