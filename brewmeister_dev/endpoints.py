from header_files import *

def getCryptoPrice(symbol):
    url = f'{COIN_URL}/v2/cryptocurrency/quotes/latest?symbol={symbol}'
    parameters = {
    }

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COIN_API,
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        apiResponse = json.loads(response.text)

        price = apiResponse['data'][symbol][0]['quote']['USD']['price']

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    
    return price