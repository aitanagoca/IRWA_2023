import json
from myapp.analytics.analytics_data import AnalyticsData, ClickedDoc


class Document:
    def __init__(self, id, title, tweet, preprocessed_tweet, username, date, hashtags, likes, retweets, url):
        self.id = id
        self.title = title
        self.tweet = tweet
        self.preprocessed_tweet = preprocessed_tweet
        self.username = username
        self.date = date
        self.hashtags = hashtags
        self.likes = likes
        self.retweets = retweets
        self.url = url
        
    def to_json(self):
        return self.__dict__

    def __str__(self):
        """
        Print the object content as a JSON string
        """
        return json.dumps(self)


class StatsDocument:
    """
    Original corpus data as an object
    """

    def __init__(self, id, title, tweet, username, date, url, count, time_difference, rel_query, search_initiation_time, ip_address, os_info, browser):
        self.id = id
        self.title = title
        self.tweet = tweet
        self.username = username
        self.date = date
        self.url = url
        self.count = count
        self.time_difference = time_difference
        self.rel_query = rel_query
        self.search_initiation_time = search_initiation_time
        self.ip_address = ip_address
        self.os_info = os_info
        self.browser = browser

    def __str__(self):
        """
        Print the object content as a JSON string
        """
        return json.dumps(self)

    def update(self, new_count):
        self.count = new_count


class ResultItem:
    def __init__(self, id, title, tweet, username, date, likes, retweets, url, search_id, ranking):
        self.id = id
        self.title = title
        self.tweet = tweet
        self.username = username
        self.date = date
        self.likes = likes
        self.retweets = retweets
        self.url = url
        self.search_id = search_id
        self.ranking = ranking
