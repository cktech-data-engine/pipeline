def validate_weather(data):
    data_hora = data.get("data_hora")
    temperatura = data.get("temperatura_c")
    if data_hora is not None and temperatura is not None and isinstance(temperatura, (int, float)):
        return True
    return False