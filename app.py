from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load and process simulation data
data = pd.read_csv('simulation_results.csv')
avg_latency = data['latency'].mean()

@app.route('/')
def index():
    return render_template('index.html', avg_latency=avg_latency)

@app.route('/data')
def data():
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
