#!/usr/bin/python3

import tweepy
import collections
import json
import time
import configparser
import sys

config = configparser.ConfigParser()
filename = "config.ini"
delay = 20

def parse_args():
    global filename
    global delay
    for i in range(len(sys.argv)):
        if ( sys.argv[i] == "-c" ):
            i += 1
            filename = sys.argv[i]
        elif (sys.argv[i] == "-d" ):
            i += 1
            delay = int(sys.argv[i])


    print(filename)
    print(delay)
def parse_config(filename):
    config.read(filename)

def get_tweets():
    tweets = []
    twit = {}
    f = open('tweets.json', 'w')
    auth = tweepy.OAuthHandler(config['Consumer']['token'], config['Consumer']['secret'])
    auth.set_access_token(config['Access']['token'], config['Access']['secret'])
    api = tweepy.API(auth)
    #public_tweets = api.search('#google')
    for tweet in tweepy.Cursor(api.search, q=config['General']['hashtag'], rpp=20).items(10):
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
    print("Parse config file")
    parse_args()
    parse_config(filename)
    print("Fetching tweets.\n")
    twits = get_tweets()
    print_tweets(twits)
    time.sleep(delay)
    

