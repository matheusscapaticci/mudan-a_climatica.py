import requests

def dicas():
    print("Dicas para ajudar o planeta!")

resposta = requests.get("URL_DA_API")

dados = resposta.json()

print(dados)
