import os

import pytest

import db.bot_info as bi


RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)


def test_get_bot_id():
    bot_ids = bi.get_bot_ids()
    assert isinstance(bot_ids, dict)
    assert len(bot_ids) == 4

def test_get_bot_names():
    bot_names = bi.get_bot_names()
    assert isinstance(bot_names, list)
    assert len(bot_names) == 4

def test_get_bot_descs():
    bot_descs = bi.get_bot_descs()
    assert isinstance(bot_descs, dict)
    assert len(bot_descs) == 4