"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api
# import db.db as db

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
