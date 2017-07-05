import pytest

from src.news import News

@pytest.fixture
def news_client():
    return News()

# check initial attributes

def test__news_has_six_news_sources__succeeds(news_client):
    assert len(news_client.sources) == 6
    assert len(news_client.source_names) == 6

