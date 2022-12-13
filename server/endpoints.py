"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
import os
import requests
import db.bot_info as bi
import db.reviews as rev
import db.user as usr
from flask import Flask
from flask_restx import Resource, Api
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv


app = Flask(__name__)
api = Api(app)


LIST = '/listbots'
LISTBOTS = 'bot_list'
SHOWBOTDETAILS = '/showdetails'
SHOWBOTIDS = '/showbotids'
BOTIDS = 'bot_ids'
BOTMETADATA = 'bot_metadata'


RATEBOT = '/rate'
RATEBOTRESPONSE = 'response'
SHOWREVIEW = '/showreview'
REVIEW = 'reviews'
CREATEREVIEW = '/review'
CREATEREVIEWRESPONSE = 'response'
DELETEREVIEW = '/delete'
DELETERESPONSE = 'response'
UPDATEREVIEW = '/update'
UPDATERESPONSE = 'response'

CREATEUSER = '/create_user'
NEWUSERRESPONSE = 'response'
SHOWUSERS = '/show_users'
USERLIST = 'user_list'
UPDATEUSER = '/update_user'
UPDATEUSERRESPONSE = 'response'


MOVIERW = '/moviereview'
MOVIERWRESPONSE = 'response'
NEWS = '/news'
NEWSRESPONSE = 'response'


CRYPTOPRICE = '/crypto'
CRYPTOPRICERESPONSE = 'response'

load_dotenv()
COIN_API = os.getenv('COINMARKETCAP_API_KEY')
COIN_URL = os.getenv('CMC_URL')
PRICE = 'crypto_price'


@api.route(f'{CRYPTOPRICE}/<symbol>')
class CryptoPrice(Resource):
    pass


@api.route(f'{MOVIERW}/<movie_name>')
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

        return {MOVIERWRESPONSE: response.json()}


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


@api.route(LIST)
class ListBot(Resource):

    def get(self):
        return {LISTBOTS: bi.get_bot_names()}


@api.route(SHOWBOTDETAILS)
class ShowBotDetails(Resource):

    def get(self):
        return {BOTMETADATA: bi.get_bot_descs()}


@api.route(SHOWBOTIDS)
class ShowBotIDs(Resource):

    def get(self):
        return {BOTIDS: bi.get_bot_ids()}


@api.route(SHOWREVIEW)
class ShowReview(Resource):
    def get(self):
        return {REVIEW: rev.get_all_reviews()}

@api.route(CREATEREVIEW)
class CreateReview(Resource):
    def get(self):
        return {CREATEREVIEWRESPONSE: "Post Successful"}


@api.route(DELETEREVIEW)
class DeleteReview(Resource):
    def get(self):
        return {DELETERESPONSE: "Post Successful"}


@api.route(UPDATEREVIEW)
class UpdateReview(Resource):
    def get(self):
        return {UPDATERESPONSE: "Post Successful"}


@api.route(CREATEUSER)
class CreateUser(Resource):
    def get(self):
        return {NEWUSERRESPONSE: "Post Successful"}


@api.route(SHOWUSERS)
class UserList(Resource):
    def get(self):
        return {USERLIST: usr.get_users_dict()}


@api.route(UPDATEUSER)
class UpdateUser(Resource):
    def get(self):
        return {UPDATEUSERRESPONSE: "Post Successful"}


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
