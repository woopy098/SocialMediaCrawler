import tweepy
from Crawler import Crawler
import csv
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
        csvFile = open('result.csv', 'a')
        csvWriter = csv.writer(csvFile)
        search_words = "charged singapore"
        # for tweet in self.api.search(q=search_words, tweet_mode='extended', count=1000):
        i = 0
        for t in self.api.search(geocode="1.3521,103.8198,7mi", tweet_mode="extended", q=search_words+'-filter:retweets'):
            csvWriter.writerow([t.full_text.encode(
                'utf-8'), t.favorite_count, t.created_at, str(t.user.screen_name), t.retweet_count])
            i += 1
        print("Total ", i)

        #     db.insert("tweet", str(tweet.user.screen_name), str(
        #         tweet.full_text), tweet.favorite_count, tweet.created_at, tweet.retweet_count)
        # db.disconnect()
crawler = TwitterCrawler()
crawler.crawl()
