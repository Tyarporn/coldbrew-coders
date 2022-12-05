"""
This module encapsulates details about bot information.
"""
import db.db_connect as dbc

COLLECTION = 'bot_ids'
BOT_NAME = 'name'

def bot_exists(name):
    dbc.connect_db()
    bot = dbc.fetch_one(COLLECTION, {BOT_NAME: name})
    if bot is not None:
        return True

    return False

def get_bot_id():
    """
    A function to return all discord bot ids in the data store.
    """
    return {"Brewbot": 1025852605257220106,
            "Brewmeister": 1029079767443591220,
            "Stonkster": 1028785870163157082,
            "CricSco": 1039923876039237743
            }


def get_bot_names():
    """
    A funnction to return all the names of the bots in the data store.
    """
    return {"bot1": "Brewmeister",
            "bot2": "Stonkster",
            "bot3": "Brewbot",
            "bot4": "CricSco"
            }


def get_bot_description():
    """
    A function to return all discord bot descriptions in the data store.
    """
    return {"Brewbot": """Discord bot made for
                        CS-UY 4513 Software Engineering INET""",
            "Brewmeister": "Shashanka's tutorial bot",
            "Stonkster": "Yeehaw Cameron's cooking up a bot",
            "CricSco": "Get the latest cricket scores and fixtures!"
            }
