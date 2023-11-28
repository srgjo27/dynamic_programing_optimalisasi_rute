from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from data.building import Building
import heapq

app = Flask(__name__)
Bootstrap(app)

graph = Building()

# Add a route for the homepage
@app.route('/')
def index():
    # Retrieve the list of buildings from the graph
    buildings = list(graph.graph.keys())
    selected_buildings = ['GD 8', 'GD 9', 'KB', 'Auditorium', 'GD 5', 'GD 7', 'KL']
    return render_template('index.html', buildings=selected_buildings)

# Add a route for the shortest path calculation
@app.route('/shortest_path', methods=['POST'])
def calculate_shortest_path():
    start_building = request.form['start_building']
    end_building = request.form['end_building']
    
    result = shortest_path_algorithm(graph, start_building, end_building)

    # Extract the path and distance from the result
    shortest_route = result['path']
    distance_in_meters = result['distance']

    return jsonify({'status': 'success', 'result': f'>> Rute terpendek dari {start_building} ke {end_building}: <br>{shortest_route}<br> >> Jarak: {distance_in_meters} meter'})

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

    # Extract the path and distance from the result
    shortest_route = paths[end]
    distance_in_meters = distances[end]

    return {'path': shortest_route, 'distance': distance_in_meters}

if __name__ == '__main__':
    app.run(debug=True)
