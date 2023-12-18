document.addEventListener('DOMContentLoaded', function() {
    const forms = {
        'impact-form': document.getElementById('impact-form'),
        'electronics-form': document.getElementById('electronics-form'),
        'utilities-form': document.getElementById('utilities-form')
    };
    let currentForm = 'impact-form';

    function showForm(formId) {
        // animate out the current form
        const currentFormEl = forms[currentForm];
        currentFormEl.style.opacity = '0';
        setTimeout(() => {
            currentFormEl.classList.add('form-hidden');
            currentFormEl.style.opacity = ''; // reset opacity for next time it shows
        }, 600); // this should match the CSS transition time

        // animate in the new form
        const newFormEl = forms[formId];
        setTimeout(() => {
            newFormEl.classList.remove('form-hidden');
            newFormEl.style.opacity = '0';
            setTimeout(() => {
                newFormEl.style.opacity = '1';
            }, 10); // a slight delay before starting the opacity transition
        }, 600); // wait for the old form to animate out before showing the new one

        currentForm = formId;
    }

    function previousForm() {
        // determine the previous form based on currentForm
        const formKeys = Object.keys(forms);
        const currentIndex = formKeys.indexOf(currentForm);
        const previousIndex = (currentIndex - 1 + formKeys.length) % formKeys.length;
        showForm(formKeys[previousIndex]);
    }

    function nextForm() {
        // determine the next form based on currentForm
        const formKeys = Object.keys(forms);
        const currentIndex = formKeys.indexOf(currentForm);
        const nextIndex = (currentIndex + 1) % formKeys.length;
        showForm(formKeys[nextIndex]);
    }

    // event listeners for the left and right navigation arrows
    document.querySelector('.arrow.left').addEventListener('click', previousForm);
    document.querySelector('.arrow.right').addEventListener('click', nextForm);

    // submit event for the main vehicle impact form
    forms['impact-form'].addEventListener('submit', function(event) {
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
                'Carbon footprint: ' + (data.carbon_footprint.toFixed(2) || 0) + ' kg CO2';
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById('result').innerHTML = 'An error occurred. Please try again.';
        });
    });

    // TODO: Implement logic for form submission
    forms['electronics-form'].addEventListener('submit', function(event) {
        event.preventDefault();
        //
        console.log('Submit electronics impact data');
        // update the result display as needed
    });

    // TODO: implement data handling and end-point
    forms['utilities-form'].addEventListener('submit', function(event) {
        event.preventDefault();
        // more submission logic here
        console.log('Submit utilities impact data');
        // update the result display as needed
    });
});
