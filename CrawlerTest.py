import config as c
import unittest
#from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler
#from Database import Database


class CrawlerTest(unittest.TestCase):
   # def test_RedditConnection(self):
        #self.assertTrue(RedditCrawler("crimes", c.reddit_id,
                                     # c.reddit_secret), "Connection Fail")

    def test_TwitterConnection(self):
        self.assertTrue(TwitterCrawler(c.consumer_key, c.consumer_secret,
                                       c.access_token, c.access_token_secret),"Connection Fail")

    #def test_DatabaseConnection(self):
       # self.assertTrue(Database(c.host, c.user, c.password,
                                 #c.database), "Connection Fail")

if __name__ == '__main__':
    unittest.main()