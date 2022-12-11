"""
This module encapsulates details about bot information.
"""
import db.db_connect as dbc


COLLECTION = 'bot_ids'
BOT_NAME = 'name'
BOT_ID = 'id'
BOT_DESC = 'desc'
REQUIRED_FLDS = [BOT_NAME, BOT_ID, BOT_DESC]


def bot_exists(name):
    dbc.connect_db()
    bot = dbc.fetch_one(COLLECTION, {BOT_NAME: name})
    if bot is not None:
        return True

    return False

def get_bot_ids():
    """
    A function to return all discord bot ids in the data store.
    """
    # return {"Brewbot": 1025852605257220106,
    #         "Brewmeister": 1029079767443591220,
    #         "Stonkster": 1028785870163157082,
    #         "CricSco": 1039923876039237743
    #         }
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('id', COLLECTION)
    return list(raw_data.keys())

def get_bot_names():
    """
    A funnction to return all the names of the bots in the data store.
    """
    # return ["Brewmeister", "Brewbot", "CrisCo", "Stonkster"]
    dbc.connect_db()
    return dbc.fetch_all_as_dict('name', COLLECTION)
    return list(raw_data.keys())


def get_bot_descs():
    """
    A function to return all discord bot descriptions in the data store.
    """
    # return {"Brewbot": """Discord bot made for
    #                     CS-UY 4513 Software Engineering INET""",
    #         "Brewmeister": "Shashanka's tutorial bot",
    #         "Stonkster": "Yeehaw Cameron's cooking up a bot",
    #         "CricSco": "Get the latest cricket scores and fixtures!"
    #         }
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('desc', COLLECTION)
    return list(raw_data.keys())
