import requests

class News(object):
    """Class for handling fetching and displaying top news around the world"""

    APIKEY = "0146694de85d497187e35ae93a7bafdf"

    def __init__(self):
        self.sources = ["associated-press", "techcrunch", "bbc-news", "cnn", "bbc-sport", "al-jazeera-english"]
        self.source_names = ["Associated Press", "TechCrunch", "BBC", "CNN", "BBC Sport", "Al Jazeera English"]
        self.sort_by = ["top", "latest", "popular"]
        self.current_source = self.sources[0]
        self.current_sort = self.sort_by[0]
        self.articles = []