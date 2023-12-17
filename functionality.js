document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('impact-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); 
        const milesDriven = document.getElementById('miles-driven').value;
        const vehicleType = document.getElementById('vehicle-type').value;
        const homeState = document.getElementById('home-state').value;
        
        fetch('http://127.0.0.1:5000/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                miles_driven: parseFloat(milesDriven) || 0,
                vehicle_type: vehicleType,
                home_state: homeState
            }),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = 
                'Carbon Footprint: ' + (data.carbon_footprint.toFixed(2) || 0) + ' kg CO2';
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById('result').innerHTML = 'An error occurred. Please try again.';
        });
    });
});
