"""
This module encapsulates details about bot reviews.
"""
import db_connect as dbc
import user as usr
import bot_info as bi

COLLECTION = 'bot_reviews'
TEST_USER_NAME = 'Test User'
TEST_BOT_NAME = 'Brewmeister'
TEST_COMMENT = 'Test_comment'
TEST_RATING = 5
BOT_NAME = 'bot_name'
RATING = 'rating'
COMMENT = 'comment'
USERNAME = 'username'
REQUIRED_FLDS = [BOT_NAME, RATING, COMMENT, USERNAME]


def get_review(details):
    """
    Fetches one review from passed json argument from db
    """
    dbc.connect_db()
    return dbc.fetch_one(COLLECTION, details)


def review_exists(details):
    """
    Checks db to see if review exists from passed object
    """
    dbc.connect_db()
    review = dbc.fetch_one(COLLECTION, details)
    if review is not None:
        return True

    return False


def get_all_user_reviews(user):
    """
    Fetches all user reviews 
    """
    user_reviews = []
    data = get_all_reviews()

    for doc in data:
        if doc[USERNAME] == user:
            user_reviews.append((doc[BOT_NAME], doc[COMMENT]))

    return user_reviews


def get_all_bot_reviews(bot_name):
    """
    Fetches all bot reviews
    """
    bot_reviews = []
    data = get_all_reviews()

    for doc in data:
        if doc[BOT_NAME] == bot_name:
            bot_reviews.append((doc[USERNAME], doc[COMMENT]))

    return bot_reviews


def get_all_reviews():
    """
    Gets all reviews
    """
    dbc.connect_db()
    raw_data = dbc.fetch_all(COLLECTION)
    return raw_data


def create_review(details):
    """
    Creates a review from passed object
    """
    dbc.connect_db()
    user = details[USERNAME]
    bot_name = details[BOT_NAME]

    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')

    if usr.user_exists(user) and bi.bot_exists(bot_name):
        try:
            dbc.insert_one(COLLECTION, details)
            print("Successfully inserted into database")
        except Exception:
            print("ERROR: Unsuccessfully updated review in database.")
    else:
        print("ERROR: incorrect bot name or username")


def update_review(uname, bname, new_rev):
    """
    updates review given username, botname and new review
    """
    dbc.connect_db()
    if usr.user_exists(uname) and bi.bot_exists(bname):
        try:
            username = {USERNAME: uname, BOT_NAME: bname}
            comment = {'$set': {COMMENT: new_rev}}
            dbc.update_one(COLLECTION, username, comment)
            print("Successfully updated review in database.")
        except Exception:
            print("ERROR: Unsuccessfully updated review in database.")
    else:
        print("ERROR: incorrect bot name or username")


def delete_review(details):
    """
    Deletes a review
    """
    dbc.connect_db()
    if usr.user_exists(details[USERNAME]) and bi.bot_exists(details[BOT_NAME]):
        try:
            dbc.del_one(COLLECTION, details)
            print("Successfully deleted review")
        except Exception:
            print("ERROR: Unsuccessfully deleted into database.")
    else:
        print("ERROR: incorrect bot name or username")
