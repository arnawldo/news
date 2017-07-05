class NewsAppErrors(Exception):
    def __init__(self, message):
        self.message = message

class NoNewsException(NewsAppErrors):
    pass

class MenuException(NewsAppErrors):
    pass