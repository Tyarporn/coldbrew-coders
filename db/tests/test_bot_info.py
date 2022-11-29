import os

import pytest

import db.bot_info as bi


RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)


def test_bot_id(bot_name):
    bot_ids = bi.get_bot_id()
    assert isinstance(bot_ids, dict)
    assert len(bot_ids) == 4
    
