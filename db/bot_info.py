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
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('name', COLLECTION)
    result = {}
    for key, value in raw_data.items():
        result[key] = value['bot_id']

    return result


def get_bot_names():
    """
    A function to return all the names of the bots in the data store.
    """
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('name', COLLECTION)
    return list(raw_data.keys())


def get_bot_descs():
    """
    A function to return all discord bot descriptions in the data store.
    """
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('name', COLLECTION)
    result = {}

    for key, value in raw_data.items():
        result[key] = value['bot_description']

    return result
