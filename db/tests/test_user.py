import os

import pytest

import db.user as usr

def test_get_users():
    usrs = usr.get_users()
    assert isinstance(usrs, list)
    assert len(usrs) > 1

def test_get_users_dict():
    usrs = usr.get_users_dict()
    assert isinstance(usrs, dict)
    assert len(usrs) > 1


def test_get_user_details():
    usr_dets = usr.get_user_details(usr.TEST_USER_NAME)
    assert isinstance(usr_dets, dict)


def test_create_wrong_details_type():
    with pytest.raises(TypeError):
        usr.create_user([])


def test_create_missing_field():
    with pytest.raises(ValueError):
        usr.create_user({'foo': 'bar'})


def test_create_user():
    details = {}
    TEST_USER = "test12"
    for field in usr.REQUIRED_FLDS:
        details[field] = 2
    details[usr.USERNAME] = TEST_USER
    usr.create_user(details)
    assert usr.user_exists(TEST_USER)
    usr.delete_user(details)


def test_update_user():
    details = {}
    TEST_USER = "test13"
    for field in usr.REQUIRED_FLDS:
        details[field] = 2
    details[usr.USERNAME] = TEST_USER
    usr.create_user(details)
    new_pword_test = "test2024"
    usr.update_user(TEST_USER, new_pword_test)
    data = usr.get_user_details(TEST_USER)
    assert data[usr.PASSWORD] == new_pword_test
    usr.del_user(TEST_USER)   
