#!/usr/bin/python3

import tweepy
import collections
import json
import time

def get_tweets():
    tweets = []
    twit = {}
    f = open('tweets.json', 'w')
    auth = tweepy.OAuthHandler("CONSUMER_TOKEN", "CONSUMER_SECRET")
    auth.set_access_token("ACESS_TOKEN", "ACCESS_SECRET")
    api = tweepy.API(auth)
    #public_tweets = api.search('#google')
    for tweet in tweepy.Cursor(api.search, q="#YOURHASHTAG", rpp=20).items(10):
        #user = "@" .. tweet.user.screen_name
        twit = { "user": "@" + tweet.user.screen_name, 
                 "text": tweet.text
        }
        tweets.append(twit)
    #print("@" + tweet.user.screen_name + ": " + tweet.text)
    #print("---")
    json.dump(tweets, f, ensure_ascii=False)
    return tweets

def print_tweets( tweets ):
    for elem in tweets:
        print("@" + elem['user'] + ": " + elem['text'])
        print ("---")

while 1:
    print("Fetching tweets.\n")
    twits = get_tweets()
    print_tweets(twits)
    time.sleep( 20 )
    

