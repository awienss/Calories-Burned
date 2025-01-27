from flask import Flask, render_template, request
import requests

# Initialize Flask
app = Flask(__name__)

# API Key and Base URL
API_KEY = '607Rzgq5PYjjaxPge59EVMhDUU2svjGdlmZCPx0Y'
BASE_URL = 'https://api.api-ninjas.com/v1/caloriesburned'

# Define routing
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        # Get form data
        activity = request.form.get('activity')
        weight = request.form.get('weight')
        duration = request.form.get('duration')

        # Validate input
        if not activity:
            error = 'Activity name is required.'
        else:
            try:
                weight = int(weight) if weight else None
                duration = int(duration) if duration else None

                # Build query parameters
                params = {'activity': activity}
                if weight:
                    params['weight'] = weight
                if duration:
                    params['duration'] = duration

                # Make API request
                headers = {'X-Api-Key': API_KEY}
                response = requests.get(BASE_URL, headers=headers, params=params)
                if response.status_code == 200:
                    result = response.json()
                else:
                    error = f"Error: {response.status_code} - {response.text}"
            except ValueError:
                error = 'Weight and duration must be numbers.'

    return render_template('index.html', result=result, error=error)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)