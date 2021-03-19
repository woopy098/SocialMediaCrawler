import config as c
import unittest
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler
from Database import Database

class CrawlerTest(unittest.TestCase):
    def test_DatabaseConnection(self):
        print("Test Database Connection..")
        self.assertTrue(Database(c.host, c.user, c.password,
                                 c.database))

    def test_RedditConnection(self):
        print("Test Reddit Connection...")
        self.assertTrue(RedditCrawler("crimes", c.reddit_id,
                                      c.reddit_secret))

    def test_TwitterConnection(self):
        print("Test Twitter Connection...")
        self.assertTrue(TwitterCrawler(c.consumer_key, c.consumer_secret,
                                       c.access_token, c.access_token_secret))

if __name__ == '__main__':
    unittest.main()