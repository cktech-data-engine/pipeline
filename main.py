from connectors.api_connector import fetch_weather_data
from storage.raw_storage import save_raw
from storage.trusted_storage import save_trusted
from projects.clima.transformations import transform_weather
from projects.clima.validator import validate_weather

dados = fetch_weather_data()
save_raw(dados, "clima.json")
dados_transformados = transform_weather(dados)

#Teste de validação dos dados transformados
#dados_invalidos = {
#    "data_hora": "2026-10-06T19:30",
#    "temperatura_c": "23.0"
#}

if validate_weather(dados_transformados):
    save_trusted(dados_transformados, "clima_tratado.json")
    print("Dados validados e salvos no TRUSTED")
else:
    print("Dados inválidos. O arquivo não foi salvo no TRUSTED.")