from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Welcome to the Environmental Impact Tracker!"

def calculate_impact(data):
    emission_factors = {
        'ICE(Internal Combustion Engines)': 0.411,
        'Diesel': 0.467,
        'Electric': 0.130, 
        'Hybrid': 0.356
    }
    
    vehicle_type = data.get('vehicle_type', 'Gasoline')
    
    if vehicle_type == 'Electric':
        # state-specific emission factors per mile for electric vehicles
        state_emission_modifiers = {
            'AL': 0.0916, 'AK': 0.1275, 'AZ': 0.0722, 'AR': 0.1128, 'CA': 0.0465,
            'CO': 0.1192, 'CT': 0.0581, 'DE': 0.1169, 'FL': 0.0889, 'GA': 0.0822,
            'HI': 0.1436, 'ID': 0.0331, 'IL': 0.0687, 'IN': 0.1708, 'IA': 0.0850,
            'KS': 0.0914, 'KY': 0.1893, 'LA': 0.1087, 'ME': 0.0508, 'MD': 0.0697,
            'MA': 0.0887, 'MI': 0.1184, 'MN': 0.0898, 'MS': 0.0960, 'MO': 0.1704,
            'MT': 0.1199, 'NE': 0.1297, 'NV': 0.0732, 'NH': 0.0319, 'NJ': 0.0555,
            'NM': 0.1041, 'NY': 0.0570, 'NC': 0.0729, 'ND': 0.1546, 'OH': 0.1255,
            'OK': 0.0748, 'OR': 0.0304, 'PA': 0.0770, 'RI': 0.0842, 'SC': 0.0597,
            'SD': 0.0376, 'TN': 0.0811, 'TX': 0.0963, 'UT': 0.1558, 'VT': 0.0,
            'VA': 0.0692, 'WA': 0.0219, 'WV': 0.2117, 'WI': 0.1278, 'WY': 0.1984
        }
       
  
        state = data.get('home_state', 'CA')
        emission_factor = state_emission_modifiers.get(state, emission_factors['Electric'])
        
    else:
        emission_factor = emission_factors.get(vehicle_type, 0.411)
        
    carbon_footprint = data['miles_driven'] * emission_factor
    return {"carbon_footprint": carbon_footprint}

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    result = calculate_impact(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
