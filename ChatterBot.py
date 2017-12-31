# Dependencies
import tweepy
import json
import time


# Twitter API Keys
consumer_key = "7TlA9v2GbHF3ULBa3IcJMOFHB"
consumer_secret = "6ONQkhVXU5bP2DVOIpk0ygt6RXSZcrFbRjUDpF73IhfjGgl0qN"
access_token = "944048582826397696-K562QtFCN9Re9I30ksQyiR6xvZj7XHa"
access_token_secret = "0o7PG1syI2uEruYbWYNDNiQ2eFGlcEUdOQAHJ698DzYfv"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def tweetOut():
    currentsec = int(time.time())
    api.update_status('It has been {:,} seconds since the epoch (1 Jan 1970)'.format(currentsec))

for x in range(60):
    tweetOut()
    time.sleep(60)
