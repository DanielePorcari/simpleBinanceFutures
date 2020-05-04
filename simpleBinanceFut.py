#Porcari Daniele https://danieleporcaripython.blogspot.com
#Simple Binance Futures API for Python
import requests
import json

def fbin_ultimo_prezzo(coppia):
    coppia=coppia.upper()
    indirizzo='https://fapi.binance.com/fapi/v1/ticker/price?symbol='+coppia
    r=requests.get(indirizzo)
    file=r.text
    prezzo=json.loads(file)
    return prezzo['price']

def fbin_book(coppia):
    coppia=coppia.upper()
    indirizzo='https://fapi.binance.com/fapi/v1/depth?symbol='+coppia
    r=requests.get(indirizzo)
    file=r.text
    return json.loads(file)

def fbin_candlestick(coppia,intervallo,limite):
    coppia=coppia.upper()
    indirizzo='https://fapi.binance.com/fapi/v1/klines?symbol='+coppia+'&interval='+intervallo+'&limit='+limite
    r=requests.get(indirizzo)
    file=r.text
    return json.loads(file)

def fbin_prezzomercato(coppia):
    coppia=coppia.upper()
    indirizzo='https://fapi.binance.com//fapi/v1/premiumIndex?symbol='+coppia
    r=requests.get(indirizzo)
    file=r.text
    return json.loads(file)

def fbin_24h_statisticheprezzo(coppia):
    coppia=coppia.upper()
    if coppia=='NONE':
        indirizzo='https://fapi.binance.com/fapi/v1/ticker/24hr'
    else:
        indirizzo='https://fapi.binance.com/fapi/v1/ticker/24hr?symbol='+coppia
    r=requests.get(indirizzo)
    file=r.text
    return json.loads(file)

def fbin_book_migliorprezzo(coppia):
    coppia=coppia.upper()
    indirizzo='https://fapi.binance.com//fapi/v1/ticker/bookTicker?symbol='+coppia
    r=requests.get(indirizzo)
    file=r.text
    return json.loads(file)
