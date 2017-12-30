# Dependencies
import tweepy
import json
import time
import time


# Twitter API Keys
consumer_key = "7TlA9v2GbHF3ULBa3IcJMOFHB"
consumer_secret = "6ONQkhVXU5bP2DVOIpk0ygt6RXSZcrFbRjUDpF73IhfjGgl0qN"
access_token = "944048582826397696-hFW38T3AEloUaxEZv9er58Ch804HFLJ"
access_token_secret = "wcfyskPPMvNfwGrN6awRiW1hv1XNP9NYOM2iYHqk22j29"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def tweetOut(tweetCount):
    try:
        api.update_status('This is tweet #{}, but with a timer man!'.format(tweetCount))
    except:
        millis = int(round(time.time() * 1000))
        api.update_status('Tried to post duplicate {}'.format(millis))

for x in range(5):
    tweetOut(x)
    time.sleep(6)
