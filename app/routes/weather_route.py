# app/routes/weather_route.py
from fastapi import APIRouter, Request
from app.services.geolocation import get_location_by_ip
from app.services.weather import get_weather_by_location

router = APIRouter()

@router.get("/location/{ip}")# get the location by ip
async def get_location(ip: str):
    location = await get_location_by_ip(ip)
    return location

@router.get("/weather/{ip}")
async def get_weather(ip: str):
    # Get location data
    location = await get_location_by_ip(ip)
    
    # Extract coordinates from location data
    lat = location["location"]["lat"]
    lng = location["location"]["lng"]
    
    # Get weather data
    weather = await get_weather_by_location(lat, lng)
    
    # Return combined data
    return {
        "location": location["location"],
        "weather": weather
    }