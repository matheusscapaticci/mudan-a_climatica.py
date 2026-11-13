import requests
import time
import datetime
from curiosidades import curiosidades
from dicas import dicas
from quiz import quiz

print("""
██████╗ ███████╗███╗   ███╗    ██╗   ██╗██╗███╗   ██╗██████╗  ██████╗
██╔══██╗██╔════╝████╗ ████║    ██║   ██║██║████╗  ██║██╔══██╗██╔═══██╗
██████╔╝█████╗  ██╔████╔██║    ██║   ██║██║██╔██╗ ██║██║  ██║██║   ██║
██╔══██╗██╔══╝  ██║╚██╔╝██║    ╚██╗ ██╔╝██║██║╚██╗██║██║  ██║██║   ██║
██████╔╝███████╗██║ ╚═╝ ██║     ╚████╔╝ ██║██║ ╚████║██████╔╝╚██████╔╝
╚═════╝ ╚══════╝╚═╝     ╚═╝      ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝
""")
print("Esse é um site sobre mudanças climáticas")

nome = input("Digite seu nome:")

print("""
- MENU -
-------------------
1. Curiosidades sobre mudanças climáticas
2. Dicas de como ajudar o planeta
3. Quiz sobre mudanças climáticas
4. Sair do site
""")

opcao = input("Escolha uma opção:")

if opcao == "1":
    curiosidades()
elif opcao == "2":
    dicas()
elif opcao == "3":
    quiz()
elif opcao == "4": 
    print("Saindo do site")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(2)
    print("Até mais tarde!")
else:
    print("Opção não existe")
