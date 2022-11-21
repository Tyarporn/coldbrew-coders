"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""


def fetch_bot_id():
    """
    A function to return all discord bot ids in the data store.
    """
    return {"Brewbot": 1025852605257220106,
            "Brewmeister": 1234,
            "Stonkster": 2345,
            "CricSco": 3456
            }


def fetch_bot_description():
    """
    A function to return all discord bot descriptions in the data store.
    """
    return {"Brewbot": """Discord bot made for
                        CS-UY 4513 Software Engineering INET""",
            "Brewmeister": "Shashanka's tutorial bot",
            "Stonkster": "Yeehaw Cameron's cooking up a bot",
            "CricSco": "Get the latest cricket scores and fixtures!"
            }
