import requests

def curiosidades():
    print("Curiosidades sobre mudanças climáticas!")

resposta = requests.get("URL_DA_API")

dados = resposta.json()

print(dados)
