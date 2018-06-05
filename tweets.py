import tweepy
import json
from auth import get_api

api = get_api()

def search_tweets(query, count):
    return [{'id':status.id, 'text':status.text} for status in tweepy.Cursor(api.search, q=query).items(count)]

# topic = input("Enter topic: " )
# numbertweets = int(input("Enter number of tweets: "))
    
tweets = search_tweets("brexit", 5)

for tweet in tweets:
    print(tweet)


