"""
This module encapsulates details about bot reviews.
"""
import db.db_connect as dbc
import user as usr

COLLECTION = 'bot_reviews'
BOT_NAME = 'bot_name'
RATING = 'rating'
COMMENT = 'comment'
USERNAME = 'username'
REQUIRED_FLDS = [BOT_NAME, RATING, COMMENT, USERNAME]


def create_review(details):
    dbc.connect_db()  
    user = details[USERNAME]

    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    
    if usr.user_exists(user):
        dbc.insert_one(COLLECTION, details)


def update_review():
    x=20


def delete_review():
    x=20


