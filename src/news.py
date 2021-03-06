import requests

from src.news_errors import MenuException, NoNewsException


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

    def show_news_sources(self):
        """
        Show menu of news sources

        :return: None
        """
        menu = "\n"

        for i, source in enumerate(self.source_names):
            menu += "{pos}. {name} \n".format(pos=str(i + 1), name=source)

        return menu

    def show_news_sort_options(self):
        """
        Show methods of sorting the articles

        :return: None
        """
        menu = "\n"

        for i, method in enumerate(self.sort_by):
            menu += "{pos}. {name} \n".format(pos=str(i + 1), name=method)

        return menu


    def show_news_articles(self):
        """Show news stories"""

        # check if news has been fetched
        if len(self.articles) == 0:
            raise NoNewsException("News has not been fetched yet!")

        # pretty print news stories
        stories = "News from: " + self.current_source + "-" * 100 + "\n\n"
        for article in self.articles:
            stories += "TITLE: {}\n\n".format(article["title"])
            stories += "STORY: {}\n\n".format(article["description"])
            stories += "AUTHOR: {}\n\n".format(article["author"])
            stories += "-" * 50 + "\n\n"

        return stories

    def fetch_news(self):
        """
        Access news from newsapi.org API

        :return:
        """
        new_api = ("https://newsapi.org/v1/articles?source={source}&sortBy={sort_method}&apiKey={apikey}"
                   .format(source=self.current_source,
                           sort_method=self.current_sort,
                           apikey=News.APIKEY))

        request = requests.get(new_api)
        self.articles = request.json()["articles"]