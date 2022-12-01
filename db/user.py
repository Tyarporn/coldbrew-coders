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
REQUIRED_FLDS = [USERNAME, PASSWORD, EMAIL, FIRST_NAME, LAST_NAME, CART]

def create_user(details):
    dbc.connect_db()
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')

    dbc.insert_one('user', details)


def update_user():
    x=20


def get_users():
    dbc.connect_db()
    raw_data = dbc.fetch_all_as_dict('username', 'user')
    return list(raw_data.keys())


def main():
    users = get_users()
    print(users)
    doc = {
        USERNAME: "cam",
        PASSWORD: "1231344",
        EMAIL: "ergrgrg13414",
        FIRST_NAME: "rgregerg123123",
        LAST_NAME: "ergergerg123213",
        CART: {"Brewbot" : 0}
    }
    create_user(doc)


if __name__ == '__main__':
    main()

