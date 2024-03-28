import requests
import json

def pegaCotacoes(moeda, periodoMinutos, diasPassados):
    codigoMoeda = moeda + 'USDT'
    intervalo = periodoMinutos
    url = "https://api.binance.com/api/v3/klines?symbol=" + codigoMoeda + "&interval=" + intervalo

    req = requests.get(url)
    dados = json.loads(req.text)

    cotacoes = []
    for d in dados:
        cotacoes.append({"close":d[4]})
    return cotacoes

print(pegaCotacoes("BTC", "15m", None))