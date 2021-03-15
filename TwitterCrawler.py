import tweepy
from Crawler import Crawler
from Database import Database
consumer_key = "OrRuKndlEY6Xx3sOEuWaW3dPx"
consumer_secret = "hwXN4qFNrCSRTy3k8tZWJ5uqJREGI8gJVDhpJj7YZ5Gs3PLfbL"
access_token = "1368589570518831106-JNKPyMGTUgifprCjUJqFZoVa0NzOSx"
access_token_secret = "Yqe9FSSawbubSLQdv7Skifbh02gVnmsXxRF3Xow2upl5U"


class TwitterCrawler(Crawler):
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
        self.number_of_tweets = 1000
    # Crawl function

    def crawl(self):
        db = Database()
        for t in tweepy.Cursor(self.api.user_timeline, id="straits_times", tweet_mode="extended").items(self.number_of_tweets):
            # print("Text: {}\n Likes: {}\n Date: {}\n User: {}\n Retweet count: {}".format(
            #     t.full_text, t.favorite_count, t.created_at, t.user.screen_name, t.retweet_count))
            db.insert("tweet", str(t.user.screen_name), str(t.full_text), t.favorite_count, t.created_at, t.retweet_count)
        db.disconnect()

#crawler = TwitterCrawler()
#crawler.crawl()