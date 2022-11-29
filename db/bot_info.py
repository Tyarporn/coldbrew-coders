"""
This module encapsulates details about bot information.
"""
import db.db_connect as dbc

def get_bot_id():
    """
    A function to return all discord bot ids in the data store.
    """
    return {"Brewbot": 1025852605257220106,
            "Brewmeister": 1234,
            "Stonkster": 2345,
            "CricSco": 3456
            }

def get_bot_names():
    return {"bot1": "Brewmeister",
            "bot2": "Stonkster"
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
