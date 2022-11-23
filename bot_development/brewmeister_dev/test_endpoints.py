import pytest
import endpoints as ep

TEST_CLIENT = ep.app.test_client()

def testCryptoPrice():
    resp_json = TEST_CLIENT.get(ep.CRYPTOPRICE).get_json()
    assert isinstance(resp_json[ep.PRICE], float)
    