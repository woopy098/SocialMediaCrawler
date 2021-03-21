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
Install MySQL installer:
```
https://dev.mysql.com/downloads/installer/
```
Visit https://www.sqlshack.com/how-to-install-mysql-database-server-8-0-19-on-windows-10/ for detailed installation step

## Configuration & Run Program
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
