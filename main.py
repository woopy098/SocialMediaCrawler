from Database import Database
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler
host = "localhost"
password = "admin"
user = "root"
database = "sqldatabase"
consumer_key = "OrRuKndlEY6Xx3sOEuWaW3dPx"
consumer_secret = "hwXN4qFNrCSRTy3k8tZWJ5uqJREGI8gJVDhpJj7YZ5Gs3PLfbL"
access_token = "1368589570518831106-JNKPyMGTUgifprCjUJqFZoVa0NzOSx"
access_token_secret = "Yqe9FSSawbubSLQdv7Skifbh02gVnmsXxRF3Xow2upl5U"

print("Start")
db = Database(host,user,password,database)
db.createTable()
# rcrawl = RedditCrawler("Crimes", "zSqCr7ZeezCMgQ","-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
# rcrawl.crawl(db)
print("Tcrawl")
tcrawl = TwitterCrawler(consumer_key, consumer_secret,access_token, access_token_secret)
tcrawl.crawl(db)
# #db.read(10) #user able to set the limit that they want

# #keyword = "kill"
# #db.search(keyword)
db.disconnect()
