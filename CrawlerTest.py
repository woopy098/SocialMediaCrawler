import config as c
import unittest
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler
from Database import Database

class CrawlerTest(unittest.TestCase):
    def testInvalidRedditAuthentication(self):
        r = RedditCrawler("crimes","id","secret")
        self.assertRaises(Exception, r.crawl(db=None))
    
    def testInvalidTwitterAuthentication(self):
        t = TwitterCrawler("wrong_key","wrong_secret","wrong_token","wrong_tokensecret")
        self.assertRaises(Exception, t.crawl(db=None))
        
    def test_DatabaseConnection(self):
        self.assertTrue(Database(c.host, c.user, c.password,
                                 c.database))

if __name__ == '__main__':
    unittest.main()