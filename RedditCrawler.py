import praw
from datetime import datetime
from Crawler import Crawler
from Database import Database
from SentimentAnalyzer import SentimentAnalyzer

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


    def crawl2(self):
        subreddit = self.reddit.subreddit("Singapore")
        newSubVaccine = subreddit.search("vaccine")
        for submission in newSubVaccine:
            comments = submission.comments.list()
            print("P: {} , Title: {} , ups: {} , downs: {} , Comments: {}".format(submission.id,
                                                                                  submission.title,
                                                                                  submission.ups,
                                                                                  submission.downs,
                                                                                  len(comments)))
            for comment in comments:
                text= comment.body
                print("Sentiment = ",str(SentimentAnalyzer.analyzeSentiment(text))," : ",text)





#crawler = RedditCrawler("Shopping_habits", "zSqCr7ZeezCMgQ",
#                        "-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
#crawler.crawl()