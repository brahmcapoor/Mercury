import tweepy
import os

"""
deals with the tweepy API i.e. handling tweets and updating description
TODO: deal with mentions
"""

auth = tweepy.OAuthHandler(
    os.environ['twitter_consumer_key'],
    os.environ['twitter_consumer_secret'])
auth.set_access_token(
    os.environ['twitter_access_key'],
    os.environ['twitter_access_secret'])
api = tweepy.API(auth)


def post_tweet(tweet):
    status = api.update_status(status=tweet)


def update_description(about):
    api.update_profile(description=about)
