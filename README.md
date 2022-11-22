# _Twitter Scrapper with Telegram Bot_ 🤖


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


Twitter Scraper to scrape Follower username and Follower user Url.
Sends Information of Followers on Telegram Channel.

- python3
- selenium4
- webdriver Manager
- Telebot
- Telethon
- ✨Magic ✨


## Features

- Auto logins to your Twitter Account.
- Scrap all your followers usernames and thier urls.
- Export your followers info in a .CSV file named as followers.
- when run afterwards it will automatically create new followers file that will contain the required info of the new followers in a separate csv file.
- sends new Followers info to Telegram Channel.
- Runs After every 6 hours
## Installation

This Scrapper requires [python](https://www.python.org/) v10+ to run.
``` bash
pip install -r requirements.txt
```
Edit credential.txt
replace username and password with your twitter username & password present in the credentials.txt
```
username
password
```
run initial.py
``` bash
python initial.py
```
this will create a csv file which contains all the records.

after this you can run final.py to know info about new followers.
``` bash
python final.py
```
This will create a csv file named "new_followers.csv" which contains all the new_followers that you got and it will also append new followers to the followers.csv.
## License

MIT


Powered by:
![N|Solid](https://cdn.iconscout.com/icon/free/png-64/python-2-226051.png)

