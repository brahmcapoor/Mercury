# -*- coding: utf-8 -*-

import tweets
import utils
import moods
import markovify
from datetime import date, datetime
import time


def generate_tweet_text(mood):
    mood = mood.strip()
    filename = ("emotions/{}.txt").format(mood)
    with open(filename, encoding='utf-8') as f:
        text = f.read()

    text = utils.strip_non_ascii(text)

    text_model = markovify.Text(text)

    sentence = text_model.make_short_sentence(130)

    return sentence.encode('utf-8')


def test_quotes():
    for mood in moods.moods:
        print(("{}: {}").format(mood, test_quote(mood)))


def post_tweets(delay):
    while(True):
        for mood in moods.moodList():
            tweets.postTweet(("{}: {}").format(mood, test_quote(mood)))
        time.sleep(3600)


def reconstruct_date(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    return date


def main():
    while(True):
        with open('bot_state.txt', 'r+') as f:
            olddate = reconstruct_date(f.readline().strip())
            if date.today() > olddate.date():
                f.seek(0)
                f.write(str(date.today()))
                f.write('\n')
                emotion = moods.choose_random_mood()
                f.write(emotion + "             ")
                tweets.update_description(
                    "I'm feeling {} today".format(emotion))
            else:
                emotion = f.readline()
            text = generate_tweet_text(emotion)
            tweets.post_tweet(text)
         time.sleep(1800)


if __name__ == "__main__":
    main()
