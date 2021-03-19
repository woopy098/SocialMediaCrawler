from Database import Database
from RedditCrawler import RedditCrawler
from socialMediaObjectCreator import socialMedia
from TwitterCrawler import TwitterCrawler

host = "localhost"
password = "password"
user = "root"
database = "sqldatabase"
consumer_key = "OrRuKndlEY6Xx3sOEuWaW3dPx"
consumer_secret = "hwXN4qFNrCSRTy3k8tZWJ5uqJREGI8gJVDhpJj7YZ5Gs3PLfbL"
access_token = "1368589570518831106-JNKPyMGTUgifprCjUJqFZoVa0NzOSx"
access_token_secret = "Yqe9FSSawbubSLQdv7Skifbh02gVnmsXxRF3Xow2upl5U"





print("Start")
db = Database(host,user,password,database)
# db.createTable()
# rcrawl = RedditCrawler("Crimes", "zSqCr7ZeezCMgQ","-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
# rcrawl.crawl(db)
# tcrawl = TwitterCrawler(consumer_key, consumer_secret,access_token, access_token_secret)
# tcrawl.crawl(db)
# readReddit= readDatabase(db,"reddit")
# print("REDDIT SENTIMENT = ",readReddit.readSentiment())

twitterObject= socialMedia(db,"twitter")
print("\treadTwitter")
print("Twitter Sentiment score  :",twitterObject.getSentimentScore())
print("Twitter Sentiment        :",twitterObject.getSentiment())
print("Twitter Crime Count      :",twitterObject.getCrimeScore())

print("\n\n")
redditObject= socialMedia(db,"reddit")
print("\treadReddit")
print("Reddit Sentiment score  :",redditObject.getSentimentScore())
print("Reddit Sentiment        :",redditObject.getSentiment())
print("Reddit Crime Count      :",redditObject.getCrimeScore())



# #keyword = "kill"
# #db.search(keyword)
db.disconnect()
