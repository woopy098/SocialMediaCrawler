import config as c
from Database import Database
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler

print("Start")
db = Database(c.host, c.user, c.password, c.database)
db.createTable()
# rcrawl = RedditCrawler("Crimes", c.reddit_id, c.reddit_secret)
# rcrawl.crawl(db)
tcrawl = TwitterCrawler(c.consumer_key, c.consumer_secret,
                        c.access_token, c.access_token_secret)
tcrawl.crawl(db)
db.disconnect()