"""
This module encapsulates details about user information.
"""
import db_connect as dbc


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
    user = dbc.fetch_one(COLLECTION, {'username': username})
    if user is not None:
        return False

    return True


def get_users_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict('username', COLLECTION)


def get_user_details(username):
    dbc.connect_db()
    return dbc.fetch_one(COLLECTION, {'username': username})


def del_user(username):
    dbc.connect_db()
    dbc.del_one(COLLECTION, {USERNAME: username})


def create_user(details):
    dbc.connect_db()
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')

    dbc.insert_one(COLLECTION, details)


def update_user(email, new_password):
    dbc.connect_db()
    dbc.update_one(COLLECTION, {EMAIL:email}, {'$set': {PASSWORD: new_password}})


def get_users():
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('username', COLLECTION)
    return list(raw_data.keys())


def main():
    users = get_users()
    print(users)
    # doc = {
    #     USERNAME: "cam",
    #     PASSWORD: "1231344",
    #     EMAIL: "ergrgrg13414",
    #     FIRST_NAME: "rgregerg123123",
    #     LAST_NAME: "ergergerg123213",
    #     CART: {"Brewbot" : 0}
    # }
    # create_user(doc)
    update_user('ergrgrg', 'ty123456')


if __name__ == '__main__':
    main()
