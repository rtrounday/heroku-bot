# Create a function that tweets
# Dependencies
import tweepy
import json
import time

# Twitter API Keys
import os
# consumer_key = os.getenv("twitter_consumer_key")
# consumer_secret = os.getenv("twitter_consumer_secret")
# access_token = os.getenv("twitter_access_token")
# access_token_secret = os.getenv("twitter_access_token_secret")
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_LEVEL



# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_LEVEL)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(f"practice tweet from python script deployed to heroku: #{tweet_number}!")

# Create a function that calls the TweetOut function every minute
counter = 0

t_end = time.time() + 60 * 5
while(time.time() < t_end):
    TweetOut(counter)
    time.sleep(60)
    counter = counter + 1
