import tweepy
from Crawler import Crawler

class TwitterCrawler(Crawler):
    """
    A class to represent twitter Crawler

    ...
    Attributes
    ----------
    Reddit : Object
        Initialize twitter Connection using tweepy

    Methods
    -------
    crawl():
        Crawl Singapore crimes related data from twitter.
    """
    def __init__(self, consumer_key, consumer_secret, access_token, token_secret):
        """
        Constructs all the necessary attributes for Tweepy a library to crawl from twitter, and initialize connection to twitter API

        Parameters
        ----------
            Consumer_Key: str
                The API key that twitter issues to the consumer
            Consumer_secret: str
                The password that is used to request access to twitter
            access_token: str
                is issued to the consumer by twitter to allow access priviledge
            token_secret
                is the access token secret that is use along with the access token 

        """
        consumer_key = "OrRuKndlEY6Xx3sOEuWaW3dPx"
        consumer_secret = "hwXN4qFNrCSRTy3k8tZWJ5uqJREGI8gJVDhpJj7YZ5Gs3PLfbL"
        access_token = "1368589570518831106-JNKPyMGTUgifprCjUJqFZoVa0NzOSx"
        access_token_secret = "Yqe9FSSawbubSLQdv7Skifbh02gVnmsXxRF3Xow2upl5U"    
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, token_secret)
        api = tweepy.API(auth)
        


    # Crawl function
    def crawl(self, db):
        """
        Crawl Singapore crimes related data from Twitter.

        Parameters
        ----------
        db: Database object
            Initialize connection to MySQL Database and inserting data

        Returns
        -------
        None
        """
        keys = "(charged OR jail OR arrested OR sentenced) AND singapore"
        for tweet in tweepy.Cursor(self.api.search, lang="en", q=keys+'-filter:retweets').items():
            db.insert("tweet", str(tweet.user.screen_name),
                str(tweet.text), tweet.favorite_count, tweet.created_at, tweet.retweet_count)
     