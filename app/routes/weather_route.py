# app/routes/weather_route.py
from fastapi import APIRouter
from app.services.geolocation import get_location_by_ip

router = APIRouter()

@router.get("/weather/{ip}")
async def get_weather(ip: str):
    location = await get_location_by_ip(ip)
    return location