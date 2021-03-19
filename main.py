import config as c
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from socialMediaObjectCreator import socialMedia
from Database import Database
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler
from GUI import GUI
import tweepy

print("Start")
db = Database(c.host, c.user, c.password, c.database)
reddit = RedditCrawler("Crimes", c.reddit_id, c.reddit_secret)
twitter = TwitterCrawler(c.consumer_key, c.consumer_secret, c.access_token, c.access_token_secret)
# obj = socialMedia(db, "reddit")
# print(obj.getCrimeScore())
ui = GUI(db, reddit, twitter)
ui.root.mainloop()
db.disconnect()
