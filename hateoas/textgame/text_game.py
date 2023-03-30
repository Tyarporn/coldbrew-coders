from textapp.text_app import get_single_opt, URL, METHOD
from textapp.text_app import TYPE, DATA, RESPONSE
from textapp.text_app import FORM, MENU
from textapp.text_app import FLDS
import os
from http.client import OK
import requests
import sys
sys.path.append('../')


"""
This package provides a simple text interface to a GameAPI server.
It relies on the `text_menu` package, which is not yet on PyPi,
"""

MAIN_MENU_ROUTE = '/main_menu'
MENU_URL = ''
ROUTE = "/*"

CONTINUE = 1
HALT = 0
ERROR = -1

API_SERVER_URL = "GAME_API_URL"
LOCAL_HOST = "http://127.0.0.1:8080"

EXIT = 'x'

def run_menu(session, server, route=None, menu=None, form=None):
    """
    The caller must pass *either* `route` OR `menu`.
    """
    print(f"route = {server}{route}")
    status = ERROR
    try:
        if menu is None:
            menu_resp = session.get(f"{server}{route}")
            status = menu_resp.status_code
            menu = menu_resp.json()  # error here
    except Exception as e:
        print(str(e))
    if status != OK:
        return ERROR
    print(f'{menu=}')
    opt = get_single_opt(menu)
    # no URL means exit!
    if not opt.get(URL):
        return HALT

    if opt[METHOD] == 'get':
        result = session.get(f"{server}{opt[URL]}")
        if not result:
            print(f"Get method failed with code: {result.status_code}")
            exit(1)
        print(result.content)
        json_ret = result.json()
        if json_ret[TYPE] == "Route":
            print(json_ret["response"])
        elif json_ret[TYPE] == MENU:
            run_menu(session, server, menu=json_ret)
    elif opt[METHOD] == 'post':
        if form is None:
            print("Data to post missing from post method.")
            exit(1)
        print(f"Submitting {form[FLDS]}")
        session.post(f"{server}{opt[URL]}")
    return CONTINUE


def main():
    server = os.getenv(API_SERVER_URL, LOCAL_HOST)
    print(f"API server is {server}")
    session = requests.Session()
    cont = CONTINUE
    while cont == CONTINUE:
        cont = run_menu(session, server, route=MAIN_MENU_ROUTE)
    if cont == ERROR:
        return ERROR


if __name__ == "__main__":
    main()
