# app/services/geolocation.py
import httpx # make async requests
from app.config import GEO_API_KEY # call this from .env file

async def get_location_by_ip(ip: str):
    url = f"https://geo.ipify.org/api/v2/country,city?apiKey={GEO_API_KEY}&ipAddress={ip}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()