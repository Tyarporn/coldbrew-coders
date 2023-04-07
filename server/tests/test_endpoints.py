import pytest
import server.endpoints as ep
import db.reviews as rev
import db.user as usr
# import db.bot_info as bi

TEST_CLIENT = ep.app.test_client()


@pytest.fixture
def movie_value():
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

@pytest.fixture
def books_value():
    test_value = "title=the+midnight+library"
    return test_value


@pytest.mark.skip(reason="not implemented yet in main endpoints file")
def testCryptoPrice(coin_api_value):
    resp_json = TEST_CLIENT.get(ep.CRYPTOPRICE).get_json()
    assert isinstance(resp_json[ep.PRICE], dict)


def test_news_api_call(news_value):
    resp_json = TEST_CLIENT.get(f'{ep.NEWS}/{news_value}').get_json()
    print(resp_json)
    assert isinstance(resp_json, dict)


def test_movie_api_call(movie_value):
    resp_json = TEST_CLIENT.get(f'{ep.MOVIERW}/{movie_value}').get_json()
    print(resp_json)
    assert isinstance(resp_json, dict)


def test_book_api_call(books_value):
    resp_json = TEST_CLIENT.get(f'{ep.BOOKRW}/{books_value}').get_json()
    print(resp_json)
    assert isinstance(resp_json, dict)


def test_list_bot():
    resp_json = TEST_CLIENT.get(ep.LIST).get_json()
    assert isinstance(resp_json[ep.LISTBOTS], list)


def test_show_bot_details():
    resp_json = TEST_CLIENT.get(ep.SHOWBOTDETAILS).get_json()
    assert isinstance(resp_json[ep.BOTMETADATA], dict)


TEST_REVIEW = {
    rev.BOT_NAME: rev.TEST_BOT_NAME,
    rev.RATING: rev.TEST_RATING,
    rev.COMMENT: rev.TEST_COMMENT,
    rev.USERNAME: rev.TEST_USER_NAME,
}


def test_create_review():
    TEST_CLIENT.post(ep.CREATEREVIEW, json=TEST_REVIEW)
    assert rev.review_exists(TEST_REVIEW)
    rev.delete_review(TEST_REVIEW)


TEST_USER = {
    usr.USERNAME: usr.TEST_USER_NAME,
    usr.PASSWORD: "testPassword",
    usr.EMAIL: "test@gmail.com",
    usr.FIRST_NAME: "test",
    usr.LAST_NAME: "user",
    usr.CART: []
}


def test_create_user():
    TEST_CLIENT.post(ep.CREATEUSER, json=TEST_USER)
    assert usr.user_exists(TEST_USER[usr.USERNAME])
    usr.delete_user(TEST_USER)


def test_list_users():
    resp_json = TEST_CLIENT.get(ep.SHOWUSERS).get_json()
    assert isinstance(resp_json[ep.USERLIST], dict)


# @pytest.mark.skip(reason="home not returning json")
def test_route_home():
    resp = TEST_CLIENT.get(ep.HOME).get_json()
    print(resp)
    assert isinstance(resp, dict)


def test_route_discover():
    resp = TEST_CLIENT.get(ep.DISCOVER).get_json()
    assert isinstance(resp, dict)


def test_route_about():
    resp = TEST_CLIENT.get(ep.ABOUT).get_json()
    assert isinstance(resp, dict)


def test_route_contact():
    resp = TEST_CLIENT.get(ep.CONTACT).get_json()
    assert isinstance(resp, dict)


def test_route_login():
    resp = TEST_CLIENT.get(ep.LOGIN).get_json()
    assert isinstance(resp, dict)
