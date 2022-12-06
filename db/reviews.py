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

def review_exists(details):
    dbc.connect_db()
    review = dbc.fetch_one(COLLECTION, details)
    if review is not None:
        return True
    
    return False



def get_all_user_reviews(user):
    user_reviews = []
    data = get_all_reviews()

    for doc in data:
        if doc[USERNAME] == user:
            user_reviews.append((doc[BOT_NAME], doc[COMMENT]))
    
    return user_reviews

def get_all_bot_reviews(bot_name):
    bot_reviews = []
    data = get_all_reviews()

    for doc in data:
        if doc[BOT_NAME] == bot_name:
            bot_reviews.append((doc[USERNAME], doc[COMMENT]))
    
    return bot_reviews
    

def get_all_reviews():
    dbc.connect_db()
    raw_data = dbc.fetch_all(COLLECTION)
    return raw_data


def create_review(details):
    dbc.connect_db()  
    user = details[USERNAME]
    bot_name = details[BOT_NAME]

    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    
    if usr.user_exists(user) and bi.bot_exists(bot_name):
        dbc.insert_one(COLLECTION, details)


def update_review(username, bot_name, new_review):
    dbc.connect_db()
    if usr.user_exists(username) and bi.bot_exists(bot_name):
        dbc.update_one(COLLECTION, {USERNAME: username, BOT_NAME: bot_name}, {'$set': {COMMENT: new_review}})


def delete_review(details):
    dbc.connect_db()
    if usr.user_exists(details[USERNAME]) and bi.bot_exists(details[BOT_NAME]): 
        dbc.del_one(COLLECTION, details)


def main():

    # TEST_USER = "test12"
    # details = {
    #     BOT_NAME: TEST_BOT_NAME,
    #     RATING: TEST_RATING,
    #     COMMENT: TEST_COMMENT,
    #     USERNAME: TEST_USER
    # }
    # create_review(details)
    # print(get_all_reviews())
    # doc = {
    #     BOT_NAME: TEST_BOT_NAME,
    #     RATING: TEST_RATING,
    #     COMMENT: TEST_COMMENT,
    #     USERNAME: TEST_USER_NAME
    # }
    # create_review(doc)
    # # # update_review(TEST_USER_NAME, "Brewmeister", "great!")
    # delete_review(doc)
    # # print(get_all_user_reviews(TEST_USER_NAME))
    # # print(get_all_bot_reviews(TEST_BOT_NAME))
    # # details = {
    # #     BOT_NAME: TEST_BOT_NAME,
    # #     RATING: TEST_RATING,
    # #     COMMENT: TEST_COMMENT,
    # #     USERNAME: TEST_USER_NAME
    # # }
    # print(review_exists(doc))

if __name__ == '__main__':
    main()