import os
import json
from dotenv import load_dotenv
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


load_dotenv()
COIN_API = os.getenv('COINMARKETCAP_API_KEY')
COIN_URL = os.getenv('CMC_URL')


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
