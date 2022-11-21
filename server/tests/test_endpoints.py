
import pytest

import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

def test_create_bot():
    resp_json = TEST_CLIENT.get(ep.CREATE).get_json()
    assert isinstance(resp_json[ep.CREATEBOTRESPONSE], str)


def test_list_bot():
    resp_json = TEST_CLIENT.get(ep.LIST).get_json()
    assert isinstance(resp_json[ep.LISTBOTS], list)


def test_show_bot_details():
    resp_json = TEST_CLIENT.get(ep.SHOWBOTDETAILS).get_json()
    assert isinstance(resp_json[ep.BOTMETADATA], list)

def test_delete_bot():
    resp_json = TEST_CLIENT.get(ep.DELETEBOT).get_json()
    assert isinstance(resp_json[ep.DELETEBOT], list)

def test_rate_bot():
    resp_json = TEST_CLIENT.get(ep.RATEBOT).get_json()
    assert isinstance(resp_json[ep.RATEBOT], list)
    
def test_review_bot():
    resp_json = TEST_CLIENT.get(ep.REVIEWBOT).get_json()
    assert isinstance(resp_json[ep.REVIEWBOT], list)
    
