import tweepy
import twitter_confidential


auth = tweepy.OAuthHandler(**twitter_confidential.get_consumer_info())
auth.set_access_token(**twitter_confidential.get_access_info())
api = tweepy.API(auth)


def post_tweet(tweet):
    status = api.update_status(status=tweet)


def update_description(about):
    api.update_profile(description=about)
