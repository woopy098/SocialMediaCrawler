import tweepy
from Crawler import Crawler

class TwitterCrawler(Crawler):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        self.number_of_tweets = 1000

    # Crawl function
    def crawl(self, db):
        search_words = "(charged OR jail OR arrested OR sentenced) AND singapore -filters:retweets"
        for tweet in tweepy.Cursor(self.api.search, lang="en", q=search_words).items():
            db.insert("tweet", str(tweet.user.screen_name),
                str(tweet.text), tweet.favorite_count, tweet.created_at, tweet.retweet_count)