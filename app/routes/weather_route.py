# app/routes/weather_route.py
from fastapi import APIRouter
from app.models import Location, Weather
from app.services.geolocation import get_location_by_ip
from app.services.weather import get_weather_by_location

router = APIRouter()

@router.get("/weather/{ip}")
async def get_weather(ip: str):
    location = await get_location_by_ip(ip)
    weather = await get_weather_by_location(location["latitude"], location["longitude"])
    return {"location": location, "weather": weather}