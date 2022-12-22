import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()


@pytest.fixture
def review_api_value():
    test_value = "godfather"
    return test_value


@pytest.fixture
def coin_api_value():
    test_value = "BTC"
    return test_value


@pytest.fixture
def news_value():
    test_value = "nyu"
    return test_value


@pytest.mark.skip(reason="not implemented yet in main endpoints file")
def testCryptoPrice(coin_api_value):
    resp_json = TEST_CLIENT.get(ep.CRYPTOPRICE).get_json()
    assert isinstance(resp_json[ep.PRICE], dict)


def test_news_api_call(news_value):
    resp_json = TEST_CLIENT.get(f'{ep.NEWS}/{news_value}').get_json()
    print(resp_json)
    assert isinstance(resp_json, dict)


def test_review_api_call(review_api_value):
    resp_json = TEST_CLIENT.get(f'{ep.MOVIERW}/{review_api_value}').get_json()
    print(resp_json)
    assert isinstance(resp_json, dict)


def test_list_bot():
    resp_json = TEST_CLIENT.get(ep.LIST).get_json()
    assert isinstance(resp_json[ep.LISTBOTS], list)


def test_show_bot_details():
    resp_json = TEST_CLIENT.get(ep.SHOWBOTDETAILS).get_json()
    assert isinstance(resp_json[ep.BOTMETADATA], dict)


def test_create_review():
    resp_json = TEST_CLIENT.get(ep.CREATEREVIEW).get_json()
    assert isinstance(resp_json[ep.CREATEREVIEWRESPONSE], str)


def test_delete_review():
    resp_json = TEST_CLIENT.get(ep.DELETEREVIEW).get_json()
    assert isinstance(resp_json[ep.DELETERESPONSE], str)


def test_update_review():
    resp_json = TEST_CLIENT.get(ep.UPDATEREVIEW).get_json()
    assert isinstance(resp_json[ep.UPDATERESPONSE], str)


def test_create_user():
    resp_json = TEST_CLIENT.get(ep.CREATEUSER).get_json()
    assert isinstance(resp_json[ep.NEWUSERRESPONSE], str)


def test_update_users():
    resp_json = TEST_CLIENT.get(ep.UPDATEUSER).get_json()
    assert isinstance(resp_json[ep.UPDATEUSERRESPONSE], str)


def test_delete_users():
    return


def test_list_users():
    resp_json = TEST_CLIENT.get(ep.SHOWUSERS).get_json()
    assert isinstance(resp_json[ep.USERLIST], dict)


def test_update_cart():
    return
