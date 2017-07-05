from src.news import News

if __name__ == "__main__":

    # initialize news client
    news = News()

    # ask for preferences
    print("""\nWelcome to Arnold's World News Portal!\nHere are the news publishers: \n""")

    print(news.show_news_sources())

    print("Which one would you like to read from?")

    news_source_choice = int(input("Choose number [1-6]: "))

    news.set_source(news_source_choice)

    print("How would you like to sort the articles?")
    print(news.show_news_sort_options())

    news_sort_method = int(input("Choose number [1-3]: "))

    print("Loading articles now....")

    news.fetch_news()

    print("Done!\n")

    print(news.show_news_articles())

    print("Enjoy your reading! ")

