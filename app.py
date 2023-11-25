from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from data.building import Building
import heapq

app = Flask(__name__)
Bootstrap(app)
graph = Building()

@app.route('/')
def index():
    buildings = graph.get_buildings()
    return render_template('index.html', buildings=buildings)

def format_path_result(path, distance):
    if path:
        formatted_path = f"Rute terpendek dari {path[0]} ke {path[-1]}: {', '.join(path)}"
        formatted_distance = f"Jarak: {distance} meter"
        return f"{formatted_path}\n{formatted_distance}"
    else:
        return "Tidak ada rute yang valid"

def shortest_path_algorithm(start, end):
    distances = {building: float('infinity') for building in graph.get_buildings()}
    previous_nodes = {building: None for building in graph.get_buildings()}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.get_buildings():
            weight = graph.get_distance(current_node, neighbor)
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current_building = end
    while previous_nodes[current_building] is not None:
        path.insert(0, current_building)
        current_building = previous_nodes[current_building]
    path.insert(0, start)

    return path if distances[end] != float('infinity') else None

@app.route('/shortest_path', methods=['GET', 'POST'])
def shortest_path():
    if request.method == 'POST':
        start_building = request.form.get('start_building')
        end_building = request.form.get('end_building')

        distance = graph.get_distance(start_building, end_building)
        path = shortest_path_algorithm(start_building, end_building)

        return jsonify({'status': 'success', 'result': format_path_result(path, distance)})

    # If it's a GET request, you can handle it as needed
    return jsonify({'status': 'error', 'message': 'Invalid request'})

if __name__ == '__main__':
    app.run(debug=True)