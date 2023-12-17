from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def calculate_impact(data):
    emission_factors = {
        'ICE(Internal Combustion Enines)': 0.411,
        'Diesel': 0.467,
        'Electric': 0.130,
        'Hybrid': 0.356
    }
    
    vehicle_type = data.get('vehicle_type', 'Gasoline')
    emission_factor = emission_factors.get(vehicle_type, 0.411)
    
    if vehicle_type == 'Electric':
        state_emission_modifiers = {
        'AL': 242.34,
        'AK': 124.27,
        'AZ': 229.91,
        'AR': 298.26,
        'AS': 0,
        'CA': 62.14,
        'CO': 273.4,
        'CT': 93.21,
        'DE': 217.48,
        'DC': 80.78,
        'FL': 205.05,
        'GA': 254.76,
        'GU': 0,
        'HI': 93.21,
        'ID': 43.5,
        'IL': 248.55,
        'IN': 341.76,
        'IA': 242.34,
        'KS': 316.9,
        'KY': 366.61,
        'LA': 316.9,
        'ME': 49.71,
        'MD': 136.7,
        'MA': 80.78,
        'MI': 279.62,
        'MN': 198.84,
        'MS': 304.47,
        'MO': 329.33,
        'MT': 236.12,
        'NE': 310.69,
        'NV': 142.92,
        'NH': 62.14,
        'NJ': 130.49,
        'NM': 192.63,
        'NY': 68.35,
        'NC': 248.55,
        'ND': 385.25,
        'MP': 0,
        'OH': 292.05,
        'OK': 329.33,
        'OR': 37.28,
        'PA': 236.12,
        'PR': 0,
        'RI': 111.85,
        'SC': 260.98,
        'SD': 192.63,
        'TN': 285.83,
        'TX': 267.19,
        'TT': 0,
        'UT': 229.91,
        'VT': 6.21,
        'VA': 242.34,
        'VI': 0,
        'WA': 18.64,
        'WV': 403.89,
        'WI': 242.34,
        'WY': 372.82,
    }
  
        state = data.get('home_state', 'CA')
        emission_factor *= state_emission_modifiers.get(state, 1)
        
        carbon_footprint = data['miles_driven'] * emission_factor
        return {"carbon_footprint": carbon_footprint}
                    
    carbon_footprint = data['miles_driven'] * 0.411  #Average CO2 emitted per mile by a passenger vehicle
    return {"carbon_footprint": carbon_footprint}

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    result = calculate_impact(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)