import tweepy
import time
import pandas as pd

#from config import api_key, api_secret_key, access_token, access_token_secret

pd.set_option('display.max_colwidth', 1000)

# define keys and tokens
api_key = "a1FlXVMCqmmvEPForypkPsjv5"
api_secret_key = "pvNHoHckf9Mgn4GKRHrCzkQgZ5c3NDOM9Ho5Qbm1SQ97Ge0Tr3"
access_token = "193957391-81gXwxmOYK0Mk0GIVF36vw3vCojovgaKwwEdDmiX"
access_token_secret = "5PqkhEZIsATzOtutnbi1qyk34x0Zpwazuco1yGn1XH69j"

# api authentication
authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
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