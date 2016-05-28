# -*- coding: utf-8 -*-

import tweets
import utils
import moods
import markovify
from datetime import date, datetime
import time
from random import choice
from PyDictionary import PyDictionary
dictionary = PyDictionary()


def generate_tweet_text(mood):
    mood = mood.strip()
    filename = ("emotions/{}.txt").format(mood)
    with open(filename, encoding='utf-8') as f:
        text = f.read()

    text = utils.strip_non_ascii(text)

    text_model = markovify.Text(text)

    sentence = text_model.make_short_sentence(120)

    synonymset = dictionary.synonym(mood)
    synonym = choice(synonymset)

    sentence += " #{}".format(synonym)

    return sentence.encode('utf-8')


def main():
    emotion = "innovative"
    olddate = date(2016, 1, 1)
    while(True):
        if date.today() > olddate:
            olddate = date.today()
            emotion = moods.choose_random_mood()
            tweets.update_description(
                "Mercurial means changing moods quickly and often. That sounds like fun. I'm feeling {} today".format(emotion))
        else:
            tweets.update_description(
                "Mercurial means changing moods quickly and often. That sounds like fun. I'm feeling {} today".format(emotion))
        text = generate_tweet_text(emotion)
        tweets.post_tweet(text)
        time.sleep(1800)

if __name__ == "__main__":
    main()
