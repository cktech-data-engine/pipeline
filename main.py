import pandas
import requests
import dotenv
import yaml
import sqlalchemy
import streamlit
import json

from connectors.api import get_data
from storage.raw_storage import save_raw
from storage.trusted_storage import save_trusted
from projects.clima.transformations import transform_weather
url = "https://api.open-meteo.com/v1/forecast?latitude=-22.9068&longitude=-43.1729&current=temperature_2m"
dados = get_data(url)
save_raw(dados, "clima.json")
dados_transformados = transform_weather(dados)
save_trusted(dados_transformados, "clima_tratado.json")
print(dados_transformados)