import os

import pytest

import db.reviews as rev


RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

TEST_REVIEW_NAME = 'Game to be deleted'

def test_get__all_user_reviews():
    user_revs = rev.get_all_user_reviews()
    assert isinstance(user_revs, list)

def test_get_bot_user_reviews():
    bot_revs = rev.get_all_bot_reviews()
    assert isinstance(bot_revs, list)

def test_get_all_reviews():
    all_revs = rev.get_all_reviews()
    assert isinstance(all_revs, list)

def test_create_review():
    details = {}
    TEST_USER = "test12"
    for field in rev.REQUIRED_FLDS:
        details[field] = 2
    details[rev.USERNAME] = TEST_USER
    rev.create_review(details)
    assert rev.review_exists(TEST_USER)
    rev.del_user(TEST_USER)

def test_update_review():
    

def test_delete_review():


