import tweepy
import json
from auth import get_api

api = get_api()

def search(query, count):
    return [status for status in tweepy.Cursor(api.search, q=query).items(count)]

topic = input("Enter topic: " )
numbertweets = int(input("Enter number of tweets: "))
    
tweets = search(topic, numbertweets)

print("Text of tweet: " + tweets[0].text)
print("User's screen name: " + tweets[0].user.screen_name)
hashtags = [h["text"] for h in tweets[0].entities["hashtags"]]
print("Hashtags: " + str(hashtags))
print("User's followers: " + str(tweets[0].user.followers_count))
print("User's friends: " + str(tweets[0].user.friends_count))
print("User's Tweet Count: " + str(tweets[0].user.statuses_count))

