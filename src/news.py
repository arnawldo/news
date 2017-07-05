import requests

from src.news_errors import MenuException


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

    def set_source(self, menu_pos):
        """
        Select news source to fetch news from

        :param menu_pos: menu position selected corresponding to news source
        :type menu_pos: int
        :return: None
        """
        # check for incorrect input
        if type(menu_pos) is not int:
            raise MenuException("Invalid input")
        elif menu_pos < 1 or menu_pos >= len(self.sources):
            raise MenuException("Invalid input")

        # set source
        self.current_source = self.sources[menu_pos - 1]  # for zero-based indexing

    def set_sort_method(self, menu_pos):
        """
        Select sorting method for articles

        :param menu_pos: menu position to select sorting method
        :type menu_pos: int
        :return: None
        """
        # check for incorrect input
        if type(menu_pos) is not int:
            raise MenuException("Invalid input")
        elif menu_pos < 1 or menu_pos >= len(self.sort_by):
            raise MenuException("Invalid input")

        # set sort method
        self.current_sort = self.sort_by[menu_pos - 1]  # for zero-based indexing