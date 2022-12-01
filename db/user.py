"""
This module encapsulates details about user information.
"""
import db_connect as dbc

TEST_USER_NAME = 'Test user'
USERNAME = 'username'
PASSWORD = 'password'
EMAIL = 'email'
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
CART = 'cart'
REQUIRED_FLDS = [USERNAME, PASSWORD, EMAIL, FIRST_NAME, LAST_NAME, CART]

def create_user(name, details):
    dbc.connect_db()
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
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

if __name__ == '__main__':
    main()

