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


<<<<<<< HEAD
# crawler = RedditCrawler("Crimes", "zSqCr7ZeezCMgQ",
#                         "-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
# crawler.crawl()
=======
    def crawl2(self):
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

#crawler = RedditCrawler("Shopping_habits", "zSqCr7ZeezCMgQ",
#                        "-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
#crawler.crawl()
>>>>>>> 6f5fa3125dd84511bb3f89f4f2580bd4cac3e3af
