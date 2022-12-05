"""
This module encapsulates details about bot reviews.
"""
import db_connect as dbc
import user as usr

COLLECTION = 'bot_reviews'
TEST_USER_NAME = 'Test User'
BOT_NAME = 'bot_name'
RATING = 'rating'
COMMENT = 'comment'
USERNAME = 'username'
REQUIRED_FLDS = [BOT_NAME, RATING, COMMENT, USERNAME]

def get_all_reviews():
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('bot_name', COLLECTION)
    return raw_data


def create_review(details):
    dbc.connect_db()  
    user = details[USERNAME]

    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    
    if usr.user_exists(user): # check if bot exists here as well
        dbc.insert_one(COLLECTION, details)


def update_review():
    x=20


def delete_review():
    x=20


def main():
    # print(get_all_reviews())
    doc = {
        BOT_NAME: 'Brewmeister',
        RATING: 5,
        COMMENT: "sexy",
        USERNAME: "shakka boomboom"
    }
    create_review(doc)

if __name__ == '__main__':
    main()