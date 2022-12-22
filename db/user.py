"""
This module encapsulates details about user information.
"""
import db_connect as dbc
import bot_info as bi

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


# delete test
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

    if user_exists(details[USERNAME]) is False:
        try:
            dbc.insert_one(COLLECTION, details)
            print("Sucessfully inserted into user database")
        except Exception:
            print("Unsucessfully inserted into user database")
    else:
        print("ERROR: User doesn't exist")


def delete_user(details):
    dbc.connect_db()
    if user_exists(details[USERNAME]):
        try:
            dbc.del_one(COLLECTION, details)
            print("Successfully deleted user")
        except Exception:
            print("ERROR: Unsuccessfully deleted user in database.")
    else:
        print("ERROR: User doesn't exist")


def update_user(un, p):
    dbc.connect_db()
    if user_exists(un):
        try:
            dbc.update_one(COLLECTION, {USERNAME: un}, {'$set': {PASSWORD: p}})
            print("Sucessfully updated user database")
        except Exception:
            print("Unsuccessfully updated user database")
    else:
        print("ERROR: User doesn't exist")


def update_cart(uname, bot):
    dbc.connect_db()
    if user_exists(uname):
        dbc.update_one(COLLECTION, {USERNAME: uname}, {'$push': {CART: bot}})
    else:
        print("ERROR: User doesn't exist")


def get_users():
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('username', COLLECTION)
    return list(raw_data.keys())


def add_to_cart(details, bot_name):
    dbc.connect_db()
    if user_exists(details[USERNAME]) and bi.bot_exists(bot_name):
        update_cart(details[USERNAME], bot_name)
    else:
        print("ERROR: User doesn't exist or bot doesn't exist")
