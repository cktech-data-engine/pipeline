from projects.clima.validator import validate_weather


def test_dados_validos():

    dados = {
        "data_hora": "2026-10-06T19:30",
        "temperatura_c": 23.0
    }

    resultado = validate_weather(dados)
    assert resultado is True

def test_dados_invalidos():
    dados = {
        "data_hora": "2026-10-06T19:30",
        "temperatura_c": "23.0" 
    }

    resultado = validate_weather(dados)
    assert resultado is False

def test_temperatura_ausente():
    dados = {
        "data_hora": "2026-10-06T19:30"
    }
    resultado = validate_weather(dados)
    assert resultado is False