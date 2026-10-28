from connectors.api_connector import fetch_weather_data

def test_fetch_weather_data():
    dados = fetch_weather_data()

    assert isinstance(dados, dict)
    assert "current" in dados
