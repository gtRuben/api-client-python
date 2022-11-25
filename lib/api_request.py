import requests


def get_quote(currency:str):

    if currency == 'usd':
        return requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL').json()['USDBRL']['bid'][:4].replace('.',',')

    if currency == 'eur':
        return requests.get('https://economia.awesomeapi.com.br/json/last/EUR-BRL').json()['EURBRL']['bid'][:4].replace('.',',')

    if currency == 'btc':
        return requests.get('https://economia.awesomeapi.com.br/json/last/BTC-BRL').json()['BTCBRL']['bid']


def get_address(cep:str):
    
    try:
        ads = requests.get(f'https://cdn.apicep.com/file/apicep/{cep[:5]}-{cep[5:]}.json').json()
        return True, f'\n\tCode: {ads["code"]}\n\tState: {ads["state"]}\n\tCity: {ads["city"]}\n\tDistrict: {ads["district"]}\n\tAddress: {ads["address"]}'

    except:
        return False, '\nAn error occurred. Try another CEP.'
