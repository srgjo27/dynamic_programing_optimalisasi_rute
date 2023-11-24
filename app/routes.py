from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    start_building = request.form['start_building']
    end_building = request.form['end_building']

    # Tempatkan logika pencarian rute disini

    result = f"Rute dari {start_building} ke {end_building} akan ditampilkan di sini."
    return render_template('index.html', result=result)
