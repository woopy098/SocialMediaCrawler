import Database as Database
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler

print("Start")
db = Database.Database()
# db.createTable()
db.createTable()
rcrawl = RedditCrawler("Crimes","zSqCr7ZeezCMgQ","-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
rcrawl.crawl(db)
tcrawl = TwitterCrawler()
tcrawl.crawl(db)
# #db.read(10) #user able to set the limit that they want

# #keyword = "kill"
# #db.search(keyword)
db.disconnect()