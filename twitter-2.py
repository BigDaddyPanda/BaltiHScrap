import tweepy
import csv
import pandas as pd
import sys
import json

# API credentials here
ACCESS_TOKEN = "1175030158631346177-p7pCyWBwDoCgQMkb7LoI2AymUAtHXp"
ACCESS_TOKEN_SECRET = "3fUxB1VBpiModZnae6XfrqxwRQJXWlfQqsEAuogt75crd"
CONSUMER_KEY = "O6uTJJj1ECTvmCdNCQbCUbrge"
CONSUMER_SECRET = "u1k0F1iMNZXC0c6cUKnIQfySuoWZzn9Ig400xkjLVLaIEmgDJW"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Search word/hashtag value 
HashValue = ""

# search start date value. the search will start from this date to the current date.
StartDate = ""

# getting the search word/hashtag and date range from user
# HashValue = input("Enter the hashtag you want the tweets to be downloaded for: ")
HashValue = "Carrefour"
# StartDate = input("Enter the start date in this format yyyy-mm-dd: ")
StartDate = "2020-07-01"

# Open/Create a file to append data
csvFile = open(HashValue+'.csv', 'a')

#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=HashValue,count=20,lang="en",since=StartDate, tweet_mode='extended').items(2):
    print (json.dumps(tweet._json))
    break

# print ("Scraping finished and saved to "+HashValue+".csv")
#sys.exit()
