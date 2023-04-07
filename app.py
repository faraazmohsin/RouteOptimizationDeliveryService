from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("knn_model.pkl")

@app.route('/optimize_route', methods=['POST'])
def optimize_route():
    data = request.get_json()
    locations = data['locations']
    cluster_assignments = model.predict(locations)
    result = {'routes': cluster_assignments.tolist()}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)