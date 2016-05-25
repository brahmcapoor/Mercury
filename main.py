# -*- coding: utf-8 -*-

"""
Currently just a testing harness for other modules
"""
import tweets
import emotionDatabase
import markovify
import time

moods = [
    'happy',
    'existential',
    'contemptuous',
    'sad',
    'innovative',
    'suspicious',
    'disgusted',
    'surprised',
    'funny',
    'inspirational',
    'romantic',
    'philosophical',
    'wise']


def generateDatabase():
    emotionDatabase.create_emotion_database(moods)


def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def test_quote(mood):
    filename = ("emotions/{}.txt").format(mood)
    with open(filename, encoding='utf-8') as f:
        text = f.read()

    text = strip_non_ascii(text)

    text_model = markovify.Text(text)

    sentence = text_model.make_short_sentence(130)

    return sentence.encode('utf-8')


def test_quotes():
    for mood in moods:
        print(("{}: {}").format(mood, test_quote(mood)))


def post_tweets(delay):
    while(True):
        for mood in moods:
            tweets.postTweet(("{}: {}").format(mood, test_quote(mood)))
        time.sleep(3600)


def main():
    # generateDatabase()
    test_quotes()
    # post_tweets(10)


if __name__ == "__main__":
    main()
