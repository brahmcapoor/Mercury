#MoodyBot

> Brahm Capoor and Michael Troute

##Overview

We're going to make a twitter bot that every day, decides what its mood is, and then periodically posts tweets based on that mood. Perhaps one day it'll be optimistic, and the next deluded. In addition to that, it'll respond to people mentioning it in tweets. Tell it to cheer up, and it'll change its mood to happy. Point out it's a bot, on the other hand, and it'll start feeling existential. 

##Background

Robot are cool and the world needs more of them.

There isn't much more to say here, really. Both of us have enjoyed reading about and talking about twitter bots in the past and we thought it might be fun to make one. We think that the idea of it changing moods and responding to user commands is exciting and that we have a relatively new take on it. 

Neither of us have really done something like this in the past or meaningfully used any of the technologies we're planning to use so it's also going to be a learning experience for us. 

##Implementation Strategy

Every 24 hours, the Bot will choose a random new mood from the collection of moods we give it. It'll then periodicially post tweets based on its mood.

We're going to use [Markovify](https://github.com/jsvine/markovify) to actually generate tweets. It has a method that generates short sentences which are ideal for tweets. To generate a corpus for the Markov Chains, we're going to use GoodReads' collections of quotes. Some of these are:

We'll use requests and BeautifulSoup to parse these quotes and save them in separate txt files based on which emotion they correspond to. If we need more quotes, they shouldn't be hard to find.

We'll use the [Tweepy](https://github.com/tweepy/tweepy) library to handle all the twitter stuff, which will primarily consist of posting tweets that the Markov Chain generates. It has a bunch of methods telling us whether a string is valid and so on, and we can use those to do some basic checking.

Periodically, we'll also check to see if the Bot has been mentioned by another user and if what that user has said represents a shift in mood, the bot will change its mood accordingly. If we don't have that much time, we'll have a list of explicit commands to change the bot's mood. If we do have time, we'll have the bot check for emotional cues by looking at synonyms of the words that the user uses. [NLTK](http://www.nltk.org/) can help us do this, but if we have enough time, we might make a more custom synonym trawler. 

Also, we need to figure out a way to have the bot running continuously. 

##Tasks

1. Create a twitter account with a good name
2. Authenticate with the twitter API
3. Generate a database of txts associated with a particular emotion using quotes from Goodreads.
4. Have the bot change its mood every day
5. Periodically generate a tweet using Markovify on the relevant emotion txt
6. Post the tweet
7. Have the bot check when its mentioned
8. If the mention is a valid command, change the bot's mood
9. *(Stretch)* Have the bot trawl synonyms of the words in the mention to understand what the user wants using nltk
10. *(Stretch)* Build a custom synonym trawler
11. *(Stretch)* If the bot doesn't understand the user's tweet, use the cleverbot API to make a clever response


###Estimated Timeline

**(Core)**

* Tasks 1 & 2 (30 minutes) - both
* Task 3 (1 hr) - Brahm
* Task 4 (30 minutes) - Michael
* Task 5 (1 hr) - both
* Task 6 (20 minutes) - both 
* Task 7 & 8 (1.5 hr) - both

**(Stretch)**
* Task 9 (2 hr) - Brahm 
* Task 10 (2 hr) - Michael
* Task 11 (1 hr) - both


##Resources
We're basically just going to be using the APIs we talked about.

