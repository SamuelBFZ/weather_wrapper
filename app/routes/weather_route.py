# app/routes/weather_route.py
from fastapi import APIRouter, Request
from app.services.geolocation import get_location_by_ip
from app.services.weather import get_weather_by_location

router = APIRouter()

@router.get("/location/{ip}")# get the location by ip
async def get_location(ip: str):
    location = await get_location_by_ip(ip)
    return location

@router.get("/weather/{ip}")# get the weather by location
async def get_weather(lat: float, lon: float):
    weather = await get_weather_by_location(lat, lon)
    return weather