import requests


def get_quote(currency):

    if currency == 'usd':
        return requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL').json()['USDBRL']['bid'][:4].replace('.',',')

    if currency == 'eur':
        return requests.get('https://economia.awesomeapi.com.br/json/last/EUR-BRL').json()['EURBRL']['bid'][:4].replace('.',',')

    if currency == 'btc':
        return requests.get('https://economia.awesomeapi.com.br/json/last/BTC-BRL').json()['BTCBRL']['bid']


def get_address(cep):
    pass
