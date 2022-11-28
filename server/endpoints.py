"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api
# import db.db as db
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

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
MOVIEREVIEW = '/moviereview/<movie>'
MOVIEREVIEWRESPONSE = 'response'


@api.route(MOVIEREVIEW)
class MovieReview(Resource):
    def get(self, movie):

        nyt_api_1 = "https://api.nytimes.com/svc/movies/v2/"
        nyt_api_2 = "reviews/search.json?query="
        nyt_api_3 = "&api-key=ydFNAxCapwZOAgyxQ9cPIkacUTD8QnWx"

        try:
            url = nyt_api_1 + nyt_api_2 + movie + nyt_api_3
            response = requests.get(url)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

        return {MOVIEREVIEWRESPONSE: response.json()}


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
