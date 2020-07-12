# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:40:59 2020

@author: asus
"""

# YouTube Video: https://www.youtube.com/watch?v=wlnx-7cm4Gg
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
#import twitter_credentials
ACCESS_TOKEN = "1175030158631346177-p7pCyWBwDoCgQMkb7LoI2AymUAtHXp"
ACCESS_TOKEN_SECRET = "3fUxB1VBpiModZnae6XfrqxwRQJXWlfQqsEAuogt75crd"
CONSUMER_KEY = "O6uTJJj1ECTvmCdNCQbCUbrge"
CONSUMER_SECRET = "u1k0F1iMNZXC0c6cUKnIQfySuoWZzn9Ig400xkjLVLaIEmgDJW"
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["covid", "confinement"]
    fetched_tweets_filename = r"C:\Users\ky94\Desktop\BaltiH\tweet.xls"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)