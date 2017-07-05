import pytest

from src.news import News
from src.news_errors import MenuException

@pytest.fixture
def news_client():
    return News()

# check initial attributes

def test__news_has_six_news_sources__equal(news_client):
    assert len(news_client.sources) == 6
    assert len(news_client.source_names) == 6

def test__news_sources_and_source_names_equal__succeeds(news_client):
    assert len(news_client.sources) == len(news_client.source_names)

def test__news_class_has_api_key__succeds():
    assert News.APIKEY is not None

# check setting news source

@pytest.mark.parametrize("not_int_input", ["3", 5.4, "", []])

def test__news_set_source__not_int_input__raises(news_client, not_int_input):
    with pytest.raises(MenuException):
        news_client.set_source(not_int_input)

@pytest.mark.parametrize("negative_or_above_5_int", [-3, -100, 6, 100])

def test__news_set_source__negative_or_above_5_input__raises(news_client, negative_or_above_5_int):
    with pytest.raises(MenuException):
        news_client.set_source(negative_or_above_5_int)