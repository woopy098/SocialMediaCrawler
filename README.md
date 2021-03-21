# 1009CrawlOOP
Lab P3 OOP Project
## Installation
### PRAW
PRAW is supported on Python 3.6+. The recommended way to install is via pip:
```
pip install praw
```
Visit https://praw.readthedocs.io/en/latest/getting_started/installation.html for detailed installation step.
### Tweepy
The easiest way to install is by using pip:
```
pip install tweepy
```
Visit https://docs.tweepy.org/en/latest/install.html for detailed installation steps.
### NLTK
Install NLTK by running pip:
```
pip install nltk
python
>>> import nltk
>>> nltk.download('vader_lexicon')
```
### matplotlib
The graph plot feature is designed using matplotlib interface. Install via pip:
```
pip install matplotlib
```
Visit https://matplotlib.org/stable/users/installing.html for detailed installation guide.
### tkinter
The UI interface is designed using tkinter python interface. Running ```python -m tkinter``` from command line will let you know whether it is properly installed.
Install via pip:
```
pip install tkinter
```
Visit https://docs.python.org/3/library/tkinter.html for detailed installation guide.
### MySQL Connector
Install MySQL Connector by running pip:
```
pip install mysql-connector-python
```
Visit https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html for detailed installation step.
### Database
Install MySQL installer Community:
```
https://dev.mysql.com/downloads/installer/
```
Visit https://www.sqlshack.com/how-to-install-mysql-database-server-8-0-19-on-windows-10/ for detailed installation step

## Configuration
### Reddit Authentication
Visit https://github.com/reddit-archive/reddit/wiki/OAuth2 for detailed guide on how to register and get the credentials.
### Twitter Authentication
Visit for detailed guide on how to register and get the credentials.
### Database
Create Database credentials:
Visit https://www.sqlshack.com/how-to-install-mysql-database-server-8-0-19-on-windows-10/ again on how to create a database.
Take note of your localhost, user, password and database name for the below configuration.
### config.py
Before you run python program, make sure to change the configuration to your credentials in ```config.py```:
```
# Database credentials
host = ""
password = ""
user = ""
database = ""

# Reddit credentials
reddit_id = ""
reddit_secret = ""

# Twitter credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
```
## Run Program
Once the configuration is done. Run the program where the file is located via:
```
python ./main.py
```
Remember that data in the database and the table is not found.
Press the crawl button first and wait 5 to 10 mins to finish crawling data from Reddit and Twitter.
Make sure that configuration is correct or else the program will not run.
