import Database as Database
from RedditCrawler import RedditCrawler
print("Start")

db = Database.Database()
list =db.read()
listLen=len(list)
print(len(list))
print(list[0][3])
# Key words to look for in subreddit
keywords = {"RAPE": 0, "SCAM": 0, "CYBERCRIME": 0, "DRUGS": 0, "FIREARM": 0, "ARSON": 0, "THEFT": 0, "TRAFFICKING": 0, "FRAUD": 0, "SEX OFFENCE": 0,
                    "SYNDICATE": 0, "MISAPPROPRIATION": 0, "MOLESTING": 0, "RIOT": 0, "JAILED": 0, "FINED": 0, "ROBBERY": 0, "MURDER": 0, "ASSAULT": 0, "PHISHING": 0, "ABUSE": 0}

print(type(list))
print(keywords)
for word in keywords:
    for row in list:
        if word in str(row[3]).upper():
            keywords[word]+=1
print(keywords)

#db.truncatetable()
# crawler = RedditCrawler("Shopping_habits","zSqCr7ZeezCMgQ","-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
# crawler.crawl()
# db.disconnect()

#test.read()
#test.disconnect()

