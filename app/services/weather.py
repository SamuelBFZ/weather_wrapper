# app/services/weather.py
import httpx
from app.config import WEATHER_API_KEY

async def get_weather_by_location(lat: float, lon: float):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()