# Mercury

A twitter bot that generates tweets based on its mood. Made in collaboration with Michael Troute (@troute and SUNET: mtroute). The bot runs on heroku

##Technical Details

We generated several corpora of quotes corresponding to various emotions from goodreads and saved them as separate txt files. Every day, the bot chooses a new emotion and starts generating tweets based on the mood. It does so by creating markov chains of maximum length 120 and then appending a hashtag, which is a synonym of the emotion.

##Packages used

* Markovify - to generate the tweets
* Tweepy - to handle the twitter API
* PyDictionary - to find synonyms of words
* BeautifulSoup & Requests - to scrape goodreads for quotes

##Testing

You can check the [account of the bot](https://twitter.com/mercurialbot), or implement it in your own account or alternatively, you can replace line 52 in main.py with `print(text)` and delete line 53 to generate tweets more quickly

##Todo

Respond to twitter mentions. We haven't had time to implement this yet
