import requests
BASE_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather_data():
    response = requests.get(
        BASE_URL, 
        params={
            "latitude": -22.9068, 
            "longitude": -43.1729, 
             "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "precipitation,"
            "wind_speed_10m,"
            "weather_code"
        ),
        "timezone": "America/Sao_Paulo"
        },
        timeout=10
    )

    response.raise_for_status()
    dados = response.json()
    return dados
