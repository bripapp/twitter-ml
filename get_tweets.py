import tweepy
import time
import pandas as pd
# pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.expand_frame_repr', False)


# api key
api_key = "a1FlXVMCqmmvEPForypkPsjv5"
# api secret key
api_secret_key = "pvNHoHckf9Mgn4GKRHrCzkQgZ5c3NDOM9Ho5Qbm1SQ97Ge0Tr3"
# access token
access_token = "193957391-81gXwxmOYK0Mk0GIVF36vw3vCojovgaKwwEdDmiX"
# access token secret
access_token_secret = "5PqkhEZIsATzOtutnbi1qyk34x0Zpwazuco1yGn1XH69j"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)