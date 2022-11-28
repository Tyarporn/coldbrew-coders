"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api
# import db.db as db
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import os

app = Flask(__name__)
api = Api(app)

CREATE = '/create'
CREATEBOTRESPONSE = 'response'
LIST = '/listbots'
LISTBOTS = 'bot_list'
SHOWBOTDETAILS = '/showdetails'
BOTMETADATA = 'bot_metadata'
DELETEBOT = '/delete'
DELETEBOTRESPONSE = 'response'
RATEBOT = '/rate'
RATEBOTRESPONSE = 'response'
REVIEWBOT = '/review'
REVIEWBOTRESPONSE = 'response'
UPDATEBOT = '/update'
UPDATEBOTRESPONSE = 'response'
MOVIEREVIEW = '/moviereview'
MOVIEREVIEWRESPONSE = 'response'
CRYPTOPRICE = '/crypto'
CRYPTOPRICERESPONSE = 'response'
NEWS = '/news'
NEWSRESPONSE = 'response'


load_dotenv()
COIN_API = os.getenv('COINMARKETCAP_API_KEY')
COIN_URL = os.getenv('CMC_URL')
PRICE = 'crypto_price'


@api.route(f'{CRYPTOPRICE}/<symbol>')
class CryptoPrice(Resource):
    pass


@api.route(f'{MOVIEREVIEW}/<movie_name>')
class MovieReview(Resource):
    def get(self, movie_name):

        nyt_api_1 = "https://api.nytimes.com"
        nyt_api_2 = "/svc/movies/v2/reviews/search.json?query="
        nyt_api_3 = "&api-key=ydFNAxCapwZOAgyxQ9cPIkacUTD8QnWx"

        try:
            url = nyt_api_1 + nyt_api_2 + movie_name + nyt_api_3
            response = requests.get(url)
            print(response.json())

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

        return {MOVIEREVIEWRESPONSE: response.json()}


@api.route(f'{NEWS}/<keyword>')
class News(Resource):
    def get(self, keyword):
        nyt_api_1 = "https://api.nytimes.com"
        nyt_api_2 = "/svc/search/v2/articlesearch.json?q="
        nyt_api_3 = "&api-key=ydFNAxCapwZOAgyxQ9cPIkacUTD8QnWx"
        try:
            url = nyt_api_1 + nyt_api_2 + keyword + nyt_api_3
            response = requests.get(url)
            print(response.json())

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

        return {NEWSRESPONSE: response.json()}


@api.route(CREATE)
class CreateBot(Resource):

    def get(self):
        return {CREATEBOTRESPONSE: "POST successful"}


@api.route(LIST)
class ListBot(Resource):

    def get(self):
        return {LISTBOTS: ["brewmeister", "brewbot", "crisco", "stonkster"]}


@api.route(SHOWBOTDETAILS)
class ShowBotDetails(Resource):

    def get(self):
        return {BOTMETADATA: ["#1234", "#1222", "#1221", "1223"]}


@api.route(DELETEBOT)
class DeleteBot(Resource):
    def get(self):
        return {DELETEBOTRESPONSE: "Post Successful"}


@api.route(RATEBOT)
class RateBot(Resource):
    def get(self):
        return {RATEBOTRESPONSE: "Post Successful"}


@api.route(REVIEWBOT)
class ReviewBot(Resource):
    def get(self):
        return {REVIEWBOTRESPONSE: "Post Successful"}


@api.route(UPDATEBOT)
class UpdateBot(Resource):
    def get(self):
        return {UPDATEBOTRESPONSE: "Post Successful"}


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = ''
        # sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}
