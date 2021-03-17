import Database as Database
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler

print("Start")

#db.createTable()
#db.truncatetable()
#db.createTable()
crawler = RedditCrawler("Shopping_habits","zSqCr7ZeezCMgQ","-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
crawler.crawl2()
#tcrawl = TwitterCrawler()
#tcrawl.crawl()
#db.read(10) #user able to set the limit that they want

#keyword = "kill"
#db.search(keyword)
#db.disconnect()
print("end")


