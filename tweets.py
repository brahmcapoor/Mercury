import tweepy

consumer_key = "hxPJmpi2a2OrpOyOyyfYZxEfV"
consumer_secret = "WXnuoWKxdbpKpXl3t3sjSUUXZpzLWr7QbQ9QEgENShLvMZjAn8"
access_token = "734860294179033088-9JcS4eiVsfQ48pSX2k5NEEJNp945j94"
access_token_secret = "hp6nmAKJk9wgZLYT7jBqGbM2v3vZmdMo1F2VuACO5NEZV"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def postTweet(tweet):
    try:
        status = api.update_status(status=tweet)
    except:
        print("Tweet failed to post!")


def checkTweet():
    pass
