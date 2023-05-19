import threading
import time
import tkinter as tk

import requests

api_key = "sua_chave_da_api"


def getWeather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    resposta = requests.get(url)
    data = resposta.json()

    if resposta.status_code == 200:
        weather = data["main"]["temp"]
        descript = data["weather"][0]["description"]
        celsius = weather - 273.15
        return f"Temperatura: {celsius:.2f}ºC\nDescrição: {descript}"
    else:
        return "Erro ao obter previsão do tempo"


def Att_weather():
    while atualizando.get():
        clima_atual = getWeather(cidade.get(), api_key)
        label_clima.config(text=clima_atual)
        time.sleep(5)


def stop_weather():
    atualizando.set(False)


janela = tk.Tk()
janela.title("Informações de Clima")
janela.geometry("300x200")

# Variáveis
atualizando = tk.BooleanVar()
atualizando.set(True)
cidade = tk.StringVar()


# Componentes
label_cidade = tk.Label(janela, text="Digite a cidade:")
label_cidade.pack()

entry_cidade = tk.Entry(janela, textvariable=cidade)
entry_cidade.pack()

label_clima = tk.Label(janela, text="Aguardando atualização...")
label_clima.pack()

button_parar = tk.Button(
    janela, text="Parar Atualização", command=stop_weather)
button_parar.pack()

# Iniciar thread de atualização do clima
thread_atualizacao = threading.Thread(target=Att_weather)
thread_atualizacao.start()

# Executar a interface gráfica
janela.mainloop()
