async function getWeatherByIP() {
    const ipInput = document.getElementById('ipInput');
    const resultContainer = document.getElementById('weatherResult');
    const ip = ipInput.value.trim();

    if (!ip) {
        showError('Please enter an IP address');
        return;
    }

    try {
        resultContainer.innerHTML = '<p>Loading...</p>';
        const response = await fetch(`/weather/${ip}`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'Failed to fetch weather data');
        }

        displayWeatherData(data);
    } catch (error) {
        showError(error.message);
    }
}

function displayWeatherData(data) {
    const resultContainer = document.getElementById('weatherResult');
    
    if (!data || !data.location || !data.weather) {
        showError('Invalid data received from server');
        return;
    }

    const location = data.location;
    const weather = data.weather;
    
    const html = `
        <div class="weather-info">
            <div class="weather-card">
                <h3>Location</h3>
                <p>City: ${location.city || 'N/A'}</p>
                <p>Region: ${location.region || 'N/A'}</p>
                <p>Country: ${location.country || 'N/A'}</p>
                <p>Coordinates: ${location.lat || 'N/A'}, ${location.lng || 'N/A'}</p>
            </div>
            <div class="weather-card">
                <h3>Weather</h3>
                <p>Temperature: ${weather.temperature || 'N/A'}°C</p>
                <p>Condition: ${weather.condition || 'N/A'}</p>
                <p>Humidity: ${weather.humidity || 'N/A'}%</p>
                <p>Wind Speed: ${weather.windSpeed || 'N/A'} km/h</p>
            </div>
        </div>
    `;
    
    resultContainer.innerHTML = html;
}

function showError(message) {
    const resultContainer = document.getElementById('weatherResult');
    resultContainer.innerHTML = `<div class="error">${message}</div>`;
} 