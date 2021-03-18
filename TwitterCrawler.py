import tweepy
from Crawler import Crawler

class TwitterCrawler(Crawler):
    def __init__(self, consumer_key, consumer_secret, access_token, token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    # Crawl function
    def crawl(self, db):
        keywords = "(charged OR jail OR arrested OR sentenced) AND singapore"
        for tweet in tweepy.Cursor(self.api.search, lang="en", q=keywords+'-filter:retweets').items():
            db.insert("tweet", str(tweet.user.screen_name),
                str(tweet.text), tweet.favorite_count, tweet.created_at, tweet.retweet_count)