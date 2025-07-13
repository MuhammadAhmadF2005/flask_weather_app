# Flask Weather App

A simple weather application built with Flask that allows users to search for weather information by city, state, and country.

## Features

- Search weather by city, state, and country
- Autocomplete functionality for location search
- Real-time weather data from OpenWeatherMap API
- Responsive design with Bootstrap

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenWeatherMap API key as an environment variable:
   ```bash
   export API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Deployment on Vercel

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy the application:
   ```bash
   vercel
   ```

4. Set environment variables in Vercel dashboard:
   - Go to your project settings
   - Add `API_KEY` with your OpenWeatherMap API key

## Environment Variables

- `API_KEY`: Your OpenWeatherMap API key (required)

## API Dependencies

This application uses the OpenWeatherMap API for:
- Geocoding (converting city names to coordinates)
- Current weather data

Get your free API key at: https://openweathermap.org/api
