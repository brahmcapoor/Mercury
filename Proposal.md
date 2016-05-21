#Mercury

> Brahm Capoor and Michael Troute

##Overview

We're going to make a twitter bot that starts each day by choosing a mood, and posts tweets over the course of the day that correspond to that mood. One day it might be happy, the next existential, the next angry. In addition, it'll change it's mood according to the content of tweets directed at it by other users. If another user tells the bot to cheer up, it'll change it's mood to happy. Point out it's a bot, on the other hand, and it'll start feeling existential.

##Background

Robots are cool and the world needs more of them.

There isn't much more to say here, really. Both of us have enjoyed reading about and talking about twitter bots in the past and we thought it might be fun to make one. We think that the idea of it changing moods and responding to user commands is exciting and that we have a relatively new take on it. None of the individual pieces of the project are overwhelmingly complex on their own, but implementing them all will give us lots of experience with using Python packages that we haven't been exposed to before.

##Implementation Strategy

Every 24 hours, the Bot will choose a random new mood from the collection of moods we give it. It'll then periodicially post tweets based on its mood.

We're going to use [Markovify](https://github.com/jsvine/markovify) to generate Markov chains from a corpus. Markovify also includes a method that generates short sentences which are ideal for tweets. To generate a corpus for the Markov Chains, we're going to use GoodReads' collections of quotes. Some of these are:

[Happy](https://www.goodreads.com/quotes/tag/happiness)
[Existential](https://www.goodreads.com/quotes/tag/existentialism)
[Contemptuous](https://www.goodreads.com/quotes/tag/contempt)

We'll use [Requests](http://docs.python-requests.org/en/master/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to parse these quotes and save them in separate .txt files based on which emotion they correspond to. Hopefully the Goodreads quotes will provide a large enough corpus, but if we need more text, it shouldn't be hard to find.

We'll use the [Tweepy](https://github.com/tweepy/tweepy) library to handle the all the Twitter API stuff, which will primarily consist of posting tweets that the Markov Chain generates and retrieving and examining tweets that contain mentions of the bot's account. It includes a bunch of methods telling us whether a string is valid and so on, which we can use to do some basic checking.

If we don't have that much time left once we've finished the basic functionality, we'll have a list of explicit commands that change the bot's mood. If we do have time, we'll have the bot check for emotional cues by looking at synonyms of the words that the user uses. [NLTK](http://www.nltk.org/) can help us do this, but if we have enough time, we might make a more custom synonym trawler.

Also, we need to figure out a way to have the bot running continuously.

##Tasks

1. Create a twitter account with a good name.
2. Figure out the Twitter API (authentication, tweet posting, tweet retrieval, etc.).
3. Generate a series of corpora corresponding to emotions using the quote collections from Goodreads.
4. Get the bot running constantly, and handle the daily mood swing.
5. Handle tweet generation by using Markovify on the relevant emotional corpus.
6. Make the bot react to tweets that mention it by potentially changing it's mood.
7. *(Stretch)* Have the bot trawl synonyms of the words in the mention to understand what the user wants using nltk
8. *(Stretch)* Build a custom synonym trawler
10. *(Stretch)* If the bot doesn't understand the user's tweet, use the cleverbot API to make a clever response
11. *(Stretch)* Have the bot occasionally post pictures of how it's feeling
12. *(Stretch)* Give the bot a 'wakeup' and 'sleep' time to give the impression it actually sleeps at nightl Have these times change based on its mood.
13. *(Stretch)* Time dependent tweets


###Estimated Timeline

**(Core)**

* Tasks 1 & 2 (30 minutes) - both
* Task 3 (1 hr) - Brahm
* Task 4 (30 minutes) - Michael
* Task 5 & 6 (3 hrs) - Brahm

**(Stretch)**
* Task 7 (2 hr) - Brahm
* Task 8 (2 hr) - Michael
* Task 9 (1 hr) - both
* Task 10 (1 hr) - both
* Task 11 (1 hr) - both
* Tasks 12 - 13 (2.5 hrs) - both


##Resources
We're basically just going to be using the APIs we talked about.
