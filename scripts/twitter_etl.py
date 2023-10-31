import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def twitter_etl():
    access_key = "4sUO94qjbzdWovCGjU43rg8B8"
    access_secret = "AXbK9jeQ0U1LReTzvGHfgYUHZCjTuCTdMFSwGoqmCLn8TwWpF7"

    consumer_key = "1668525660112060416-ZzBTBPM5kddlxe3KkhWo2dtFvEfhD8"
    consumer_secret = "ShPGXmOu6gIEruUCX3vYHPQLjqxIfo95HP8b4KvftFFaT"

    auth = tweepy.OAuthHandler(access_key,access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name = "@elonmusk",
                            count = 2,
                            include_rts = False,
                            tweet_mode = 'extended')
    print(tweets)

    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full text"]


        refined_tweet = {"user" : tweet.user.screen_name,
                        "text" : text,
                        "favourite_count" : tweet.favourite_count,
                        "created_at" : tweet.created_at}
        

        tweet_list.append(refined_tweet)

    df = pd.DataFrame(refined_tweet)
    df.to_csv("elon_musk.csv")