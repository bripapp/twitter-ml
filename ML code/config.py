# import required libraries
import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "a1FlXVMCqmmvEPForypkPsjv5"
# api secret key
api_secret_key = "pvNHoHckf9Mgn4GKRHrCzkQgZ5c3NDOM9Ho5Qbm1SQ97Ge0Tr3"
# access token
access_token = "193957391-81gXwxmOYK0Mk0GIVF36vw3vCojovgaKwwEdDmiX"
# access token secret
access_token_secret = "5PqkhEZIsATzOtutnbi1qyk34x0Zpwazuco1yGn1XH69j"

# authorize the API Key
authentication = tweepy.oAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the api
api = tweepy.API(authentication, wait_on_rate_limit=True)

