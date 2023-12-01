from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from data.building import Building
import heapq
import networkx as nx
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os

app = Flask(__name__)
Bootstrap(app)

graph = Building()

@app.route('/')
def index():
    buildings = list(graph.graph.keys())
    selected_buildings = ['GD 8', 'GD 9', 'KB', 'Auditorium', 'GD 5', 'GD 7', 'KL']
    return render_template('index.html', buildings=selected_buildings)


@app.route('/shortest_path', methods=['POST'])
def calculate_shortest_path():
    start_building = request.form['start_building']
    end_building = request.form['end_building']

    result = shortest_path_algorithm(graph, start_building, end_building)

    shortest_route = result['path']
    distance_in_meters = result['distance']

    graph_image_path = generate_graph_image(graph, shortest_route, start_building, end_building)

    return jsonify({'status': 'success',
                    'result': f'>> Rute terpendek dari {start_building} ke {end_building}: <br>{shortest_route}<br> >> Jarak: {distance_in_meters} meter',
                    'graph_image_path': graph_image_path})


def generate_graph_image(building, shortest_route, start, end):
    G = nx.DiGraph(building.graph)

    pos = nx.spring_layout(G, k=0.3)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='black', width=2,
            arrows=True, connectionstyle='arc3,rad=0.1', edgecolors='black')
    nx.draw_networkx_nodes(G, pos, nodelist=shortest_route, node_color='red', node_size=1000, edgecolors='black')
    node_labels = {node: node if node in shortest_route else '' for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels)

    graph_image_path = f"static/images/graph_{start}_{end}.png"
    plt.savefig(graph_image_path)
    plt.close()

    return graph_image_path


def shortest_path_algorithm(building, start, end):
    graph = building.graph
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

    shortest_route = paths[end]
    distance_in_meters = distances[end]

    return {'path': shortest_route, 'distance': distance_in_meters}


if __name__ == '__main__':
    app.run(debug=True)
