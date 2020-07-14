import tweepy
import csv
import pandas as pd
import sys
import json
import collections

TWITTERPARSINGFIELDS = json.load(open('./config/twitter.json'))
TWITTERPARSINGFIELDS = [x['apifield'] for x in TWITTERPARSINGFIELDS]


def flatten(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


# API credentials here
ACCESS_TOKEN = "1175030158631346177-p7pCyWBwDoCgQMkb7LoI2AymUAtHXp"
ACCESS_TOKEN_SECRET = "3fUxB1VBpiModZnae6XfrqxwRQJXWlfQqsEAuogt75crd"
CONSUMER_KEY = "O6uTJJj1ECTvmCdNCQbCUbrge"
CONSUMER_SECRET = "u1k0F1iMNZXC0c6cUKnIQfySuoWZzn9Ig400xkjLVLaIEmgDJW"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Search word/hashtag value
HashValue = ""

# search start date value. the search will start from this date to the current date.
StartDate = ""

# getting the search word/hashtag and date range from user
# HashValue = input("Enter the hashtag you want the tweets to be downloaded for: ")
HashValue = "Carrefour"
# StartDate = input("Enter the start date in this format yyyy-mm-dd: ")
StartDate = "2020-07-01"


def scrap(hashtag=HashValue, startDate=StartDate, endDate="2020-12-31", limit=10):
    allTweets = tweepy.Cursor(api.search, q=HashValue, count=20,
                              lang="en", since=StartDate, tweet_mode='extended')
    allTweets = allTweets.items(max(limit, 10))
    allTweetsJson = [json.loads(json.dumps(tweet._json))
                     for tweet in allTweets]
    return allTweetsJson


def writeintocsv(_allTweetsJson, file_name, fields=TWITTERPARSINGFIELDS):
    # Open/Create a file to append data
    allTweetsJson = map(flatten, _allTweetsJson)
    with open(file_name, 'w+', newline='',encoding='UTF-8') as csvFile:
        # Use csv Writer
        f = csv.writer(csvFile)

        # Write CSV Header, If you dont need that, remove this line
        f.writerow(fields)
        for x in allTweetsJson:
            f.writerow([str(x.get(field, 'N/A')) for field in fields])
        return True
    return False
# print ("Scraping finished and saved to "+HashValue+".csv")
# sys.exit()
