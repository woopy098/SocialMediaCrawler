import tweepy
from Crawler import Crawler
# import csv
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
        # csvFile = open('result.csv', 'a')
        # csvWriter = csv.writer(csvFile)
        search_words = ["charged", "singapore"]
        for t in self.api.search(q=search_words, tweet_mode='extended', count=1000):
            # csvWriter.writerow([t.full_text.encode(
            #     'utf-8'), t.favorite_count, t.created_at, str(t.user.screen_name), t.retweet_count])
            db.insert("tweet", str(t.user.screen_name), str(
                t.full_text), t.favorite_count, t.created_at, t.retweet_count)
        db.disconnect()


crawler = TwitterCrawler()
crawler.crawl()
