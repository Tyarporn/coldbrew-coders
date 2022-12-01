"""
This module encapsulates details about user information.
"""
import db_connect as dbc

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

