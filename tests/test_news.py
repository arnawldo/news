import pytest

from src.news import News

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

