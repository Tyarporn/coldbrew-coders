"""
This module encapsulates details about user information.
"""
import db_connect as dbc

TEST_USER_NAME = 'Test user'
NAME = 'name'
EMAIL = 'email'
FULL_NAME = 'full_name'

# We expect the user database to change frequently:
# For now, we will consider EMAIL to be
# our mandatory fields.
REQUIRED_FLDS = [EMAIL]
users = {TEST_USER_NAME: {EMAIL: 'x@y.com', FULL_NAME: 'Porgy Tirebiter'},
         'handle': {EMAIL: 'z@y.com', FULL_NAME: 'Nick Danger'}}
def create_user():
    x = 20


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

