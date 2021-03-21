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
### Database
1)proceed to https://dev.mysql.com/downloads/installer/
2)download mysql-installer-community-8.0.x.0.msi . (x represent the number of the latest version)
3)run the mysql-installer and select developer default for Setup type.
4)At check requirements, select Next. It will prompt one or more product requirements have not been satisfied, select yes to continue.
5)review the list of software/products that are going to be installed and click on execute.
6)Wait for a few mins, select next to start configuring MySQL database server.
7)under product configuration, it will show the list of product that need to be configure.
8)for default setting, click on next till you are required to enter your root password for MySQL. set your password and click next.
9)execute to apply the configuration and do a test connection to the server by providing the 'root' username and the password you set previously and select check to ensure you are connected.
10)select next till installation is completed.

### Connection to MySQL Server
1)make sure MySQL80 is runnning on services.msc
1.1)if you are unsure of step1, press win+R key to open run window and type services.msc. under the services window locate MySQL80, right click it and select start.
2)open MySQL workbench, at the welcome screen you will see a local instance MySQL80.
3)select it and type in 'root' with your password.
4)under Query, type in CREATE DATABASE sqldatabase , and execute query.
----------------------OPTIONAL----------------------------------------
5)once the query is executed, you will be able to see the new database under 'SCHEMAS'.
6)double click on sqldatabase to set it as the default schemas.
7)Go to file and select open SQL script.
8)locate the script named sqldatabase_crawleddata.sql and execute it.
