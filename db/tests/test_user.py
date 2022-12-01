import os

import pytest

import db.user as usr

def test_get_users():
    usrs = usr.get_users()
    assert isinstance(usrs, list)
    assert len(usrs) > 1