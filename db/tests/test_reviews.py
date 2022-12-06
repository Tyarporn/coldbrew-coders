import os

import pytest

import db.reviews as rev


RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

TEST_REVIEW_NAME = 'Game to be deleted'

def test_get_review():
    details = {
        rev.BOT_NAME: rev.TEST_BOT_NAME,
        rev.RATING: rev.TEST_RATING,
        rev.COMMENT: rev.TEST_COMMENT,
        rev.USERNAME: rev.TEST_USER_NAME
    }
    rev_dets = rev.get_review(details)
    assert isinstance(rev_dets, dict)

def test_get__all_user_reviews():
    user_revs = rev.get_all_user_reviews(rev.TEST_USER_NAME)
    assert isinstance(user_revs, list)

def test_get_bot_user_reviews():
    bot_revs = rev.get_all_bot_reviews(rev.TEST_USER_NAME)
    assert isinstance(bot_revs, list)

def test_get_all_reviews():
    all_revs = rev.get_all_reviews()
    assert isinstance(all_revs, list)

def test_create_review():
    TEST_USER = "test12"
    details = {
        rev.BOT_NAME: rev.TEST_BOT_NAME,
        rev.RATING: rev.TEST_RATING,
        rev.COMMENT: rev.TEST_COMMENT,
        rev.USERNAME: TEST_USER
    }
    rev.create_review(details)
    assert rev.review_exists(details)
    rev.delete_review(details)

def test_update_review():
    new_review = "YURRRRRRRRRRRR"
    rev.update_review(rev.TEST_USER_NAME, rev.TEST_BOT_NAME, new_review)

    new_details = { 
        rev.BOT_NAME: rev.TEST_BOT_NAME,
        rev.RATING: rev.TEST_RATING,
        rev.COMMENT: new_review,
        rev.USERNAME: rev.TEST_USER_NAME
    }
    data = rev.get_review(new_details)
    assert data[rev.COMMENT] == new_review
    rev.update_review(rev.TEST_USER_NAME, rev.TEST_BOT_NAME, rev.TEST_COMMENT)  



