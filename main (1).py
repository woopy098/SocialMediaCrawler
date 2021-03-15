import Database as Database
from RedditCrawler import RedditCrawler

print("Start")
db = Database.javatest()
db.truncatetable()
crawler = RedditCrawler("Shopping_habits","zSqCr7ZeezCMgQ","-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
crawler.crawl()
db.disconnect()
#test.read()
#test.disconnect()

