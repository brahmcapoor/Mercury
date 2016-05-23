import tweepy
import twitter_confidential


auth = tweepy.OAuthHandler(**twitter_confidential.get_consumer_info())
auth.set_access_token(**twitter_confidential.get_access_info())

api = tweepy.API(auth)


def postTweet(tweet):
    status = api.update_status(status=tweet)


def checkTweet():
    pass
    """
    Conditions: length. Anything else?
    """
