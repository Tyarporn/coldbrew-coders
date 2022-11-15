
import pytest

import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

def test_create_bot():
    resp_json = TEST_CLIENT.get(ep.CREATE).get_json()
    assert isinstance(resp_json[ep.CREATEBOTRESPONSE], str)

def test_list_bot():
    resp_json = TEST_CLIENT.get(ep.LIST).get_json()
    assert isinstance(resp_json[ep.LISTBOTS], list)


