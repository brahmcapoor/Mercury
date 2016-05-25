# -*- coding: utf-8 -*-

"""
Currently just a testing harness for other modules
"""
import tweets
import emotionDatabase
import markovify

moods = [
    'happiness',
    'existentialism',
    'contempt',
    'sadness',
    'innovation',
    'suspicion',
    'disgust',
    'surprise']


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

    sentence = text_model.make_short_sentence(140)

    return sentence.encode('utf-8')


def test_quotes():
    for mood in moods:
        print(("{}: {}").format(mood, test_quote(mood)))


def main():
    # generateDatabase()
    test_quotes()


if __name__ == "__main__":
    main()
