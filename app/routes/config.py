# app/config.py
from dotenv import load_dotenv 
import os
load_dotenv() # load the .env file

GEO_API_KEY = os.getenv("GEO_API_KEY") # call this from .env file
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY") # call this from .env file