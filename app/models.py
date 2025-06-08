# app/models.py
from pydantic import BaseModel # create a class for the location and weather

class Location(BaseModel): # create a class for the location
    country: str
    city: str
    latitude: float
    longitude: float

class Weather(BaseModel): # create a class for the weather
    temperature: float
    description: str