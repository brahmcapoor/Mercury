import tweepy
import twitter_confidential
import os


auth = tweepy.OAuthHandler(
    os.environ.get('twitter_consumer_key'),
    os.environ.get('twitter_consumer_secret'))
auth.set_access_token(
    os.environ.get('twitter_access_key'),
    os.environ.get('twitter_access_secret'))
api = tweepy.API(auth)


def post_tweet(tweet):
    status = api.update_status(status=tweet)


def update_description(about):
    api.update_profile(description=about)
