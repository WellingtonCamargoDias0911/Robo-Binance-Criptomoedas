import requests
import json
import matplotlib.pyplot as plt

moeda = "BTC"
intervalo = "1m"

def pegaCotacoes(moeda, periodoMinutos, diasPassados):
    codigoMoeda = moeda + 'USDT'
    intervalo = periodoMinutos
    url = "https://api.binance.com/api/v3/klines?symbol=" + codigoMoeda + "&interval=" + intervalo

    req = requests.get(url)
    dados = json.loads(req.text)
    return dados

while True:
    dados = pegaCotacoes(moeda, intervalo, None)
    cotacoes = []
    lista_media_rapida = []
    lista_media_lenta = []
    for d in dados:
        cotacoes.append(float(d[4]))
        mediaRapida = sum(cotacoes[-8:]) / 8
        mediaLenta = sum(cotacoes[-21:]) / 21
        lista_media_rapida.append(mediaRapida)
        lista_media_lenta.append(mediaLenta)


    ag = plt.gca()
    ag.clear()
    plt.plot(cotacoes[-50:])
    plt.plot(lista_media_rapida[-50:], color="red")
    plt.plot(lista_media_lenta[-50:], color="green")
    plt.draw()

    plt.pause(5)
