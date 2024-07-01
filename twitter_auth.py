import tweepy
import config

# setting authentication
auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

# setting the client
client = tweepy.Client(
    config.bearer_token,
    config.api_key,
    config.api_key_secret, 
    config.access_token, 
    config.access_token_secret)