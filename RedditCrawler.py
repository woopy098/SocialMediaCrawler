import praw
from Crawler import Crawler

class RedditCrawler(Crawler):
    def __init__(self, topic, clientId, secret):
        self.reddit = praw.Reddit(
            client_id= clientId,
            client_secret= secret,
            user_agent= topic,
        )

    def crawl(self):
        subreddit = self.reddit.subreddit('Singapore')
        for submission in subreddit.search("jail"):
            submission.comments.replace_more(limit=None)
            comment = submission.comments.list()
            print("P: {} , Title: {} , ups: {} , downs: {} , Comments: {}".format(submission.id,
                                                                                     submission.title,
                                                                                     submission.ups,
                                                                                     submission.downs,
                                                                                     len(comment)))
            # retrieve replies
            for c in comment:
                if len(comment) > 0:
                    print("R: {}, Text: {}".format(c.id, c.body))
                    # Here: run insertRow(c.id, c.body, c.author, c.created_utc)


crawler = RedditCrawler("Shopping_habits","zSqCr7ZeezCMgQ","-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
crawler.crawl()
