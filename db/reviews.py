"""
This module encapsulates details about bot reviews.
"""
import db_connect as dbc
import user as usr
import bot_info as bi

COLLECTION = 'bot_reviews'
TEST_USER_NAME = 'Test User'
BOT_NAME = 'bot_name'
RATING = 'rating'
COMMENT = 'comment'
USERNAME = 'username'
REQUIRED_FLDS = [BOT_NAME, RATING, COMMENT, USERNAME]

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
    
    if usr.user_exists(user) and bi.bot_exists(bot_name): # check if bot exists here as well
        dbc.insert_one(COLLECTION, details)


def update_review(username, bot_name, new_review):
    dbc.connect_db()
    if usr.user_exists(username) and bi.bot_exists(bot_name):
        dbc.update_one(COLLECTION, {USERNAME: username, BOT_NAME: bot_name}, {'$set': {COMMENT: new_review}})


def delete_review(username, bot_name):
    dbc.connect_db()
    if usr.user_exists(username) and bi.bot_exists(bot_name): 
        dbc.del_one(COLLECTION, {USERNAME: username, BOT_NAME: bot_name})


def main():
    # print(get_all_reviews())
    # doc = {
    #     BOT_NAME: 'BrewBot',
    #     RATING: 5,
    #     COMMENT: "sexy",
    #     USERNAME: TEST_USER_NAME
    # }
    # create_review(doc)
    # update_review(TEST_USER_NAME, "Brewmeister", "great!")
    # delete_review(TEST_USER_NAME, "Brewmeister")
    print(get_all_user_reviews(TEST_USER_NAME))
    print(get_all_bot_reviews("Brewmeister"))

if __name__ == '__main__':
    main()