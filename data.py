from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def calculate_impact(data):
    carbon_footprint = data['miles_driven'] * 0.411  #Average CO2 emitted per mile by a passenger vehicle
    return {"carbon_footprint": carbon_footprint}

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    result = calculate_impact(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)