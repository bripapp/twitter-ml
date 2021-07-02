import tweepy
import time
import pandas as pd

pd.set_option('display.max_colwidth', 1000)

# define keys and tokens
api_key = "API KEY" 
api_secret_key = "SECRET API KEY"
access_token = "ACCESS TOKEN"
access_secret_token = "SECRET ACCESS TOKEN"

# api authentication
authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_secret_token)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    tweets_list = []
    count = 50

    try:
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            tweets_list.append({
                'created_at': tweet.created_at,
                'tweet_id': tweet.id,
                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)
    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)