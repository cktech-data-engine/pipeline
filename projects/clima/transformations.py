#receber o JSON que veio da API e retornar somente time e temperature_2m, com nomes mais claros.
def transform_weather(data):
    current = data.get("current")
    transformed_data = {
        "data_hora": current.get("time"),
        "temperatura_c": current.get("temperature_2m")
    }
    return transformed_data