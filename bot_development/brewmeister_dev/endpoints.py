import os
import json
from dotenv import load_dotenv
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from flask import Flask
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app)


CRYPTOPRICE = '/getcryptoprice/<symbol>'


load_dotenv()
COIN_API = os.getenv('COINMARKETCAP_API_KEY')
COIN_URL = os.getenv('CMC_URL')
PRICE = 'crypto_price'


@api.route(CRYPTOPRICE)
class CryptoPrice(Resource):

    def get(self, symbol):

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

            cprice = apiResponse['data'][symbol][0]['quote']['USD']['price']

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

        return {PRICE: round(cprice, 2)}
        # return {PRICE: apiResponse["data"]}
