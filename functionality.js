document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('impact-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        const milesDriven = document.getElementById('miles-driven').value;
        
        fetch('http://127.0.0.1:5000/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({miles_driven: parseFloat(milesDriven) || 0}),
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
