import requests
import json
import matplotlib.pyplot as plt

moeda = "BTC"
intervalo = "1m"

# ------------------------------------- COTAÇÕES -----------------------------------------------------------

def pegaCotacoes(moeda, periodoMinutos, diasPassados):
    # Construir a URL para buscar os dados de cotação
    codigoMoeda = moeda + 'USDT'
    intervalo = periodoMinutos
    url = "https://api.binance.com/api/v3/klines?symbol=" + codigoMoeda + "&interval=" + intervalo

    # Fazer a requisição à API da Binance
    req = requests.get(url)
    dados = json.loads(req.text)
    return dados

# ------------------------------------- COTAÇÕES -----------------------------------------------------------

# ----------------------------------PROGRAMA PRINCIPAL -----------------------------------------------------------

while True:
    # Obtendo os dados de cotação
    dados = pegaCotacoes(moeda, intervalo, None)
    cotacoes = []
    lista_media_rapida = []
    lista_media_lenta = []
    
    # Processando os dados de cotação
    for d in dados:
        cotacoes.append(float(d[4]))  # Armazenando o preço de fechamento
        mediaRapida = sum(cotacoes[-8:]) / 8 # Calculando a média móvel rápida
        mediaLenta = sum(cotacoes[-21:]) / 21 # Calculando a média móvel lenta
        lista_media_rapida.append(mediaRapida)
        lista_media_lenta.append(mediaLenta)

    # Configuração do gráfico
    ag = plt.gca()
    ag.clear()
    plt.plot(cotacoes[-50:])  # Últimos 50 preços de fechamento
    plt.plot(lista_media_rapida[-50:], color="red")  # Últimos 50 valores da média móvel rápida
    plt.plot(lista_media_lenta[-50:], color="green")  # Últimos 50 valores da média móvel lenta
    plt.draw()

    # Atualização do gráfico a cada 5 segundos
    plt.pause(5)

# ----------------------------------PROGRAMA PRINCIPAL -----------------------------------------------------------
