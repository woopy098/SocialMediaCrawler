import praw
from datetime import datetime
from Crawler import Crawler
from Database import Database


class RedditCrawler(Crawler):
    """
    A class to represent Reddit Crawler

    ...
    Attributes
    ----------
    
    """
    def __init__(self, topic, clientId, secret):
        self.reddit = praw.Reddit(
            client_id=clientId,
            client_secret=secret,
            user_agent=topic,
        )

    def crawl(self):
        db = Database()
        subreddit = self.reddit.subreddit('Singapore')
        for post in subreddit.search("jail"):
            post.comments.replace_more(limit=None)
            comment = post.comments.list()
            # insert posts
            db.insert("post", str(post.author), str(post.title), str(post.score),
                      datetime.utcfromtimestamp(post.created_utc), len(comment))
            # insert comments
            # for c in comment:
            # db.insert("comment", str(c.body), str(c.score), str(
            #     c.author), datetime.utcfromtimestamp(c.created_utc))
        db.disconnect()

#crawler = RedditCrawler("Crimes", "zSqCr7ZeezCMgQ",
#                        "-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
#crawler.crawl()