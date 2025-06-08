# app/main.py
from fastapi import FastAPI
from app.routes.weather_route import router as weather_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Weather API"}

app.include_router(weather_router)