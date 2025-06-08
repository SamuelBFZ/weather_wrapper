# weather_wrapper
## Description
Simplify IP-based weather queries through a single internal endpoint.

## Detailed Explanation.
This is an API Wrapper example to understand how a FastAPI is created.

## Endpoints
This aplication only will have an endpoint. This will be a method GET that will allow me to get the actual weather in my IP ubication.

## External APIs involved
 - **Name:** IP Geolocation
 - **Link:** geo.ipify.org 
 - **Authentication:** API Key.
 - **Return Data:** Country, City, Latitude and Longitude.

 - **Name:** OpenWeather
 - **Link:** openweathermap.org
 - **Authentication:** API Key
 - **Return Data:** Temperature, Climate, Humidity, etc.

## Wrapper Aut:
No authentication needed.

## Stack Used:
- **FastAPI:** Principal Framework.
- **httpx:** Async HTTP client.
- **Pydantic:** Model Validation.
- **dotenv:** Config manager.
- **uvicorn:** Development Server.