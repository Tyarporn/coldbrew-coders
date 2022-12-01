import os

import pymongo as pm

import pytest

import db.db_connect as dbc

# RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

# TEST_DB = dbc.GAME_DB
# TEST_COLLECT = 'test_collect'
# # can be used for field and value:
# TEST_NAME = 'test'