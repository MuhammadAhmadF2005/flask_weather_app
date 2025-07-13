from flask import Flask, render_template, request, jsonify
from weather import get_lat_lon, get_current_weather
import os
import requests

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
 
def index():
    data=None
    if request.method == 'POST':
        city=request.form['cityName']
        state=request.form['stateName']
        country=request.form['countryName']
        
        # Get API key from environment
        api_key = os.getenv('API_KEY')
        
        # First get coordinates
        lat, lon = get_lat_lon(city, state, country, api_key)
        
        # Then get weather data
        data = get_current_weather(lat, lon, api_key)

    return render_template('index.html', data=data)

@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('q', '')
    api_key = os.getenv('API_KEY')
    if not query or not api_key:
        return jsonify([])
    # Call OpenWeatherMap Geocoding API
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={api_key}'
    resp = requests.get(url)
    if resp.status_code != 200:
        return jsonify([])
    results = resp.json()
    suggestions = []
    for item in results:
        suggestions.append({
            'city': item.get('name', ''),
            'state': item.get('state', ''),
            'country': item.get('country', '')
        })
    return jsonify(suggestions)

# For Vercel deployment
app.debug = False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
