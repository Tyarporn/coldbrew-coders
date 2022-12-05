"""
This module encapsulates details about user information.
"""
import db_connect as dbc

TEST_USER_NAME = 'Test User'
TEST_EMAIL = 'test@nyu.edu'
USERNAME = 'username'
PASSWORD = 'password'
EMAIL = 'email'
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
CART = 'cart'
COLLECTION = 'user'
REQUIRED_FLDS = [USERNAME, PASSWORD, EMAIL, FIRST_NAME, LAST_NAME, CART]


def user_exists(username):
    dbc.connect_db()
    user = dbc.fetch_one(COLLECTION, {USERNAME: username})
    if user is not None:
        return True

    return False


def get_users_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict('username', COLLECTION)


def get_user_details(username):
    dbc.connect_db()
    return dbc.fetch_one(COLLECTION, {'username': username})


def del_user(username):
    dbc.connect_db()
    if user_exists(username):
        dbc.del_one(COLLECTION, {USERNAME: username})


def create_user(details):
    dbc.connect_db()
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')

    dbc.insert_one(COLLECTION, details)


def update_user(username, new_pword):
    dbc.connect_db()
    if user_exists(username):
        dbc.update_one(COLLECTION, {USERNAME: username}, {'$set': {PASSWORD: new_pword}})


def get_users():
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('username', COLLECTION)
    return list(raw_data.keys())


def main():
    # doc = {
    #     USERNAME: TEST_USER_NAME,
    #     PASSWORD: "test2023",
    #     EMAIL: "test@nyu.edu",
    #     FIRST_NAME: "Test",
    #     LAST_NAME: "User",
    #     CART: {"Brewbot" : 0, "Brewmeister": 0, "CrisCo": 0, "Stonkster": 0}
    # }
    # create_user(doc)
    data = get_user_details(TEST_USER_NAME)
    print(data['email'])


if __name__ == '__main__':
    main()
