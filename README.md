# Flask Weather App

A simple, interactive weather web app built with Flask and Bootstrap. Enter any city, state, and country in the world to get current weather conditions, with autocomplete suggestions for all fields.

## Features
- Search weather by city, state, and country (worldwide)
- Autocomplete suggestions for all location fields
- Clean, responsive Bootstrap UI
- Weather details: condition, description, temperature, and icon
- Remembers your last search in the form

## Setup Instructions

### 1. Clone the repository
```
git clone <repo-url>
cd flask_weather_app
```

### 2. Create and activate a virtual environment (optional but recommended)
```
python -m venv env
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Get an OpenWeatherMap API Key
- Sign up at [OpenWeatherMap](https://openweathermap.org/api) and get a free API key.

### 5. Create a `.env` file in the project root
```
API_KEY=your_openweathermap_api_key_here
```

## Running the App
```
python app.py
```
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Usage Notes
- Start typing in any of the location fields to see autocomplete suggestions. Click a suggestion to fill all fields.
- The app works for any city, state, and country supported by OpenWeatherMap.
- The UI is responsive and works on desktop and mobile.

## Dependencies
- Flask
- requests
- python-dotenv
- Bootstrap (via CDN)

---
**Enjoy your weather app!**
