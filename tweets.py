import tweepy
import json
from auth import get_api

api = get_api()

def search(query, count):
    return [status for status in tweepy.Cursor(api.search, q=query).items(count)]

topic = input("Enter topic: " )
numbertweets = int(input("Enter number of tweets: "))
    
tweets = search(topic, numbertweets)

for tweet in tweets:
    print(tweet.text)


