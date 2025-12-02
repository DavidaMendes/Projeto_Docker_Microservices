import time
import requests

SERVER_URL = "http://server:8080/message"

for i in range(10):
    message = "mensagem de texto do client" + str(i)

    try:
        response = requests.post(SERVER_URL, json={"content": message})
        print(response.json())
    except Exception: 
        print("Erro ao enviar !")

    time.sleep(3)