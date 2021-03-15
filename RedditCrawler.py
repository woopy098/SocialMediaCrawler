import praw
from datetime import datetime
from Crawler import Crawler
from Database import Database


class RedditCrawler(Crawler):
    def __init__(self, topic, clientId, secret):
        self.reddit = praw.Reddit(
            client_id=clientId,
            client_secret=secret,
            user_agent=topic,
        )

    def crawl(self):
        db = Database()
        subreddit = self.reddit.subreddit('Singapore')
        for submission in subreddit.search("jail"):
            submission.comments.replace_more(limit=None)
            comment = submission.comments.list()
            print("P: {} , Title: {} , ups: {} , downs: {} , Comments: {}".format(submission.id,
                                                                                  submission.title,
                                                                                  submission.ups,
                                                                                  submission.downs,
                                                                                  len(comment)))
            db.insert(str(submission.id), str(submission.author), str(
                submission.title), datetime.utcfromtimestamp(submission.created_utc))
            # retrieve replies
            for c in comment:
                if len(comment) > 0:
                    db.insert(str(c.id), str(c.author), str(
                        c.body), datetime.utcfromtimestamp(c.created_utc))


        db.disconnect()


crawler = RedditCrawler("Shopping_habits", "zSqCr7ZeezCMgQ",
                        "-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
crawler.crawl()
