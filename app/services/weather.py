# app/services/weather.py
import httpx
from app.config import WEATHER_API_KEY

async def get_weather_by_location(lat: float, lon: float):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
        # Transform the data into our expected format
        return {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "windSpeed": data["wind"]["speed"]
        }