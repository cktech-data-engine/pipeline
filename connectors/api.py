import requests #Pega os dados da API


def get_data(url): #Função genérica para reutilização
    response = requests.get(url) #Requisição de resposta da API
    response.raise_for_status()  #Interrompe a execução se houver algum erro na requisição
    return response.json() #O dado vira uma estrutura manipulável em python